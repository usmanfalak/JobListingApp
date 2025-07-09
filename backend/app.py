from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
from models import db
from routes import routes
import os

# Load environment variables from .env file
load_dotenv()  # ✅ This must be called BEFORE os.getenv

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///databse.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'fallbacksecret')

    CORS(app)
    db.init_app(app)

    app.register_blueprint(routes)

    # ✅ Create tables safely using app context
    with app.app_context():
        db.create_all()

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
