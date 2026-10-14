
# initialize the list
fruits = ["Apple", "Banana", "Cherry", "Durian"]

# get the number of items in the list
count = len(fruits)

# basic for-loop
for fruit in fruits:
    print(fruit)

# Using `enumerate()` function
# to loop with its equivalent index: (index, item)
for (index, fruit) in enumerate(fruits):
    print(f" - {index}: {fruit}")

# Adjusting the counter by adding 1 to the index
for (index, fruit) in enumerate(fruits):
    print(f" - {index+1}: {fruit}")

# Looping with a counter and total count
for (index, fruit) in enumerate(fruits):
    print(f" - {index+1}/{count}: {fruit}")