from flask_wtf import FlaskForm
from wtforms import SelectMultipleField, RadioField, SubmitField, IntegerField, StringField
from wtforms.validators import DataRequired, NumberRange, Optional

population_choices = [
    ('SIB', 'SIB'), ('ACB', 'ACB'), ('ASW', 'ASW'), ('ESN', 'ESN'),
    ('GWD', 'GWD'), ('LWK', 'LWK'), ('MSL', 'MSL'), ('YRI', 'YRI'),
    ('CLM', 'CLM'), ('MXL', 'MXL'), ('PEL', 'PEL'), ('PUR', 'PUR'),
    ('CDX', 'CDX'), ('CHB', 'CHB'), ('CHS', 'CHS'), ('JPT', 'JPT'),
    ('KHV', 'KHV'), ('CEU', 'CEU'), ('FIN', 'FIN'), ('GBR', 'GBR'),
    ('IBS', 'IBS'), ('TSI', 'TSI'), ('BEB', 'BEB'), ('GIH', 'GIH'),
    ('ITU', 'ITU'), ('PJL', 'PJL'), ('STU', 'STU')
]

superpopulation_choices = [
    ('AFR', 'AFR (Africa)'), ('AMR', 'AMR (America)'), 
    ('EAS', 'EAS (East Asian)'), ('EUR', 'EUR (European)'), 
    ('SAS', 'SAS (South Asian)')
]

class ClusteringAnalysisForm(FlaskForm):
    populations = SelectMultipleField(
        'Select Populations', 
        choices=population_choices,
        validators=[DataRequired()],
        render_kw={"class": "form-control"}
    )
    superpopulations = SelectMultipleField(
        'Select Superpopulations', 
        choices=superpopulation_choices,
        validators=[Optional()],
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
        choices=population_choices,
        validators=[DataRequired()],
        render_kw={"class": "form-control"}
    )
    superpopulations = SelectMultipleField(
        'Select Superpopulations',
        choices=superpopulation_choices,
        validators=[DataRequired()],
        render_kw={"class": "form-control"}
    )
    num_ancestral_pops = IntegerField(
        'Number of Ancestral Populations (K)',
        validators=[DataRequired(), NumberRange(min=1, message='Must be at least 1')],
        render_kw={"class": "form-control"}
    )
    submit = SubmitField('Run Admixture Analysis', render_kw={"class": "btn btn-primary"})
    

class SNPSearchForm(FlaskForm):
    search_option = RadioField('Search By', 
    choices=[
        ('snp_id', 'SNP IDs'), 
        ('coordinates', 'Genomic Coordinates'), 
        ('gene_name', 'Gene Names')
    ], default='snp_id')
    snp_ids = StringField('SNP IDs')
    chromosome = StringField('Chromosome')
    start_position = StringField('Start Position')
    end_position = StringField('End Position')
    gene_names = StringField('Gene Names')
    populations = SelectMultipleField(
        'Select Populations', 
        choices=population_choices,
        validators=[Optional()],
        render_kw={"class": "form-control"}
    )
    superpopulations = SelectMultipleField(
        'Select Superpopulations', 
        choices=superpopulation_choices,
        validators=[Optional()],
        render_kw={"class": "form-control"}
    )
    submit = SubmitField('Search')

