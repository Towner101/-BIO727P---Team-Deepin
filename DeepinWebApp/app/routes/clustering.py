from flask import Blueprint, request, render_template
from flask_sqlalchemy import SQLAlchemy
from app.forms import ClusteringAnalysisForm
from app.models import SampleTable, FinalAnalysisResults
import pandas as pd
import matplotlib.pyplot as plt
import base64
import io
from sklearn.decomposition import PCA

clustering = Blueprint('clustering', __name__)
db = SQLAlchemy()

@clustering.route('/clustering', methods=['GET', 'POST'])
def clustering_analysis():
    form = ClusteringAnalysisForm()

    if form.validate_on_submit():
        selected_populations = form.populations.data
        selected_superpopulations = form.superpopulations.data

        # Adjust your query as necessary, filtering by selected populations and superpopulations if provided
        query = db.session.query(SampleTable.POP, SampleTable.SUPER_POP, 
                                 FinalAnalysisResults.PCA1, FinalAnalysisResults.PCA2)\
                          .join(FinalAnalysisResults, SampleTable.SAMPLE_ID == FinalAnalysisResults.SAMPLE_ID)

        if selected_populations:
            query = query.filter(SampleTable.POP.in_(selected_populations))
        if selected_superpopulations:
            query = query.filter(SampleTable.SUPER_POP.in_(selected_superpopulations))

        df = pd.read_sql(query.statement, db.engine)

        # Perform PCA and plotting if data is not empty
        if not df.empty:
            pca = PCA(n_components=2)
            pca_result = pca.fit_transform(df[['PCA1', 'PCA2']])
            
            plt.figure(figsize=(10, 7))
            plt.scatter(pca_result[:, 0], pca_result[:, 1], alpha=0.7)
            plt.title('PCA Analysis')
            plt.xlabel('Principal Component 1')
            plt.ylabel('Principal Component 2')
            
            # Convert plot to PNG image
            img = io.BytesIO()
            plt.savefig(img, format='png')
            img.seek(0)
            plot_url = base64.b64encode(img.getvalue()).decode('utf8')
        else:
            plot_url = None

        return render_template('clustering_results.html', form=form, plot_url=plot_url)

    return render_template('clustering.html', form=form)
