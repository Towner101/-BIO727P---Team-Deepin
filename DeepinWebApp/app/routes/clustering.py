from flask import Blueprint, render_template, request, flash, redirect, url_for
from ..forms import ClusteringAnalysisForm

clustering = Blueprint('clustering', __name__)

@clustering.route('/clustering', methods=['GET', 'POST'])
def clustering_analysis():
    form = ClusteringAnalysisForm()
    form.populations.choices = [('pop1', 'Population 1'), ('pop2', 'Population 2')]
    
    if form.validate_on_submit():
        selected_populations = form.populations.data
        selected_method = form.analysis_method.data
       
        flash('Analysis submitted for populations: {} using {}'.format(', '.join(selected_populations), selected_method))
        return redirect(url_for('clustering.clustering_analysis_results'))
    
    return render_template('clustering_analysis.html', form=form)
