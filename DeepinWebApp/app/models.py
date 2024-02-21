from flask_sqlalchemy import SQLAlchemy
from flask import Blueprint

models = Blueprint('models',__name__)

db = SQLAlchemy()

class SNP(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    chromosome = db.Column(db.Integer)
    position = db.Column(db.Integer)
    snp_id = db.Column(db.String(255))
    gene = db.Column(db.String(255))

    def __repr__(self):
        return f"SNP(id={self.id}, chromosome={self.chromosome}, position={self.position}, snp_id={self.snp_id}, gene={self.gene})"


