import pandas as pd
def input_from_console():
    """Function to input text from the console.

       Returns:
          str: The text inputted from the console.
    """
    return input("Enter text: ")

def input_from_file(filepath):
    """Function to read text from a file.

       Args:
          filepath (str): The path to the file to be read.

       Returns:
          str: The text read from the file.
    """
    with open(filepath, 'r') as f:
        return f.read()

def input_from_file_pandas(filepath):
    """Function to read text from a file using pandas library.

       Args:
          filepath (str): The path to the file to be read.

       Returns:
          pandas.DataFrame: The data read from the file.
    """
    return pd.read_csv(filepath)

