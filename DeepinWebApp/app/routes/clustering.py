from flask import Blueprint, request, jsonify, current_app
from sqlalchemy import text
from app.database import db  # Make sure 'db' is correctly imported from your database setup module

clustering = Blueprint('clustering', __name__)

@clustering.route('/clustering/data', methods=['GET'])
def get_clustering_data():
    # Fetch populations from query parameters and split into a list
    selected_populations = request.args.get('populations', '').split(',')

    try:
        current_app.logger.debug("Fetching clustering analysis data.")

        # Ensure we have valid population selections before querying
        if selected_populations and selected_populations != ['']:
            # Prepare SQL query, placeholders for SQLite are represented as '?'
            placeholders = ",".join(["?"] * len(selected_populations))
            # Using the correct table and column names as per your database schema
            sql_query = text(f"SELECT SAMPLE_ID, POP, SUPER_POP, PCA1, PCA2 FROM Analysis_Results WHERE POP IN ({placeholders})")

            # Execute raw SQL query
            result = db.engine.execute(sql_query, selected_populations)

            # Fetch results
            analysis_results = result.fetchall()

            current_app.logger.info(f"Number of analysis results retrieved for populations {selected_populations}: {len(analysis_results)}")

            if analysis_results:
                # Convert analysis results to JSON-compatible format
                data = [{
                    'SAMPLE_ID': row[0],
                    'POP': row[1],
                    'SUPER_POP': row[2],
                    'PCA1': float(row[3]),
                    'PCA2': float(row[4])
                } for row in analysis_results]

                return jsonify(data)
            else:
                return jsonify({'message': 'No data found for the selected populations'}), 404
        else:
            # No valid populations specified in the request
            return jsonify({'message': 'No populations specified'}), 400

    except Exception as e:
        current_app.logger.error(f"Error fetching clustering data: {e}", exc_info=True)
        return jsonify({'message': 'An error occurred fetching clustering data.'}), 500
