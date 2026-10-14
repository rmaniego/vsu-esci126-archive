# Fibonacci Sequence

next, temp, count, previous = 1, 0, 1, 0
limit = int(input("Fibonacci sequence limit: "))
while count <= limit:
    if count > 1:
        temp = next
        next += previous
        previous = temp
    print(previous)
    count += 1