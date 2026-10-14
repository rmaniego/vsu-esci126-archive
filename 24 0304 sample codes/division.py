# imagine this is a data from the internet
numbers = [
    [0, 3, 7, 4],
    [5, 3, 5, 8],
    [],
    [4]
]

for values in numbers:
    if len(values) == 0:
        continue # skip to the next value

    average = sum(values) / len(values)
    print(average)
