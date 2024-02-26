from flask import Blueprint, render_template, request, redirect, url_for, session
from app.forms import SNPSearchForm
from app.models import SNP
from app.extensions import db

snp_info = Blueprint('snp_search', __name__)

@snp_info.route('/snp_search', methods=['GET', 'POST'])
def snp_search():
    form = SNPSearchForm()
    results = []
    if form.validate_on_submit():
        search_option = form.search_option.data
        selected_populations = form.populations.data

        query = SNP.query

        if search_option == 'snp_id':
            snp_ids = form.snp_ids.data.split(',')
            query = query.filter(SNP.snp_id.in_(snp_ids))
        elif search_option == 'coordinates':
            chromosome = form.chromosome.data
            start_position = int(form.start_position.data)
            end_position = int(form.end_position.data)
            query = query.filter(SNP.chromosome == chromosome, SNP.position >= start_position, SNP.position <= end_position)
        elif search_option == 'gene_name':
            gene_names = form.gene_names.data.split(',')
            query = query.filter(SNP.gene_name.in_(gene_names))

        # Filter by selected populations
        if selected_populations:
            query = query.filter(SNP.population.in_(selected_populations))
        
        results = query.all()

    return render_template('snp_search.html', form=form, results=results)


