import unittest
from app.io.input import input_from_file, input_from_file_pandas

class TestInputFunctions(unittest.TestCase):

    def test_input_from_file_exists(self):         # Test if the function exists
        self.assertTrue(callable(input_from_file))

    def test_input_from_file_returns_string(self):         # Test if the function returns a string
        file_text = input_from_file("/file_input.txt")
        self.assertIsInstance(file_text, str)

    def test_input_from_file_reads_file_correctly(self):         # Test if the function reads the file correctly
        expected_text = "Hello, my name is Rick!"
        file_text = input_from_file("/file_input.txt")
        self.assertEqual(file_text, expected_text)

    def test_input_from_file_pandas_exists(self):        # Test if the function exists
        self.assertTrue(callable(input_from_file_pandas))

    def test_input_from_file_pandas_returns_dataframe(self):        # Test if the function returns a DataFrame
        file_data = input_from_file_pandas("/pandas_data.csv")
        import pandas as pd
        self.assertIsInstance(file_data, pd.DataFrame)

    def test_input_from_file_pandas_reads_file_correctly(self):        # Test if the function reads the file correctly
        expected_columns = ['Country', 'Place', 'Points']
        file_data = input_from_file_pandas("/pandas_data.csv")
        self.assertListEqual(list(file_data.columns), expected_columns)

if __name__ == '__main__':
    unittest.main()
