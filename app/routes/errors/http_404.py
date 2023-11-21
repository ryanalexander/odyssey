from app.routes import api_blueprint
from flask import Response
import json

@api_blueprint.route('/', defaults={'path': ''})
@api_blueprint.route('/<path:path>')
def default(path):
    return Response(json.dumps({"message": "Invalid endpoint", "endpoint": path, "status": 404}), mimetype='application/json', status=404)
