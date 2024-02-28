from flask import Blueprint, render_template, request, redirect, url_for
from ..forms import AdmixtureAnalysisForm

admixture = Blueprint('admixture', __name__)

@admixture.route('/admixture', methods=['GET', 'POST'])
def admixture_analysis():
    form = AdmixtureAnalysisForm()
    form.populations.choices = [('pop1', 'Population 1'), ('pop2', 'Population 2')]  
    
    if form.validate_on_submit():
        selected_populations = form.populations.data
        num_ancestral_pops = form.num_ancestral_pops.data
        
    
        return redirect(url_for('admixture.admixture_analysis_results'))
    
    return render_template('admixture.html', form=form)


