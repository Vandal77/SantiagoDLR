import unittest
import os
from flask import current_app
from app import create_app

class MainTest(unittest.TestCase):
    
    def setUp(self):
        os.environ["FLASK_CONTEXT"] = "testing"
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        
    def tearDown(self):
        self.app_context.pop()
        
    def test_app(self):
        self.assertIsNotNone(current_app)
    
if __name__ == "__main__":
    unittest.main()