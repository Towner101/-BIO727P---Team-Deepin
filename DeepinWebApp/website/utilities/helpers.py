import os
import pandas as pd

def process_data():
    """Read and process data from a file within the Flask application."""
    # Construct the path to the file relative to the project root
    data_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'samplevcf.csv')
    
    # Read the CSV file using pandas (make sure pandas is installed)
    try:
        data = pd.read_csv(data_file)
        # Process the data as needed
        # For example, summarize, analyze, or simply prepare it for display
        results = data.describe()  # This is a placeholder for actual data processing
        return results.to_html()  # Convert results to HTML for easy display in the template
    except Exception as e:
        return f"Error processing data: {str(e)}"
