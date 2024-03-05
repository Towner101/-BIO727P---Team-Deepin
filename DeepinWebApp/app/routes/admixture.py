from flask import Blueprint, render_template, request, flash, redirect, url_for
from app.forms import AdmixtureAnalysisForm

admixture = Blueprint('admixture', __name__)

@admixture.route('/admixture', methods=['GET', 'POST'])
def admixture_analysis():
    form = AdmixtureAnalysisForm()
    
    if form.validate_on_submit():
        
        selected_populations = form.populations.data
        num_ancestral_pops = form.num_ancestral_pops.data
        
        flash('Analysis submitted successfully.', 'success')
        return redirect(url_for('admixture.admixture_analysis'))
    
    return render_template('admixture.html', form=form)
