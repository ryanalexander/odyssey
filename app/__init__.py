# Standard library imports
import logging
import os

# Third-party imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Local application imports
from app.setup.database_check import apply_migrations
from app.routes import api_blueprint
from app.utils.Logging import CustomFormatter

app_instance = None

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

        global app_instance
        app_instance = self

        self.flask_app = create_flask_app()
        self.apply_migrations_and_setup()
        self.setup_database_connection()

    def setup_database_connection(self):
        logging.info("Setting up database connection")
        self.flask_app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
        self.flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        self.db = SQLAlchemy(self.flask_app)
        logging.info("Database connection set up")

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
