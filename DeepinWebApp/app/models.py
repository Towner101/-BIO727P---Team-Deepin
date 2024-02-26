from app.extensions import db

class SNP(db.Model):
    __tablename__ = 'snps'  # Replace 'snps' with your actual table name
    id = db.Column(db.Integer, primary_key=True)
    snp_id = db.Column(db.String(128), unique=True)
    chromosome = db.Column(db.String(10))
    position = db.Column(db.Integer)
    gene_name = db.Column(db.String(128))

    def __repr__(self):
        return '<SNP {}>'.format(self.snp_id)






