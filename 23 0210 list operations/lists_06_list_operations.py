# 6. List Operations

# Multiplication or "Duplication"
# numbers = [[0, 0, 0]] * 10
# print(f"\n{numbers = }")


# not in-place
# Concatenation ==> Extend
# Concatenating two Lists into one
list1 = [1, 2, 3, 4, 5]
print(f"\n{list1 = }")

list2 = [6, 7, 8, 9, 0]
print(f"\n{list2 = }")

# not in-place
list3 = list1 + list2
print(f"\n{list3 = }")

# in-place, list1 is already changed
list1.extend(list2)
print(f"\n{list1 = }")