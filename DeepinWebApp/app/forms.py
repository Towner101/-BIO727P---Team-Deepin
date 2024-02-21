# app/forms.py
from flask_wtf import FlaskForm
from wtforms import SelectMultipleField, RadioField, SubmitField
from wtforms.validators import DataRequired

class ClusteringForm(FlaskForm):
    populations = SelectMultipleField('Select Populations or Superpopulations', choices=[('pop1', 'Population 1'), ('pop2', 'Population 2')], validators=[DataRequired()])
    analysis_type = RadioField('Select Analysis Type', choices=[('PCA', 'PCA'), ('MDS', 'MDS'), ('UMAP', 'UMAP')], validators=[DataRequired()])
    submit = SubmitField('Analyze')
