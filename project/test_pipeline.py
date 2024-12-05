import unittest
import os
import subprocess

class TestDataPipeline(unittest.TestCase):
    def setUp(self):
        # Run the pipeline before tests
        result = subprocess.run(['./pipeline.sh'], capture_output=True, text=True)
        self.pipeline_output = result.stdout
        self.pipeline_error = result.stderr
        self.pipeline_status = result.returncode

    def test_pipeline_execution(self):
        """Test if pipeline executes successfully"""
        self.assertEqual(self.pipeline_status, 0, 
                        f"Pipeline failed with error: {self.pipeline_error}")

    def test_output_files_exist(self):
        """Test if expected output files are created"""
        # Replace 'data.sqlite' with your actual output filename
        expected_file = os.path.join('..', 'data', 'data.sqlite')
        self.assertTrue(os.path.exists(expected_file), 
                       f"Expected output file {expected_file} not found")
        
        # Add more file existence checks as needed
        
    def test_output_file_not_empty(self):
        """Test if output files contain data"""
        # Replace 'data.sqlite' with your actual output filename
        expected_file = os.path.join('..', 'data', 'data.sqlite')
        self.assertGreater(os.path.getsize(expected_file), 0, 
                          f"Output file {expected_file} is empty")

if __name__ == '__main__':
    unittest.main() 