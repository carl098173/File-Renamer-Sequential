# File Renamer Sequential

A simple GUI application to copy and rename all files in a directory to a number sequence, starting with 0000000000.jpg and ending with 9999999999.jpg. The sequence continues from the highest file number if files already exist in the output directory.

## Features

- Select input and output directories through a GUI.
- Copy and rename files in the input directory to a 10-digit sequence in the output directory.
- Ensure no files are overwritten by continuing the sequence from the highest existing number.
- Console log with a scroll bar and line count to show the status of file processing.
- Dynamic resizing of the console log window.
- Only copies and renames files according to file extension.

## Requirements

- Python 3.x

## Installation

No additional packages are required as the script uses the standard Python library.

## Usage

1. Clone the repository or download the `file_renamer.py` script.

    ```bash
    git clone https://github.com/yourusername/file-renamer.git
    cd file-renamer
    ```

2. Run the script.

    ```bash
    python file_renamer.py
    ```

3. Use the GUI to select the input and output directories.

4. Click "Process Files" to start copying and renaming the files.

## Example

- Select an input directory containing files to rename.
- Select an output directory where the renamed files will be saved.
- The console log will display the processing status and completion message.

## Contributing

Feel free to fork this repository and submit pull requests. Any contributions, suggestions, or improvements are welcome.

## License

This project is licensed under the MIT License.
