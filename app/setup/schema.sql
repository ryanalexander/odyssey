-- AssetTypes.sql

-- Create AssetTypes Table
CREATE TABLE AssetTypes (
    AssetTypeID INT AUTO_INCREMENT PRIMARY KEY,
    TypeName VARCHAR(255) UNIQUE NOT NULL,
    Description TEXT
);

-- Assets.sql

-- Create Assets Table
CREATE TABLE Assets (
    AssetID INT AUTO_INCREMENT PRIMARY KEY,
    AssetTypeID INT,
    Name VARCHAR(255) NOT NULL,
    CreatedAt DATETIME DEFAULT CURRENT_TIMESTAMP,
    CreatedBy VARCHAR(255),
    LastModified DATETIME ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (AssetTypeID) REFERENCES AssetTypes(AssetTypeID)
);

-- AssetProperties.sql

-- Create AssetProperties Table
CREATE TABLE AssetProperties (
    PropertyID INT AUTO_INCREMENT PRIMARY KEY,
    AssetTypeID INT,
    PropertyName VARCHAR(255) NOT NULL,
    DataType VARCHAR(255) NOT NULL,
    FOREIGN KEY (AssetTypeID) REFERENCES AssetTypes(AssetTypeID)
);

-- AssetPropertyValues.sql

-- Create AssetPropertyValues Table
CREATE TABLE AssetPropertyValues (
    AssetID INT,
    PropertyID INT,
    PropertyValue VARCHAR(255),
    FOREIGN KEY (AssetID) REFERENCES Assets(AssetID),
    FOREIGN KEY (PropertyID) REFERENCES AssetProperties(PropertyID),
    PRIMARY KEY (AssetID, PropertyID)
);

-- AssetRelationships.sql

-- Create AssetRelationships Table
CREATE TABLE AssetRelationships (
    RelationshipID INT AUTO_INCREMENT PRIMARY KEY,
    ParentAssetID INT,
    ChildAssetID INT,
    RelationshipType VARCHAR(255) NOT NULL,
    FOREIGN KEY (ParentAssetID) REFERENCES Assets(AssetID),
    FOREIGN KEY (ChildAssetID) REFERENCES Assets(AssetID)
);


-- Create functions

CREATE OR REPLACE FUNCTION public.get_asset(asset_id INT)
    RETURNS JSON
    LANGUAGE plpgsql
AS $$
DECLARE
    _property_name TEXT;
    _property_type TEXT;
    _sql TEXT;
    _result JSON;
    _relationship_json JSON;
BEGIN
    -- Start building the JSON object
    _sql := 'SELECT json_build_object(''AssetID'', a."AssetID", ''Name'', a."Name"';

    -- Loop through each property and add it to the JSON object
    FOR _property_name, _property_type IN
        SELECT "PropertyName", "DataType"
        FROM public."AssetProperties"
        ORDER BY "PropertyName"
        LOOP
            _sql := _sql || ', ''' || _property_name || ''', MAX(CASE WHEN ap."PropertyName" = ''' || _property_name || ''' THEN ';

            -- Handle different data types
            CASE _property_type
                WHEN 'int' THEN _sql := _sql || 'CAST(apv."PropertyValue" AS INTEGER)';
                WHEN 'text' THEN _sql := _sql || 'apv."PropertyValue"';
                -- Add cases for other data types as necessary
                ELSE _sql := _sql || 'NULL'; -- Default case if data type is unknown
                END CASE;

            _sql := _sql || ' ELSE NULL END)';
        END LOOP;

    _sql := _sql || ') FROM public."Assets" a
                      JOIN public."AssetPropertyValues" apv ON a."AssetID" = apv."AssetID"
                      JOIN public."AssetProperties" ap ON apv."PropertyID" = ap."PropertyID"
                      WHERE a."AssetID" = ' || asset_id || '
                      GROUP BY a."AssetID", a."Name"';

    -- Execute the dynamic SQL for asset properties
    EXECUTE _sql INTO _result;

    -- Fetch and format relationships as a JSON array
    SELECT json_agg(json_build_object('RelationshipID', r."RelationshipID", 'ParentId', r."ParentAssetID", 'ChildId', r."ChildAssetID", 'Type', r."RelationshipType"))
    INTO _relationship_json
    FROM public."AssetRelationships" r
    WHERE r."ParentAssetID" = asset_id OR r."ChildAssetID" = asset_id;

    -- Combine properties and relationships into one JSON object
    RETURN json_build_object('Properties', _result, 'Relationships', _relationship_json);
END;
$$;
