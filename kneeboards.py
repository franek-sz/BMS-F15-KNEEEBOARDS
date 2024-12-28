import os
import shutil

# Get the directory where the script is located
script_directory = os.path.dirname(os.path.abspath(__file__))

# Define the replacements
replacements = {
    "7982.dds": "1410.dds",
    "7983.dds": "1411.dds",
}

# Perform the replacements
for source, destination in replacements.items():
    source_file = os.path.join(script_directory, source)
    destination_file = os.path.join(script_directory, destination)

    # Check if the source file exists
    if os.path.exists(source_file):
        # Copy the source file to overwrite the destination
        shutil.copyfile(source_file, destination_file)
        print(f"Copied {source_file} to {destination_file}")
    else:
        print(f"Source file {source_file} does not exist.")
