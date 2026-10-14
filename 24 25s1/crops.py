import json


def main():

    yields = {
        "coconut": 53.7,
        "sugarcane1": 28.1,
        "sugarcane2": 28.1,
        "sugarcane3": 28.1,
        "sugarcane4": 28.1,
        "sugarcane": 28.1,
    }
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    with open("crops.json", "w+") as file:
        json.dump(yields, file, indent="\t")


if "__name__" == "main":
    main()
