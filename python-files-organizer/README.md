# File Organizer 📂🔍

![screenshot](files-organizer-python.png)

## Table of Contents

- [Description](#description)
- [Best Use Case](#best-use-case)
- [Installation](#installation)
  - [Installing Python](#installing-python)
  - [Installing Dependencies](#installing-dependencies)
- [Usage](#usage)
- [Example](#example)
- [Contributing](#contributing)
- [License](#license)

## Description

The File Organizer is a Python script that helps you keep your directories tidy and well-organized. It allows you to easily sort files within a specified directory based on criteria such as file extension or modification date.

## Best Use Case

The File Organizer is ideal for individuals or organizations looking to maintain a structured file system and improve productivity by quickly locating and accessing files.

## Installation

### Installing Python

Python is required to run the File Organizer script. Follow these steps to install Python on your system:

#### Windows

1. Visit the [Python official website](https://www.python.org/downloads/) and download the latest version of Python.
2. Run the installer and follow the installation wizard.
3. Make sure to check the box that says "Add Python to PATH" during installation.

#### MacOSX

1. MacOSX typically comes with Python pre-installed. However, you can install the latest version using [Homebrew](https://brew.sh/).
2. Download & install brew package manager, if you haven't already, once satisfied,
3. Open Terminal and run the following command:
   ```
   brew install python
   ```

#### Linux

1. Most Linux distributions come with Python pre-installed. You can install it using the package manager specific to your distribution.
2. For Debian/Ubuntu-based distributions, run:
   ```
   sudo apt-get update
   sudo apt-get install python3
   ```

### Installing Dependencies

The File Organizer script requires the Colorama library for colored text output. Follow these steps to install the dependency:

#### Windows, MacOSX, Linux

1. Make sure you have pip installed. If not, follow the steps mentioned in the Python installation section.
2. Open Terminal/Command Prompt and run the following command:
   ```
   pip install colorama
   ```
3. If the previous command line threw you an error, you might want to try to the following command instead :
   ```bash
   python3 -m pip install colorama
   ```

## Usage

To use the File Organizer script, follow these steps:

1. Open Terminal/Command Prompt.
2. Navigate to the directory containing the File Organizer script.
3. Run the script by executing the following command:
   ```
   python files-organizer.py
   ```
4. If the previous command line threw you an error, you might want to try to the following command instead :
   ```bash
   python3 files-organizer.py
   ```
5. Follow the on-screen prompts to specify the directory and sorting criteria.

## Example

Here's an example of how to use the File Organizer script:

```bash
python files-organizer.py
```

or

```bash
python3 files-organizer.py
```

## Contributing

Contributions are welcome! Feel free to fork the repository, make changes, and submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
