# 📋 Clipboard Manager Utility Script

![screenshot](clipboard-manager-python.png)

## Table of Contents

- [Description](#description)
- [Best Use Case](#best-use-case)
- [Requirements](#requirements)
  - [Checking Python Version](#checking-python-version)
    - [Installing Python (Windows)](#installing-python-windows)
    - [Installing Python (macOS)](#installing-python-macos)
    - [Installing Python (Linux)](#installing-python-linux)
  - [Installing pip](#installing-pip)
    - [Installing pip (Windows)](#installing-pip-windows)
    - [Installing pip (macOS & Linux)](#installing-pip-macos--linux)
  - [Installing Dependencies](#installing-dependencies)
- [Installing and Using the Script](#installing-and-using-the-script)
- [Contributing](#contributing)
- [License](#license)

## Description

Welcome to the Clipboard Manager utility script! 🎉 Have you ever copied something important, only to accidentally overwrite it with another copy? Say goodbye to those frustrating moments with our Python-based Clipboard Manager script! 🚀 This handy tool is designed to help you effortlessly manage and organize everything you've copied. Whether it's a snippet of code, an important link, or just a piece of text, our Clipboard Manager securely stores your clipboard history, allowing you to easily retrieve any previously copied content with just a few clicks.

No more losing track of valuable information or struggling to remember what you copied earlier. With our Clipboard Manager, everything you've copied is just a glance away, ensuring seamless productivity and peace of mind in your daily workflow. Get ready to take control of your clipboard like never before.

## Best Use Case

The script is particularly handy in scenarios where you need to keep track of numerous files within a directory, such as:

- **Maintaining Project Assets**: Easily catalog image, video, or document assets in a project folder.
- **Documentation**: Generate a list of files for documentation purposes, ensuring all files are accounted for.
- **File Cleanup**: Identify redundant or unnecessary files for cleanup or archiving.

## Requirements

Before getting started, ensure you have the following:

- **Python 3.x**: If you're not sure if Python is installed, don't worry! We'll show you how to check and install it.
- **pip**: This is a package manager for Python. We'll guide you through installing it if needed.

### Checking Python Version

Let's first check if Python is installed on your computer and what version you have. Open your terminal or command prompt and type:

```bash
python --version
```

If you see a version number starting with `3.x`, you're good to go! If not, follow the instructions below to install Python for your operating system.

#### Installing Python (Windows)

1. **Download Python**: Go to the [official Python website](https://www.python.org/downloads/) and download the latest version of Python for Windows.
2. **Run Installer**: Run the downloaded installer and follow the on-screen instructions. Make sure to check the box that says "Add Python to PATH" during installation.
3. **Verify Installation**: After installation, open a new Command Prompt window and run `python --version` again to verify that Python is installed correctly.

#### Installing Python (macOS)

1. **Installation via Homebrew (recommended)**:
   ```bash
   brew install python
   ```

#### Installing Python (Linux)

1. **Installation via apt (Ubuntu/Debian)**:
   ```bash
   sudo apt update
   sudo apt install python3
   ```

### Installing pip

If you don't already have pip installed, follow these instructions to install it:

#### Installing pip (Windows)

1. **Download get-pip.py**: Download the [get-pip.py](https://bootstrap.pypa.io/get-pip.py) script.
2. **Run Script**: Open Command Prompt and navigate to the directory containing `get-pip.py`, then run:
   ```bash
   python get-pip.py
   ```

#### Installing pip (macOS & Linux)

Pip usually comes pre-installed with Python on macOS and most Linux distributions. To ensure pip is up to date, run:

```bash
python -m pip install --upgrade pip
```

If the previous command line threw you an error, you might want to try to the following command instead :

```bash
python3 -m pip install --upgrade pip
```

### Installing Dependencies

Now that we have Python and pip set up, let's install the `pyperclip` library:

```bash
pip install pyperclip
```

If the previous command line threw you an error, you might want to try to the following command instead :

```bash
python3 -m pip install pyperclip
```

Now you're all set to use the Clipboard Manager utility script!

## Installing and Using the Script

Follow these simple steps to install and use the Clipboard Manager:

1. **Clone the Repository**: Open your terminal or command prompt and navigate to the directory where you want to clone the repository. Then, run the following command:

```bash
git clone https://github.com/leonism/python-utilities.git
```

2. **Navigate to the Directory**: Change into the directory of the cloned repository:

```bash
cd python-utilities/clipboard-manager
```

3. **Run the Script**: Execute the script using Python:

```bash
python clipboard-manager.py
```

If the previous command line threw you an error, you might want to try to the following command instead :

```bash
python3 clipboard-manager.py
```

4. **Interact with the Script**: Follow the on-screen instructions to interact with the Clipboard Manager utility. You can print, search, and clear clipboard history as needed.

5. **Exiting the Script**: To exit the Clipboard Manager, simply press `Ctrl + C` in your terminal or command prompt.

That's it! You're now ready to manage your clipboard like a pro with the Clipboard Manager utility script. Happy copying! 📋✨

## Contributing

Contributions are welcome! If you encounter any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
