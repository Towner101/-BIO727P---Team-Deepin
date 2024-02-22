from flask import Blueprint, render_template, request, redirect, url_for
from app.forms import ClusteringAnalysisForm
from app.forms import AdmixtureAnalysisForm
from app.forms import SNPInformationForm


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

@main.route('/admixture', methods=['GET', 'POST'])
def admixture():
    form = AdmixtureAnalysisForm()
    # Dynamically populate the 'choices' for 'populations'
    form.populations.choices = [('pop1', 'Population 1'), ('pop2', 'Population 2')]  # Example choices

    if form.validate_on_submit():
        selected_populations = form.populations.data
        num_ancestral_pops = form.num_ancestral_pops.data
        # Here, perform the admixture analysis with the selected options
        
        # Redirect or display results as needed
        # For example, you might redirect to a results page or back to the form page
        return redirect(url_for('main.admixture_results'))  # Example redirect

    return render_template('admixture.html', form=form)

@main.route('/snp_info', methods=['GET', 'POST'])
def snp_information():
    form = SNPInformationForm()
    if form.validate_on_submit():
        # Process form submission here
        # For example, extract form data and perform a query based on the selected search option
        search_option = form.search_option.data
        populations = form.populations.data
        
        if search_option == 'snp_id':
            snp_ids = form.snp_ids.data.split(',')  # Assuming multiple SNP IDs can be separated by commas
        elif search_option == 'coordinates':
            chromosome = form.chromosome.data
            start_position = form.start_position.data
            end_position = form.end_position.data
        elif search_option == 'gene_name':
            gene_names = form.gene_names.data.split(',')  # Assuming multiple gene names can be separated by commas

        # Redirect to a results page or back to the form page with query results
        # For demonstration, redirecting back to the form page
        return redirect(url_for('main.snp_info'))

    return render_template('snp_info.html', form=form)
