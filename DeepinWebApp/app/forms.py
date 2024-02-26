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
        render_kw={"class": "form-control select2-multiple", "multiple": "multiple"}
    )
    superpopulations = SelectMultipleField(
        'Select Superpopulations',
        choices=superpopulation_choices,
        validators=[Optional()],
        render_kw={"class": "form-control select2-multiple", "multiple": "multiple"}
    )
    analysis_method = RadioField(
        'Select Analysis Method',
        choices=[('PCA', 'PCA')],
        validators=[DataRequired()],
        render_kw={"class": "form-check-input"}
    )
    submit = SubmitField('Analyse', render_kw={"class": "btn btn-primary"})

class AdmixtureAnalysisForm(FlaskForm):
    populations = SelectMultipleField(
        'Select Populations',
        choices=population_choices,
        validators=[DataRequired()],
        render_kw={"class": "form-control select2-multiple", "multiple": "multiple"}
    )
    superpopulations = SelectMultipleField(
        'Select Superpopulations',
        choices=superpopulation_choices,
        validators=[Optional()],
        render_kw={"class": "form-control select2-multiple", "multiple": "multiple"}
    )
    num_ancestral_pops = IntegerField(
        'Number of Ancestral Populations (K)',
        validators=[DataRequired(), NumberRange(min=1, max=10, message='Must be between 1 and 10')],
        render_kw={"class": "form-control"}
    )
    submit = SubmitField('Run Admixture Analysis', render_kw={"class": "btn btn-primary"})

class SNPSearchForm(FlaskForm):
    search_option = RadioField(
        'Search By',
        choices=[
            ('snp_id', 'SNP IDs'),
            ('gene_name', 'Gene Names')
        ],
        default='snp_id',
        validators=[DataRequired()],
        render_kw={"class": "form-check-input"}
    )
    snp_ids = StringField('SNP IDs', validators=[Optional()])
    gene_names = StringField('Gene Names', validators=[Optional()])
    populations = SelectMultipleField(
        'Select Populations',
        choices=population_choices,
        validators=[Optional()],
        render_kw={"class": "form-control", "multiple": "multiple"}
    )
    superpopulations = SelectMultipleField(
        'Select Superpopulations',
        choices=superpopulation_choices,
        validators=[Optional()],
        render_kw={"class": "form-control", "multiple": "multiple"}
    )

    submit = SubmitField('Search', render_kw={"class": "btn btn-primary"})

