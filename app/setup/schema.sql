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
