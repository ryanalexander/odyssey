from alembic.config import Config
from alembic import command
import os

def apply_migrations():
    # Set the Alembic configuration from the alembic.ini file
    alembic_cfg = Config(os.path.join(os.path.dirname(__file__), 'alembic.ini'))

    # Apply migrations up to the head
    command.upgrade(alembic_cfg, 'head')

if __name__ == "__main__":
    apply_migrations()
    print("All migrations have been applied.")
