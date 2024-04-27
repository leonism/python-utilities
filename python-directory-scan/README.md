# 📋 File Inventory Generator Script

![screenshot](directory-scan-python.png)

## Table of Contents

- [Description](#description)
- [Best Use Case](#best-use-case)
- [Installation](#installation)
  - [Checking Python Version](#checking-python-version)
  - [Installing Dependencies](#installing-dependencies)
  - [Installation Steps](#installation-steps)
- [Usage](#usage)
- [Example](#example)

## Description

![screenshot](directory-scanner.png)
The Inventory Generator Script is a Python utility designed to generate an inventory of files in a specified folder and save it to a text file. 📁 It allows users to quickly and easily catalog the contents of a directory, making it useful for organization, documentation, and analysis purposes. 🚀

## Best Use Case

The script is particularly handy in scenarios where you need to keep track of numerous files within a directory, such as:

- **Maintaining Project Assets**: Easily catalog image, video, or document assets in a project folder.
- **Documentation**: Generate a list of files for documentation purposes, ensuring all files are accounted for.
- **File Cleanup**: Identify redundant or unnecessary files for cleanup or archiving.

## Installation

### Checking Python Version

Before installing and using the script, ensure you have Python installed on your system. To check your Python version, open a terminal or command prompt and run the following command:

```bash
python --version
```

### Installing Dependencies

The script does not require any external dependencies beyond the Python standard library.

### Installation Steps

1. **Clone the Repository**: Clone this repository to your local machine using Git:

   ```bash
   git clone https://github.com/leonism/python-utilities.git
   ```

2. **Navigate to the Directory**: Change to the directory containing the script:

   ```bash
   cd directory-scan
   ```

## Usage

To use the Inventory Generator Script:

1. **Configure Variables**: Open the script file (`directory-scan.py`) in a text editor and modify the variables as needed. Specify the folder path to scan (`folder_to_scan`), the output file path (`output_file_path`), and any exclusion patterns (`exclude_patterns`).

2. **Run the Script**: Execute the script using a Python interpreter:

   ```bash
   python inventory_generator.py
   ```

3. **View Inventory**: Once the script completes execution, the inventory will be saved to the specified output file.

## Example

Suppose you have a project folder containing various image assets (`/project/assets/images/`). You can use the Inventory Generator Script to generate an inventory of these images for documentation or reference purposes.

## Contributing

Contributions are welcome! If you have any suggestions, feature requests, or bug reports, please open an issue or submit a pull request. This documentation provides comprehensive instructions on installing and using the Inventory Generator Script, along with examples of its best use cases. If you have any questions or encounter any issues, feel free to reach out to the project maintainers or open an issue on GitHub. 🚀

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
