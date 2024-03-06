import unittest
from app import create_app
from app import db

class ClusteringDataTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')  # Pass in a testing config if you have one
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client(use_cookies=True)
        # If your database requires it, set up the database here

    def tearDown(self):
        db.session.remove()
        self.app_context.pop()

    def test_clustering_data(self):
        # Test for success
        response = self.client.get('/clustering/data?populations=AFR,AMR')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('application/json' in response.content_type)
        
        # Test for edge case: No populations specified
        response = self.client.get('/clustering/data')
        self.assertEqual(response.status_code, 400)  # Assuming you return a 400 error for this case

        # Add more tests as needed for other scenarios and edge cases

if __name__ == '__main__':
    unittest.main()
