from flask import Blueprint, render_template, request, redirect, url_for
from app.forms import ClusteringAnalysisForm, AdmixtureAnalysisForm, SNPSearchForm
from app.models.db_models import AnalysisResults, db
import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import io
import base64

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('index.html')

@main.route('/clustering', methods=['GET', 'POST'])
def clustering():
    form = ClusteringAnalysisForm()
    if form.validate_on_submit():
        selected_populations = form.populations.data
        # Query data for clustering based on selected populations
        results = AnalysisResults.get_results_for_clustering(selected_populations)
        return render_template('clustering_results.html', results=results)
    return render_template('clustering.html', form=form)

@main.route('/admixture', methods=['GET', 'POST'])
def admixture():
    form = AdmixtureAnalysisForm()
    if form.validate_on_submit():
        selected_superpopulations = form.superpopulations.data
        # Query data for admixture analysis based on selected superpopulations
        results = AnalysisResults.get_results_for_admixture(selected_superpopulations)
        return render_template('admixture_results.html', results=results)
    return render_template('admixture.html', form=form)

@main.route('/snp_search', methods=['GET', 'POST'])
def snp_search():
    form = SNPSearchForm()
    results = None  
    if form.validate_on_submit():
        pass
    return render_template('snp_search.html', form=form, results=results)

@main.route('/aboutus')
def about():
    return render_template('aboutus.html')
