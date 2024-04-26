import os

# Start editable vars
outputfile = "/Volumes/DATA/Jekyll/OptikalBahari/assets/img/inventory.txt"  # Full directory path to save the results to
folder = "/Volumes/DATA/Jekyll/OptikalBahari/assets/img/"  # Full directory path to scan
exclude_strings = ['Thumbs.db', '.tmp', '.css', '.html', '.md', '.js', '.DS_Store']  # Exclude files containing these strings
# End editable vars

def write_inventory(folder, output_file, exclude):
    """
    Write the inventory of files in a given folder to an output file, excluding specified files.

    Args:
        folder (str): The path to the folder to be scanned.
        output_file (str): The path to the output file where the inventory will be written.
        exclude (list): A list of strings representing file names or patterns to be excluded from the inventory.

    Returns:
        None
    """
    with open(output_file, "w") as txtfile:
        for path, _, files in os.walk(folder):  # Ignore the unused "dirs" variable
            sep = "\n---------- " + path + " ----------"
            print(sep)
            txtfile.write("%s\n" % sep)

            for fn in sorted(files):
                if not any(exclude_str in fn for exclude_str in exclude):
                    file_path = os.path.join(path, fn)
                    print(file_path)
                    txtfile.write("%s\n" % file_path)

# Call the function to write the inventory
write_inventory(folder, outputfile, exclude_strings)