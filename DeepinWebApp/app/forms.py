from flask_wtf import FlaskForm
from wtforms import StringField, SelectMultipleField, RadioField, SubmitField, IntegerField, SelectField, BooleanField
from wtforms.validators import DataRequired, NumberRange, Optional

# Define the populations grouped by superpopulations
superpopulation_populations = {
    'AFR': ['ACB', 'ASW', 'ESN', 'GWD', 'LWK', 'MSL', 'YRI'],
    'AMR': ['CLM', 'MXL', 'PEL', 'PUR'],
    'EAS': ['CDX', 'CHB', 'CHS', 'JPT', 'KHV'],
    'EUR': ['SIB','CEU', 'FIN', 'GBR', 'IBS', 'TSI'],
    'SAS': ['BEB', 'GIH', 'ITU', 'PJL', 'STU']
}

# Convert the grouped populations to a flat list for use with WTForms choices
population_choices = [
    (f"{superpop}_{pop}", pop) for superpop, pops in superpopulation_populations.items() for pop in pops
]

superpopulation_choices = [
    ('AFR', 'Africa'), ('AMR', 'America'), 
    ('EAS', 'East Asian'), ('EUR', 'European'), 
    ('SAS', 'South Asian')
]

class BaseForm(FlaskForm):
    # This method organizes populations by superpopulation for template rendering
    def populations_by_superpopulation(self):
        organized = {code: [] for code, _ in superpopulation_choices}
        for superpop, pops in superpopulation_populations.items():
            organized[superpop] = [(f"{superpop}_{pop}", pop) for pop in pops]
        return organized

class ClusteringAnalysisForm(BaseForm):
    populations = SelectMultipleField(
        'Select Populations',
        choices=population_choices,
        validators=[DataRequired()],
        render_kw={"class": "form-control select2-multiple", "multiple": "multiple", "style": "height: auto; overflow-y: scroll;"}
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

class AdmixtureAnalysisForm(BaseForm):
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
        validators=[DataRequired(), NumberRange(min=1, max=10)],
        render_kw={"class": "form-control"}
    )
    submit = SubmitField('Run Admixture Analysis', render_kw={"class": "btn btn-primary"})

class SNPSearchForm(BaseForm):
    search_option = RadioField(
        'Search By',
        choices=[
            ('snp_id', 'SNP IDs'),
            ('gene_name', 'Gene Names'),
            ('chromosome_position', 'Chromosome Position')
        ],
        default='snp_id',
        validators=[DataRequired()],
        render_kw={"class": "form-check-input"}
    )
    snp_ids = StringField('SNP IDs', validators=[Optional()])
    gene_names = StringField('Gene Names', validators=[Optional()])
    chromosome = SelectField(
        'Chromosome',
        choices=[('1', '1')],  # Expand as necessary
        validators=[Optional()],
        render_kw={"class": "form-control"}
    )
    position = StringField('Position', validators=[Optional()], render_kw={"class": "form-control"})
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
