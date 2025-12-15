"""
Application start-point.

Creates the Flask application instance and runs the development server.
"""

from website import create_app

# create the application
app = create_app()

if __name__ == "__main__":
     # run Debug in development mode only
    app.run(debug=False)