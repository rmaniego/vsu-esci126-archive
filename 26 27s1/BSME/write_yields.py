import json
def main():
    crop = input("What crop to add? ")    harvest = float(input(f"How many metric tons of {crop}? "))
    
    with open("yields.json", "w+") as file:
        print(json.load(file))
if __name__ == "__main__":
    main()