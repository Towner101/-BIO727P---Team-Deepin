from flask import Flask, render_template, url_for

#create a flask application object 
app = Flask(__name__)

#define the action for the top level route
@app.route('/')
def test5():
    return render_template('test5.html')

@app.route('/About_us')
def About_us():
    return render_template('About_us.html')

@app.route('/Data_analysis')
def Data_analysis():
    return render_template('Data_analysis.html')

@app.route('/SNP_Search')
def SNP_Search():
    return render_template('SNP_Search.html')

@app.route('/Clustering_analysis.html')
def Clustering_analysis():
    return render_template('Clustering_analysis.html')

#start the web server 
if __name__=='__main__':
    app.run(debug=True)

#start the web server 
if __name__=='__main__':
    app.run(debug=True)
