from flask import Blueprint, render_template, request
from ..forms import SNPInformationForm

snp_info = Blueprint('snp_info', __name__)

@snp_info.route('/snp_info', methods=['GET', 'POST'])
def snp_information():
    form = SNPInformationForm()
    search_results = None  # Placeholder for search results
    
    if form.validate_on_submit():
        search_option = form.search_option.data
        # Perform your search query based on the form input
        # Populate search_results with actual data from your database or data source
        
        # Example: search_results = perform_search(search_option, ...)
        
    # Render the same template whether or not the form has been submitted
    return render_template('snp_info.html', form=form, search_results=search_results)

