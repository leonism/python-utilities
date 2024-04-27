# Task Scheduler 🕒

![screenshot](task-scheduler-python.png)

## Table of Contents

1. [Description](#description)
2. [Best Use Case](#best-use-case)
3. [Installation](#installation)
   - [Installing Python](#installing-python)
   - [Installation Steps on](#installation-steps-on)
     - [Windows](#windows)
     - [MacOSX](#macosx)
     - [Linux](#linux)
   - [Installing Dependencies](#installing-dependencies)
   - [Installation Steps on](#installation-steps-on)
     - [Windows](#windows-1)
     - [MacOSX](#macosx-1)
     - [Linux](#linux-1)
4. [Usage](#usage)
5. [Example](#example)
6. [Contributing](#contributing)
7. [License](#license)

## Description

The Task Scheduler is a Python script designed to automate and schedule repetitive tasks such as backups, file transfers, or data synchronization between different devices or cloud services.

## Best Use Case

- Automating daily backups of important files.
- Scheduling regular transfers of files between devices.
- Syncing data between local storage and cloud services on a recurring basis.

## Installation

### Installing Python

Make sure you have Python installed on your system. You can download and install Python from the [official Python website](https://www.python.org/).

### Installation Steps on

#### Windows

- Download the Python installer for Windows from the [official Python website](https://www.python.org/downloads/).
- Run the installer and follow the on-screen instructions to install Python.
- Make sure to check the option to add Python to PATH during installation.

#### MacOSX

- MacOSX usually comes with Python pre-installed. Open the Terminal and type `python --version` to check if Python is installed.
- If Python is not installed, you can download and install it from the [official Python website](https://www.python.org/downloads/).

#### Linux

- Most Linux distributions come with Python pre-installed. You can check if Python is installed by opening a terminal and typing `python --version`.
- If Python is not installed, you can install it using your package manager. For example, on Ubuntu, you can use `sudo apt-get install python3`.

### Installing Dependencies

The Task Scheduler script requires the `schedule` and `colorama` modules. You can install them using pip:

```bash
pip install schedule colorama
```

### Installation Steps on

#### Windows

- Open Command Prompt or PowerShell.
- Run the following command:
  ```bash
  pip install schedule colorama
  ```

#### MacOSX

- Open Terminal.
- Run the following command:
  ```bash
  pip install schedule colorama
  ```
- If the previous command line threw you an error, you might want to try to the following command instead :
  ```bash
  python3 -m pip install schedule colorama
  ```

#### Linux

- Open Terminal.
- Run the following command:
  ```bash
  pip install schedule colorama
  ```

## Usage

1. Clone or download the Task Scheduler script from this repository.
2. Open a terminal or command prompt.
3. Navigate to the directory where the script is located.
4. Run the script using Python:
   ```bash
   python task-scheduler.py
   ```
5. Run the script using Python3:
   ```bash
   python3 task-scheduler.py
   ```

## Example

Here's an example of how to use the Task Scheduler script:

```bash
python task-scheduler.py
```

or

```bash
python3 task-scheduler.py
```

## Contributing

Contributions are welcome! Feel free to submit pull requests or open issues if you have any suggestions or improvements.

## License

This project is licensed under the [MIT License](LICENSE).
