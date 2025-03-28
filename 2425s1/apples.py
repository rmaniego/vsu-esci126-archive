from glob import glob

images = glob("dataset/*.png")

for image in images:
    print(image)
