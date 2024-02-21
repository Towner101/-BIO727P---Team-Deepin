from flask import Blueprint, render_template, request, redirect, url_for
from app.forms import ClusteringAnalysisForm

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('index.html')

@main.route('/clustering', methods=['GET', 'POST'])
def clustering():
    form = ClusteringAnalysisForm()
    if form.validate_on_submit():
        # Here you'll handle the selected options and perform the analysis
        # Redirect to the same page to demonstrate functionality
        return redirect(url_for('main.clustering'))
    return render_template('clustering.html', form=form)
