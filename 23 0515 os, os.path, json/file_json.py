import json

# create dictionary

inventory = {}

while 1:
    # display available items
    items = sorted(list(inventory.keys()))
    print("\nItems: " + ", ".join(items))
    
    item = input("\nEnter name of the tool: ").strip()
    
    # if the user enters an empty string
    # end the while loop
    if not item: # same as [item == ""]
        break
    
    count = int(input(f" - How many {item}/s available? "))
    
    # add the item in the inventory
    inventory[item] = count
    # inventory.update({item: count})

# proper formatting to preserve readability
formatted_json_string = json.dumps(inventory, indent=4)
"""
{
    "key": "value"
}
"""

# modes of opening a file:
# r     - read
# r+    - create file, if not existing (ready for reading)
# w     - write
# w+    - create file, if not exisiting (reading & writing)
# a     - append

# encoding
# ASCII Encoding (American Standard for Character Information Interchange)
#   - 127 alphabet, numbers, special characters
# UTF-8 UNICODE
#   - ASCII, emoji, CJK characters, Latin characters, Greek, etc.
# garbage text, mismatch in encoding (beware, warning!!)

with open("dataset/inventory.json", mode="w", encoding="utf-8") as file:
    # write the formatted JSON string into the file
    file.write(formatted_json_string)
    






