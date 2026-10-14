"""
Python Dictionaries
 - A data structure, or a method to store data in RAM.
 - A structured data is faster versus unorganized data.
 - Contains key-value pairs.
"""

# key   - unique and descriptive name
#       - used to store and access the desired value.
#       - format: example_name_key
# value - any data type you want to store, can be a:
#         integers, floats, boolean, string, list,
#         and even another nested dictionary.


items = { "key": "value", "another-key": "another-value" }

items["name"] = "Juan dela Cruz"

items["age"] = 22

items["height"] = 1.77

items["filipino_citizen"] = True

items["swertres"] = [2, 6, 8]

items["valid_id"] = {"umid": "123", "philhealth": "123", "passport": "123"}

print(items)

items["name"] = "John dela Cruz"
print(items)

