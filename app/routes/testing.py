from flask import Blueprint

test_blueprint = Blueprint('test', __name__)

@test_blueprint.route("/test")
def test_route():
    return "Hello world"
