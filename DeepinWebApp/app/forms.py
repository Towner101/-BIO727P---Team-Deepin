from flask_wtf import FlaskForm
from wtforms import SelectMultipleField, RadioField, SubmitField, IntegerField
from wtforms.validators import DataRequired, NumberRange

class ClusteringAnalysisForm(FlaskForm):
    populations = SelectMultipleField(
        'Select Populations', 
        choices=[], 
        validators=[DataRequired()], 
        render_kw={"class": "form-control"}
    )
    analysis_method = RadioField(
        'Select Analysis Method', 
        choices=[('PCA', 'PCA'), ('MDS', 'MDS'), ('UMAP', 'UMAP')], 
        validators=[DataRequired()], 
        render_kw={"class": "form-check-input"}
    )
    submit = SubmitField(
        'Analyse', 
        render_kw={"class": "btn btn-primary"}
    )

class AdmixtureAnalysisForm(FlaskForm):
    populations = SelectMultipleField(
        'Select Populations', 
        choices=[], 
        validators=[DataRequired()],
        render_kw={"class": "form-control"}
    )
    num_ancestral_pops = IntegerField(
        'Number of Ancestral Populations (K)', 
        validators=[
            DataRequired(), 
            NumberRange(min=1, message='Must be at least 1')
        ],
        render_kw={"class": "form-control"}
    )
    submit = SubmitField(
        'Run Admixture Analysis',
        render_kw={"class": "btn btn-primary"}
    )