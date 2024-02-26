from flask import Blueprint, render_template, request
from app.forms import SNPSearchForm
from app.models import SNP

snp_info_bp = Blueprint('snp_info', __name__)

@snp_info_bp.route('/snp_search', methods=['GET', 'POST'])
def snp_search():
    form = SNPSearchForm()
    results = None  # Initialize results as None to indicate no search has been performed yet
    error = None  # To capture and display any errors during search

    if form.validate_on_submit():
        search_option = form.search_option.data
        selected_populations = form.populations.data

        # Start building the query based on the SNP model
        query = SNP.query

        try:
            if search_option == 'snp_id':
                snp_ids = form.snp_ids.data.split(',')
                query = query.filter(SNP.snp_id.in_(snp_ids))
            elif search_option == 'gene_name':
                gene_names = form.gene_names.data.split(',')
                query = query.filter(SNP.gene_name.in_(gene_names))

            if selected_populations:
                query = query.filter(SNP.population.in_(selected_populations))

            results = query.all()
        except Exception as e:
            results = None  # Reset results to None in case of error
            error = str(e)  # Capture the error message

    return render_template('snp_search.html', form=form, results=results, error=error)
