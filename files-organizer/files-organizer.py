import os
import shutil
import time  # Import the time module

# Check if pip is installed
def check_pip():
    for pip_cmd in ["pip", "pip3"]:
        try:
            result = os.system(f"{pip_cmd} --version")
            if result == 0:
                return pip_cmd
        except OSError:
            continue
    return None

# Check for colorama dependency and install if not found
def check_and_install_colorama():
    pip_cmd = check_pip()
    if pip_cmd is not None:
        print("Pip found. Checking for colorama...")
        os.system(f"{pip_cmd} show colorama")
        result = os.system(f"{pip_cmd} show colorama")
        if result != 0:
            print("Colorama module not found. Installing...")
            os.system(f"{pip_cmd} install colorama")
    else:
        print("Pip not found. Please install pip first.")

check_and_install_colorama()

# Import colorama after installation
try:
    from colorama import Fore, Style  # Import colorama for colored fonts
except ImportError:
    print("Colorama not installed. Please install it manually.")

# If colorama is not found, exit the script
if 'Fore' not in globals():
    exit()

# Function to get user input for directory and sorting criteria
def get_user_input():
    print(f"{Fore.CYAN}Welcome to the File Organizer!{Style.RESET_ALL}")
    directory = input(f"{Fore.YELLOW}Enter the path of the directory you want to organize (or type 'cancel' to exit): {Style.RESET_ALL}")
    
    # Check if user wants to cancel
    if directory.lower() == 'cancel':
        print("Action canceled.")
        return None, None
    
    while not os.path.isdir(directory):
        print(f"{Fore.RED}Error: Invalid directory path.{Style.RESET_ALL}")
        directory = input(f"{Fore.YELLOW}Enter a valid directory path (or type 'cancel' to exit): {Style.RESET_ALL}")
        
        # Check if user wants to cancel
        if directory.lower() == 'cancel':
            print("Action canceled.")
            return None, None
    
    print("\nSelect sorting criteria:")
    print(f"{Fore.GREEN}1. File Extension")
    print("2. Date")
    print("3. Cancel")
    criteria = input("Enter the number corresponding to your choice: ")
    
    # Check if user wants to cancel
    if criteria == '3':
        print("Action canceled.")
        return None, None
    
    while criteria not in ["1", "2"]:
        print(f"{Fore.RED}Error: Invalid input.{Style.RESET_ALL}")
        criteria = input("Enter the number corresponding to your choice: ")
        
        # Check if user wants to cancel
        if criteria == '3':
            print("Action canceled.")
            return None, None

    return directory, criteria

# Function to organize files based on file extension
def organize_by_extension(directory):
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    for file in files:
        file_extension = os.path.splitext(file)[1]
        if file_extension:
            folder_path = os.path.join(directory, file_extension[1:].upper())
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
            shutil.move(os.path.join(directory, file), folder_path)

# Function to organize files based on modification date
def organize_by_date(directory):
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    for file in files:
        file_path = os.path.join(directory, file)
        modification_time = os.path.getmtime(file_path)
        
        # Get the year and month from the modification time
        year = str(time.localtime(modification_time).tm_year)
        month = str(time.localtime(modification_time).tm_mon)
        
        folder_path = os.path.join(directory, year, month)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        shutil.move(file_path, folder_path)

# Main function to orchestrate the overall flow
def main():
    directory, criteria = get_user_input()
    
    # Check if user canceled the action
    if directory is None:
        return

    if criteria == "1":
        organize_by_extension(directory)
    elif criteria == "2":
        organize_by_date(directory)

    print(f"{Fore.GREEN}Files organized successfully!{Style.RESET_ALL}")

# Entry point of the script
if __name__ == "__main__":
    main()
