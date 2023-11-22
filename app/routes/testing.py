from app.routes import api_blueprint
from flask import Response
import json

@api_blueprint.route("/test")
def test_route():
    return "Hello world"
