names_of_crops = list()

names_of_crops.append("rice")
names_of_crops.append("corn")
names_of_crops.append("coconut")
names_of_crops.append("banana")
names_of_crops.append("cacao")
print(names_of_crops)

"""

names_of_crops.insert(3, "sweet potato")

print(names_of_crops)

crop = names_of_crops.pop(4)
print(names_of_crops)
print(f"Deleted '{crop}' crop.\n")

crop = names_of_crops.pop(3)
print(names_of_crops)
print(f"Deleted '{crop}' crop.\n")

crop = names_of_crops.pop(2)
print(names_of_crops)
print(f"Deleted '{crop}' crop.\n")

crop = names_of_crops.pop(2)
print(names_of_crops)
print(f"Deleted '{crop}' crop.\n")

names_of_crops.append("corn")
names_of_crops.append("corn")
names_of_crops.append("corn")
names_of_crops.append("corn")
print(names_of_crops)

crop_to_remove = "corn"
names_of_crops.remove(crop_to_remove)
print(names_of_crops)
print(f"Deleted '{crop_to_remove}' crop.\n")

counter = names_of_crops.count("corn")
print(f"Number of corn: '{counter}'\n")

counter = names_of_crops.count("strawberry")
print(f"Number of strawberry: '{counter}'\n")

index = names_of_crops.index("rice")
print(f"Index of rice: '{index}'\n")
"""

names_of_crops.clear()
print(names_of_crops)

