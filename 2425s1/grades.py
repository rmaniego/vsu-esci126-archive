import json


def main():

    # read from JSON file
    with open("yields.json") as file:
        grades = json.load(file)

    print(json.dumps(grades, indent=4))


if "__name__" == "main":
    main()
