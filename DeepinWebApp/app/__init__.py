from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Import your blueprints
from app.routes.main import main as main_blueprint
from app.routes.clustering import clustering as clustering_blueprint
from app.routes.admixture import admixture as admixture_blueprint
from app.routes.snp_search import snp_info_bp as snp_info_blueprint
from app.routes.aboutus import about_bp as about_blueprint

def create_app():
    app = Flask(__name__)

    # Configuration
    app.config['SECRET_KEY'] = 'qmuldeepinweb'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app_database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    # Register blueprints with their URL prefixes
    app.register_blueprint(main_blueprint)
    app.register_blueprint(clustering_blueprint, url_prefix='/clustering')
    app.register_blueprint(admixture_blueprint, url_prefix='/admixture')
    app.register_blueprint(snp_info_blueprint, url_prefix='/snp_search')
    app.register_blueprint(about_blueprint, url_prefix='/aboutus')

    return app
