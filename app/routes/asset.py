from app.routes import api_blueprint
from flask import Response
from sqlalchemy import text
import json

from app.utils.generic_utils import asset_ref_to_obj

@api_blueprint.get("/asset/<string:asset_id>")
def get_asset(asset_id):
    obj = asset_ref_to_obj(asset_id)
    
    # Return the asset data as JSON response
    return Response(json.dumps(resolve_asset(obj['row_id'])), mimetype='application/json', status=200)

def resolve_asset(asset_id, resolve_relationships=True):
    sql_query = text('SELECT * FROM get_asset(:asset_id)')
    
    sql_query = sql_query.bindparams(asset_id=asset_id)
    
    from app import app_instance
    result = app_instance.db.session.execute(sql_query)
    
    asset_data = result.fetchone()
    asset_dict = tuple(asset_data)[0]

    asset = {
        **asset_dict['Properties']
    }

    if resolve_relationships:
        for relationship in asset_dict['Relationships']:
            RelationshipID = relationship['RelationshipID']
            ParentId = relationship['ParentId']
            ChildId = relationship['ChildId']
            Type = relationship['Type']

            if ParentId == asset['AssetID']:
                continue
            
            if Type not in asset:
                asset[Type] = []
                
            asset[Type].append(resolve_asset(ParentId, False))
    return asset