import os
from dotenv import load_dotenv
from flask import Flask, jsonify, render_template
from flask_cors import CORS
from flask_login import LoginManager
from flask_socketio import SocketIO

# New structure imports
from routes.advanced import adv_bp
from routes.api import api_bp
from routes.auth import auth_bp
from models.models import User, db
from utils.socket_events import register_socket_events

load_dotenv()

socketio = SocketIO(cors_allowed_origins="*", async_mode="threading")
login_manager = LoginManager()

def create_app():
    # Root of the project is where app.py is now
    project_root = os.path.abspath(os.path.dirname(__file__))
    
    app = Flask(
        __name__,
        static_folder='static',
        template_folder='templates'
    )
    
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "mindtrack-dev-secret")
    
    # DB in project root
    db_file = os.path.join(project_root, "mindtrack.db")
    default_database_url = f"sqlite:///{db_file}"
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL", default_database_url)
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SESSION_COOKIE_SAMESITE"] = "Lax"
    app.config["SESSION_COOKIE_HTTPONLY"] = True

    CORS(
        app,
        supports_credentials=True,
        origins=[
            "http://localhost:5000",
            "http://127.0.0.1:5000",
            "http://localhost:5500",
            "http://127.0.0.1:5500",
            "null",
        ],
    )
    
    db.init_app(app)
    login_manager.init_app(app)
    socketio.init_app(app)
    register_socket_events(socketio)

    app.register_blueprint(auth_bp)
    app.register_blueprint(api_bp)
    app.register_blueprint(adv_bp)

    @app.get("/")
    def serve_index():
        return render_template("index.html")

    @login_manager.user_loader
    def load_user(user_id):
        return db.session.get(User, int(user_id))

    @login_manager.unauthorized_handler
    def unauthorized():
        return jsonify({"error": "Unauthorized"}), 401

    with app.app_context():
        db.create_all()

    return app

app = create_app()

if __name__ == "__main__":
    port = int(os.getenv("PORT", "5000"))
    socketio.run(app, host="0.0.0.0", port=port, debug=True, allow_unsafe_werkzeug=True)
