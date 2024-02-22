from flask import Blueprint

#define the name of the Blueprint
auth = Blueprint('auth',__name__)

@auth.route('/snp/<int:snp_id>')
def snp(snp_id):
    snp_data = get_snp_data(snp_id)
    return render_template('snp.html', snp_data=snp_data)

#register the blueprint with the Flask app
def create_app():
    app = Flask(__name__)
    app.register_blueprint(auth)
    return app 