from waitress import serve
from app import app  # assuming your Flask app is in 'app.py'

if __name__ == "__main__":
    serve(app, host='0.0.0.0', port=8080)  # Bind to 0.0.0.0 for external access
