# Standard library imports
import logging

# Third-party imports
from flask import Flask

# Local application imports
from app.setup.database_check import apply_migrations
from app.routes import api_blueprint
from app.utils.Logging import CustomFormatter

# Setup Logger
def configure_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        handlers=[logging.StreamHandler()]
    )

    for handler in logging.root.handlers:
        handler.setFormatter(CustomFormatter())

def create_flask_app():
    app = Flask(__name__)

    # Additional Flask configuration can be added here

    return app

class App:
    def __init__(self):
        configure_logging()
        logging.info("App initialized")

        self.flask_app = create_flask_app()
        self.apply_migrations_and_setup()

    def apply_migrations_and_setup(self):
        logging.info("Applying database migrations")
        apply_migrations()
        logging.info("Database migrations applied")
        self.register_blueprints()

    def register_blueprints(self):
        self.flask_app.register_blueprint(api_blueprint)

    def run(self):
        logging.info("Starting Flask web server")
        self.flask_app.run(debug=True)  # Set debug to False in production

def create_app():
    return App()
