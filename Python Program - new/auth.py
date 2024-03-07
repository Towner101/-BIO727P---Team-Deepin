from flask import Blueprint

#define the name of the Blueprint
auth = Blueprint('auth',__name__)

#define authentication routes 
@auth.route('/login')
def login():
    return 'Login page'

@auth.route('/logout')
def logout():
    return 'Logout page'

#register the blueprint with the Flask app
def create_app():
    app = Flask(__name__)
    app.register_blueprint(auth)
    return app 