import os

# filename.extension
# -------------------------------------------------
# image.jpg - Joint-Photographic Group (Standard, Lossy)
# image.png - Portable Network Graphics (Transaparent Pixels)
# image.gif - Graphics Interchage Format (Animated)
# image.svg - Scalable Vector Graphics (Art, Graphics)
# image.webp - Alternative to PNG/JPG
# powerpoint.pptx
# slides.pdf
# -------------------------------------------------
# file.txt
# file.csv
# file.json

subfolder = "dataset/"

print(f"\nFolder: {subfolder}")

# whitelist of file types
allowed_extensions = ["jpg"] # , "png", "gif"]
print("\nAllowed Extensions: ", allowed_extensions)

print("\nPictures:")
all_files_and_folders = os.listdir(subfolder)
for item in all_files_and_folders:
    # print(item, os.path.isfile(item))
    # if not os.path.isfile(item):
    #    continue

    # <filename>.v1.20230515.<extension>
    #      0      1     2         3
    #     -4     -3    -2        -1
    # split the full filename by the periods
    # get the last item in the list
    extension = item.split(".")[-1]
    if extension in allowed_extensions:
        print(f" - {item}")




