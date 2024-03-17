def output_to_console(text):
    """Function to output text to the console.

       Args:
           text (str): The text to be outputted.
    """
    print(text)

def output_to_file(text, filepath):
    """Function to write text to a file.

       Args:
            text (str): The text to be written to the file.
            file_path (str): The path to the file to be written.
    """
    with open(filepath, 'w') as file:
        file.write(text)
