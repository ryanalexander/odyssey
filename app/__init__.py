from flask import Flask
from app.setup.database_check import apply_migrations
import logging
from app.utils.Logging import CustomFormatter

class App:
    def __init__(self):
        # Configure logger
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s [%(levelname)s] %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
            handlers=[logging.StreamHandler()]
        )

        # Apply the custom formatter
        for handler in logging.root.handlers:
            handler.setFormatter(CustomFormatter())

        # Initialize app
        logging.info("App initialized")
        logging.info("Applying database migrations")
        apply_migrations()
        logging.info("Database migrations applied")

        # Create Flask app instance
        self.flask_app = Flask(__name__)

        # Configure Flask app (if needed)
        self.configure_app()

        # Register Blueprints (if any)
        self.register_blueprints()

        # Any further pre-start tasks

    def configure_app(self):
        # App configuration settings
        pass

    def register_blueprints(self):
        # Register Flask blueprints
        pass

    def run(self):
        # Run Flask web server
        logging.info("Starting Flask web server")
        self.flask_app.run(debug=True)  # Set debug to False in production

def create_app():
    return App()
