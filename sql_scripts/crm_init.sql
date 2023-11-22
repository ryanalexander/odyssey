INSERT INTO public."AssetTypes" ("TypeName")
VALUES ('CUSTOMER'), ('CASE');

INSERT INTO public."AssetProperties" ("AssetTypeID", "PropertyName", "DataType")
SELECT at."AssetTypeID", ap."PropertyName", ap."DataType"
FROM (VALUES
          ('Customer Name', 'VARCHAR(255)'),
          ('Email Address', 'VARCHAR(255)'),
          ('Phone Number', 'VARCHAR(255)'),
          ('Address', 'TEXT'),
          ('Customer Since', 'DATE')
     ) AS ap("PropertyName", "DataType")
         CROSS JOIN public."AssetTypes" at
WHERE at."TypeName" = 'CUSTOMER'

UNION ALL

SELECT at."AssetTypeID", ap."PropertyName", ap."DataType"
FROM (VALUES
          ('Case Title', 'VARCHAR(255)'),
          ('Description', 'TEXT'),
          ('Status', 'VARCHAR(255)'),
          ('Priority', 'VARCHAR(255)'),
          ('Assigned To', 'VARCHAR(255)'),
          ('Opened Date', 'TIMESTAMP'),
          ('Closed Date', 'TIMESTAMP')
     ) AS ap("PropertyName", "DataType")
         CROSS JOIN public."AssetTypes" at
WHERE at."TypeName" = 'CASE';


INSERT INTO public."Assets" ("AssetTypeID", "Name")
SELECT "AssetTypeID", 'John Doe' FROM public."AssetTypes" WHERE "TypeName" = 'CUSTOMER';

INSERT INTO public."Assets" ("AssetTypeID", "Name")
SELECT "AssetTypeID", 'Case 001' FROM public."AssetTypes" WHERE "TypeName" = 'CASE';

INSERT INTO public."AssetPropertyValues" ("AssetID", "PropertyID", "PropertyValue")
SELECT a."AssetID", ap."PropertyID",
       CASE
           WHEN ap."PropertyName" = 'Customer Name' THEN 'John Doe'
           WHEN ap."PropertyName" = 'Email Address' THEN 'johndoe@email.com'
           -- Other conditions here
           END
FROM public."Assets" a
         JOIN public."AssetProperties" ap ON a."AssetTypeID" = ap."AssetTypeID"
WHERE a."Name" = 'John Doe' AND ap."AssetTypeID" = (SELECT "AssetTypeID" FROM public."AssetTypes" WHERE "TypeName" = 'CUSTOMER')

UNION ALL

SELECT a."AssetID", ap."PropertyID",
       CASE
           WHEN ap."PropertyName" = 'Case Title' THEN 'Product Issue'
           -- Other conditions here
           WHEN ap."PropertyName" = 'Opened Date' THEN TO_CHAR(CURRENT_TIMESTAMP, 'YYYY-MM-DD HH24:MI:SS')
           -- Assuming Closed Date is NULL initially
           END
FROM public."Assets" a
         JOIN public."AssetProperties" ap ON a."AssetTypeID" = ap."AssetTypeID"
WHERE a."Name" = 'Case 001' AND ap."AssetTypeID" = (SELECT "AssetTypeID" FROM public."AssetTypes" WHERE "TypeName" = 'CASE');

INSERT INTO "AssetRelationships" ("ParentAssetID", "ChildAssetID", "RelationshipType") VALUES (
                                                                                              (SELECT "AssetID" FROM public."Assets" WHERE "Name" = 'John Doe'),
                                                                                              (SELECT "AssetID" FROM public."Assets" WHERE "Name" = 'Case 001'),
                                                                                               'Case'
                                                                                              )
