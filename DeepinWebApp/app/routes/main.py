from flask import Blueprint, render_template, request, redirect, url_for
from app.forms import ClusteringAnalysisForm, AdmixtureAnalysisForm, SNPSearchForm

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('index.html')

@main.route('/clustering', methods=['GET', 'POST'])
def clustering():
    form = ClusteringAnalysisForm()
    if form.validate_on_submit():
        selected_populations = form.populations.data
    
        return render_template('clustering_results.html')
    return render_template('clustering.html', form=form)

@main.route('/admixture', methods=['GET', 'POST'])
def admixture():
    form = AdmixtureAnalysisForm()
    if form.validate_on_submit():
        selected_superpopulations = form.superpopulations.data
        
        return render_template('admixture_results.html')
    return render_template('admixture.html', form=form)

@main.route('/snp_search', methods=['GET', 'POST'])
def snp_search():
    form = SNPSearchForm()
    results = None  
    if form.validate_on_submit():
        pass
    return render_template('snp_search.html', form=form)

@main.route('/aboutus')
def about():
    return render_template('aboutus.html')