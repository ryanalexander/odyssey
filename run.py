from app import create_app

app = create_app()

# Define global context. With the @app.context_processor decorator.

if __name__ == '__main__':
    app.run()  # Set debug=False in a production environment
