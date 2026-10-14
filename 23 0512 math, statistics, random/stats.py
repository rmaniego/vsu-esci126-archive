import statistics

grades = [92.1, 93.4, 99.5, 95.7, 91.0, 87.4, 75.8, 87.4, 82.3]

# simple way
average = sum(grades) / len(grades)
middle_value = sorted(grades)[len(grades)//2]

max_occurence = 1
common_value = middle_value
for g in list(set(grades)):
    o = grades.count(g)
    if o > max_occurence:
        common_value = g
        max_occurence = o

print(grades)
print(sorted(grades))

print(f"Average: {average}")
print(f"Middle value: {middle_value}")
print(f"Common value: {common_value}")

# use statistics package/module
mean = statistics.mean(grades)
median = statistics.median(grades)
mode = statistics.mode(grades)

print(f"Average: {mean}")
print(f"Middle value: {median}")
print(f"Common value: {mode}")