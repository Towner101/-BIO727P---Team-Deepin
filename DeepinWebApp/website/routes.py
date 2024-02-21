from flask import Blueprint, render_template, request
from website import app
from website.utilities.helpers import process_data  # Ensure this function is properly defined in helpers.py

routes = Blueprint('routes',__name__)

@app.route('/')
@app.route('/index')
def index():
    """Render the home page."""
    return render_template('index.html', title='Home')

@app.route('/about')
def about():
    """Render the about page."""
    return render_template('about.html', title='About Us')

@app.route('/analysis', methods=['GET', 'POST'])
def analysis():
    """Handle the analysis form; process data on POST, and show the form on GET."""
    if request.method == 'POST':
        # Extract data from the form submission
        form_data = request.form
        # Process the data and obtain results
        try:
            results = process_data(form_data)
            # Pass the results to the results template for display
            return render_template('results.html', title='Analysis Results', results=results)
        except Exception as e:
            # Handle errors in data processing
            error_message = str(e)
            return render_template('analysis.html', title='Analysis Tools', error=error_message)
    # For a GET request, just show the analysis form
    return render_template('analysis.html', title='Analysis Tools')



