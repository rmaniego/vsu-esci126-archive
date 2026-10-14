import json
def main():
	# Make sure the JSON file exists.
	with open("yields.json") as file:
		harvest = json.load(file)
		print(json.dumps(harvest, indent="\t"))

if __name__ == "__main__":
	main()