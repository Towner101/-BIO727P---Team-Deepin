from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.routes.main import main  
from app.routes.clustering import clustering
from app.routes.admixture import admixture
from app.routes.snp_search import snp_info
from app.routes.aboutus import about_bp


db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'qmuldeepinweb'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///SNPdatabase.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    db.init_app(app)
    
    # Register blueprints
    app.register_blueprint(main)
    app.register_blueprint(clustering, url_prefix='/clustering')
    app.register_blueprint(admixture, url_prefix='/admixture')  
    app.register_blueprint(snp_info, url_prefix='/snp_search')
    app.register_blueprint(about_bp, url_prefix='/aboutus')
    
    return app



