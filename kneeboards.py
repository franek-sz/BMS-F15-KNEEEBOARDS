import os
import shutil

script_directory = os.path.dirname(os.path.abspath(__file__))

source_range = range(7982, 7998)
destination_range = range(1403, 1419)

for src, dest in zip(source_range, destination_range):
    source_file = os.path.join(script_directory, f"{src}.dds")
    destination_file = os.path.join(script_directory, f"{dest}.dds")

    if os.path.exists(source_file):
        shutil.copyfile(source_file, destination_file)
        print(f"Copied {source_file} to {destination_file}")
    else:
        print(f"Source file {source_file} does not exist.")
