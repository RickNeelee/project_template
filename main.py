from app.io.input import input_from_console, input_from_file, input_from_file_pandas
from app.io.output import output_to_console, output_to_file

def main():
    #Input from console
    console_text = input_from_console()
    output_to_console(console_text)
    output_to_file(console_text, "data/console_output.txt")

    #Input from file
    file_text = input_from_file("data/file_input.txt")
    output_to_console(file_text)
    output_to_file(file_text, "data/file_output.txt")

    # Input from file using pandas
    file_pandas_data = input_from_file_pandas("data/pandas_data.csv")
    output_to_console(str(file_pandas_data))
    file_pandas_data.to_csv("data/file_pandas_input.csv", index=False)

if __name__ == "__main__":
    main()
