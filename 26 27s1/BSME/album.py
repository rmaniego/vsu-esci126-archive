from glob import glob
def main():
    # List down images found on a specific directory
    images = glob("albums/*.png")
    for filepath in images:
        print(filepath)
if __name__ == "__main__":
    main()