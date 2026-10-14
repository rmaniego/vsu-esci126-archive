"""
Python Dictionaries
 - A data structure, or a method to store data in RAM.
 - A structured data is faster versus unorganized data.
 - The data supplied in
 - Contains key-value pairs.
"""

# key   - unique and descriptive name
#       - used to store and access the desired value.
# value - any data type you want to store, can be a:
#         integers, floats, boolean, string, list,
#         and even another nested dictionary.


items = {}

## 1st method: variable[key] = value
## 2nd method: variable.update({ "key": "value" })

items.update({"name": "Juan dela Cruz"})
items.update({"age": 22})
items.update({"height": 1.77})
items.update({"filipino_citizen": True})
items.update({"swertres": [2, 6, 8]})
items.update({"valid_id": {"umid": "123", "philhealth": "123", "passport": "123"}})
print(items)

items.update({"name": "John dela Cruz"})
print(items)
