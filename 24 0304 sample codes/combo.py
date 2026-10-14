list1 = ["Spaghetti", "Sundae", "Fries", "Hotdog", "Kwek2"]
list2 = ["Spaghetti", "Sundae", "Fries", "Hotdog", "Kwek2"]

for item1 in list1:
    for item2 in list2:
        if item1 == item2:
            continue
        print(f"\n{item1} and {item2}")