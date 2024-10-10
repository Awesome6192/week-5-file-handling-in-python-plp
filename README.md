```markdown
File Handling Assignment

Objective
This Python script demonstrates basic file handling operations, including creating, reading, appending, and handling errors associated with file operations.

Features
- File Creation: Creates a new text file named `my_file.txt` and writes three lines of text to it.
- File Reading: Reads the contents of `my_file.txt` and displays them on the console.
- File Appending: Opens `my_file.txt` in append mode and adds three additional lines of text to the existing content.
- Error Handling: Implements error handling using try, except, and finally blocks to manage potential file-related exceptions.

Requirements
- Python

How to Run
1. Clone the repository or download the script.
2. Open a terminal and navigate to the directory where `file_handling_assignment.py` is located.
3. Run the script using the following command:
   ```bash
   python file_handling_assignment.py
   ```

Example Output
The script will create and modify `my_file.txt` as follows:
- Initially, the content will include three lines of text.
- Upon reading, the console will display the contents of the file.
- After appending, the file will contain three additional lines.

Error Handling
The script includes error handling for common file-related issues, such as:
- `FileNotFoundError`
- `PermissionError`
