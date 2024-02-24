from app.extensions import db

class SNP(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    snp_id = db.Column(db.String(128), unique=True, nullable=False)
    chromosome = db.Column(db.String(10), nullable=False)
    position = db.Column(db.Integer, nullable=False)
    gene_name = db.Column(db.String(128), nullable=True)
    population = db.Column(db.String(128), nullable=False)  # This assumes each SNP entry is associated with a population
    # Add other fields as necessary, like allele frequencies, genotype frequencies, etc.





