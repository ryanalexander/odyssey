from app.routes import api_blueprint
from flask import Response
import os
import json

@api_blueprint.errorhandler(500)
def internal_server_error(error):
    if os.getenv("debug") is True:
        return Response(json.dumps({"message": "Internal server error", "error": str(error), "status": 500}), mimetype='application/json', status=500)
    return Response(json.dumps({"message": "Internal server error", "status": 500}), mimetype='application/json', status=500)