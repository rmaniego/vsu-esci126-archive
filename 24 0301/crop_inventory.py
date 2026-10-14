# NOTE: Implement using a Dictionary
# 2. Ask the user three (3) crops and its corresponding scientific names,
# then display all crops information afterwards.

crops = {}

while True:
    crop_name = input("\nEnter crop name: ").strip()
    
    if crop_name == "":
        break
    
    scientific_name = input("Enter its scientific name: ").strip()
    
    if scientific_name == "":
        continue
    
    # dictionary[key] = value
    crops[crop_name] = scientific_name

print("\nCrop List")
for crop_name, scientific_name in crops.items():
    print(f" * {crop_name} ({scientific_name}) ")