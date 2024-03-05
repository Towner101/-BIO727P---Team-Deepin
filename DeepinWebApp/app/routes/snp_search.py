from flask import Blueprint, render_template
from app.forms import SNPSearchForm

snp_info_bp = Blueprint('snp_info', __name__)

@snp_info_bp.route('/snp_search', methods=['GET', 'POST'])
def snp_search():
    form = SNPSearchForm()
    results = None 
    error = None  

    if form.validate_on_submit():
        search_option = form.search_option.data
        selected_populations = form.populations.data

    return render_template('snp_search.html', form=form, results=results, error=error)
