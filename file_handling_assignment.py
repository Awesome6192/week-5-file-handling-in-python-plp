def create_file():
    """Create a new file and write some initial content."""
    try:
        with open("my_file.txt", 'w') as file:
            file.write("Hello, this is my first line.\n")
            file.write("Here is the second line with a number: 42.\n")
            file.write("And this is the third line.\n")
        print("File created and initial content written successfully.")
    except Exception as e:
        print(f"An error occurred while creating the file: {e}")

def read_file():
    """Read and display the contents of the file."""
    try:
        with open("my_file.txt", 'r') as file:
            contents = file.read()
            print("Contents of my_file.txt:")
            print(contents)
    except FileNotFoundError:
        print("Error: The file does not exist.")
    except PermissionError:
        print("Error: You do not have permission to read this file.")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")

def append_to_file():
    """Append additional lines to the file."""
    try:
        with open("my_file.txt", 'a') as file:
            file.write("This is the fourth line added later.\n")
            file.write("Here comes the fifth line!\n")
            file.write("Finally, this is the sixth line.\n")
        print("Additional lines appended successfully.")
    except FileNotFoundError:
        print("Error: The file does not exist.")
    except PermissionError:
        print("Error: You do not have permission to append to this file.")
    except Exception as e:
        print(f"An error occurred while appending to the file: {e}")

def main():
    """Main function to execute the tasks."""
    create_file()
    read_file()
    append_to_file()
    read_file()

# Call the main function to execute the script
if __name__ == "__main__":
    main()
