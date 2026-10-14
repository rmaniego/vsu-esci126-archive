def main():
    toolbox = {
        "Screw": 5,
        "Hammer": 1,
        "bolpin": 2,
        "t-square": 1,
        "calcu": 1,
        "brain cells": 6
    }
    
    print("###########################")
    print("# My Toolbox              #")
    print("# Owned by: Elmer's Glue  #")
    print("###########################")
    for item, count in toolbox.items():
        print(f" * {item} x{count}")
if __name__ == "__main__":
    main()