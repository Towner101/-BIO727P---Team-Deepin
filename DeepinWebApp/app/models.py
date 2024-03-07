from flask_sqlalchemy import SQLAlchemy
from app import db

class SampleTable(db.Model):
    __tablename__ = 'sample_table'
    SAMPLE_ID = db.Column(db.Text, primary_key=True)
    POP = db.Column(db.Text, primary_key=True)
    SUPER_POP = db.Column(db.Text, primary_key=True)

class FinalAnalysisResults(db.Model):
    __tablename__ = 'final_analysis_results'
    SAMPLE_ID = db.Column(db.Text, db.ForeignKey('sample_table.SAMPLE_ID'), primary_key=True)
    Ancestry1 = db.Column(db.Float)
    Ancestry2 = db.Column(db.Float)
    Ancestry3 = db.Column(db.Float)
    Ancestry4 = db.Column(db.Float)
    Ancestry5 = db.Column(db.Float)
    PCA1 = db.Column(db.Float)
    PCA2 = db.Column(db.Float)

