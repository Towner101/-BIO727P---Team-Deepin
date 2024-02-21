from flask_wtf import FlaskForm
from wtforms import SelectMultipleField, RadioField, SubmitField
from wtforms.validators import DataRequired

class ClusteringAnalysisForm(FlaskForm):
    populations = SelectMultipleField('Select Populations', choices=[], validators=[DataRequired()])
    analysis_method = RadioField('Select Analysis Method', choices=[('PCA', 'PCA'), ('MDS', 'MDS'), ('UMAP', 'UMAP')], validators=[DataRequired()])
    submit = SubmitField('Analyze')
