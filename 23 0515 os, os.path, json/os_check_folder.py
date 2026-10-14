import os
from datetime import datetime

# Get current working directory
# Check if sakto imohang location
current_working_directory = os.getcwd()
print(f"\nRunning in '{current_working_directory}'...")

current_date = datetime.now().strftime("%Y%m%d")
subfolders = f"{current_date}/tests"

# check if that specific directory already exists
if not os.path.exists(subfolders):
    print(f"\nCreating '{subfolders}' directory...")
    
    # operating system dot make directory
    # os.mkdir("folder_name")
    
    # operating system dot make directories
    os.makedirs(subfolders)
else:
    print(f"\nSorry, the '{subfolders}' directory already exists...")

if os.path.exists(subfolders):
    # Deletion of a single folder
    # os.remove("folder_name")
    
    # Recursive deletion of nested folders and subfolders
    print(f"\nDeleting '{subfolders}' directory...")
    # os.removedirs(subfolders)
    
    # check the deleted directory exists
    exists = os.path.exists(subfolders)
    print(f"The '{subfolders}' directory exists = {exists}.")
else:
    print("\nSorry, unable to delete non-existing directory...")