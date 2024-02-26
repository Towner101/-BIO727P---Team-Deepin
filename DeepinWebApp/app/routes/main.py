from flask import Blueprint, app, render_template, request, redirect, url_for
from app.forms import ClusteringAnalysisForm, AdmixtureAnalysisForm, SNPSearchForm
from app.extensions import db
from app.models import SNP


main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('index.html')

@main.route('/clustering', methods=['GET', 'POST'])
def clustering():
    form = ClusteringAnalysisForm()
    if form.validate_on_submit():
        # Handle selected options and perform analysis
        return redirect(url_for('main.clustering'))
    return render_template('clustering.html', form=form)

@main.route('/admixture', methods=['GET', 'POST'])
def admixture():
    form = AdmixtureAnalysisForm()
    if form.validate_on_submit():
        selected_populations = form.populations.data
        num_ancestral_pops = form.num_ancestral_pops.data
        
        # Perform the admixture analysis with selected options
        return redirect(url_for('main.admixture'))  

    return render_template('admixture.html', form=form)

@main.route('/snp_search', methods=['GET', 'POST'])
def snp_search():
    form = SNPSearchForm()
    results = None  # Variable to hold query results

    if form.validate_on_submit():
        search_option = form.search_option.data
        populations = form.populations.data

        query = SNP.query  

        if search_option == 'snp_id':
            snp_ids = form.snp_ids.data.split(',')
            query = query.filter(SNP.snp_id.in_(snp_ids))
        elif search_option == 'gene_name':
            gene_names = form.gene_names.data.split(',')
            query = query.filter(SNP.gene_name.in_(gene_names))

        if populations:
            query = query.filter(SNP.population.in_(populations))

        results = query.all()  # Execute query and collect results

    return render_template('snp_search.html', form=form, results=results)

@main.route('/aboutus')
def about():
    return render_template('aboutus.html')


