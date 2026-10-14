import os

# Current Directory where the program is running
# C:\folder\subfolder>
# all_files_and_folders = os.listdir(".")

current_working_directory = os.getcwd()
all_files_and_folders = os.listdir(current_working_directory)

print("\nAll Files (isfile()):")
for item in all_files_and_folders:
    # if the item is a file,
    # display the filename
    if os.path.isfile(item):
        print(f" - {item}")


print("\nAll Folders (isdir()):")
for item in all_files_and_folders:
    # if the item is a directory,
    # display the folder name
    if os.path.isdir(item):
        print(f" - {item}")