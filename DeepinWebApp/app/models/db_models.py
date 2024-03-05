from .database import db

class AnalysisResults(db.Model):
    __tablename__ = 'AnalysisResults'  
    id = db.Column(db.Integer, primary_key=True)  
    SAMPLE_ID = db.Column(db.String(120))
    POP = db.Column(db.String(120))
    SUPER_POP = db.Column(db.String(120))
    PCA1 = db.Column(db.Float)
    PCA2 = db.Column(db.Float)

    @staticmethod
    def get_results_for_clustering(selected_populations):
        try:
            results = AnalysisResults.query.filter(AnalysisResults.POP.in_(selected_populations)).all()
            return results
        except Exception as e:
            print("Error retrieving clustering results:", e)
            return []


class SampleTable(db.Model):
    __tablename__ = 'SampleTable'
    SAMPLE_ID = db.Column(db.String(255), primary_key=True)
    POP = db.Column(db.String(50))
    SUPER_POP = db.Column(db.String(50))
