from flask import Flask
from .routes.main import main  
from app.routes.clustering import clustering
from app.routes.admixture import admixture

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'qmuldeepinweb'
    
    # Register blueprints
    app.register_blueprint(main)
    app.register_blueprint(clustering, url_prefix='/clustering')
    app.register_blueprint(admixture, url_prefix='/admixture')  
    
    return app



