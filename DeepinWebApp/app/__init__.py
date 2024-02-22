from flask import Flask
from app.routes.main import main  
from app.routes.clustering import clustering
from app.routes.admixture import admixture
from app.routes.snp_info import snp_info

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'qmuldeepinweb'
    
    # Register blueprints
    app.register_blueprint(main)
    app.register_blueprint(clustering, url_prefix='/clustering')
    app.register_blueprint(admixture, url_prefix='/admixture')  
    app.register_blueprint(snp_info, url_prefix='/snp_info')
    
    return app



