import json
# read from JSON file
with open("yields.json") as file:
	crops = json.load(file)

print(json.dumps(crops, indent="\t"))