from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.database import db

# Import your blueprints
from app.routes.clustering import clustering
from app.routes.admixture import admixture
from app.routes.snp_search import snp_info_bp
from app.routes.aboutus import about_bp

# Initialize SQLAlchemy
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Configuration
    app.config['SECRET_KEY'] = 'qmuldeepinweb'
    # Updated database URI to point to the SQLite database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/lydiaobeng/Documents/Projects/GitHub/BIO727P-Team-Deepin/DeepinWebApp/mydb.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize extensions with app
    db.init_app(app)

    # Register blueprints
    app.register_blueprint(clustering, url_prefix='/clustering')
    app.register_blueprint(admixture, url_prefix='/admixture')
    app.register_blueprint(snp_info_bp, url_prefix='/snp_search')
    app.register_blueprint(about_bp, url_prefix='/aboutus')

    return app
