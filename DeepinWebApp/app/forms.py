from flask_wtf import FlaskForm
from wtforms import SelectMultipleField, RadioField, SubmitField, IntegerField, StringField
from wtforms.validators import DataRequired, NumberRange, Optional

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

class SNPInformationForm(FlaskForm):  
    search_option = RadioField(
        'Search By', 
        choices=[('snp_id', 'SNP IDs'), ('coordinates', 'Genomic Coordinates'), ('gene_name', 'Gene Names')], 
        default='snp_id', 
        validators=[DataRequired()]
    )
    snp_ids = StringField('SNP IDs', validators=[Optional()])
    chromosome = StringField('Chromosome', validators=[Optional()])
    start_position = StringField('Start Position', validators=[Optional()])
    end_position = StringField('End Position', validators=[Optional()])
    gene_names = StringField('Gene Names', validators=[Optional()])
    populations = SelectMultipleField(
        'Select Populations', 
        choices=[('pop1', 'Population 1'), ('pop2', 'Population 2')], 
        validators=[Optional()]
    )
    submit = SubmitField('Search', render_kw={"class": "btn btn-primary"})
