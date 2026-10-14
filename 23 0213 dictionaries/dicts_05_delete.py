"""
Python Dictionaries
 - A data structure, or a method to store data in RAM.
 - A structured data is faster versus unorganized data.
 - The data supplied in
 - Contains key-value pairs.
"""

pets = {"bird": "Tweety", "cat": "Tom", "dog": "Bruno"}
print(pets)

# Make sure only delete if key is in the dictionary

# 1st method
key = "bird"
del pets[key]

# 2nd method:
pets.pop("dog")

print(pets)
