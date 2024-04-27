import os

# Define variables for the script
output_file_path = "/assets/img/inventory.txt"  # Path to save the inventory results
folder_to_scan = "/assets/img/"  # Path of the folder to scan for files
exclude_patterns = ['Thumbs.db', '.tmp', '.css', '.html', '.md', '.js', '.DS_Store']  # Patterns to exclude from inventory

def generate_inventory(folder_path, output_path, exclusion_list):
    """
    Generate an inventory of files in the specified folder and save it to a text file.

    Args:
        folder_path (str): The path of the folder to be scanned.
        output_path (str): The path of the output file to save the inventory.
        exclusion_list (list): A list of strings representing file names or patterns to be excluded.

    Returns:
        None
    """
    with open(output_path, "w") as output_file:
        # Iterate through the directory tree starting from the specified folder
        for root, _, files in os.walk(folder_path):
            # Create a separator line to denote the current directory being scanned
            separator = f"\n---------- {root} ----------"
            print(separator)
            # Write the separator line to the output file
            output_file.write(f"{separator}\n")

            # Iterate through the files in the current directory
            for filename in sorted(files):
                # Check if the file matches any of the exclusion patterns
                if not any(exclude_pattern in filename for exclude_pattern in exclusion_list):
                    # Construct the full path of the file
                    file_path = os.path.join(root, filename)
                    # Print the file path to the console
                    print(file_path)
                    # Write the file path to the output file
                    output_file.write(f"{file_path}\n")

# Call the function to generate the inventory
generate_inventory(folder_to_scan, output_file_path, exclude_patterns)
