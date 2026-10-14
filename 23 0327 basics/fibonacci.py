# Fibonacci sequence
# next number = current number + previous number

temporary = 0
count = 1
previous = 1
next_number = 0

limit = int(input("Sequence count: "))

while count <= limit:
	temporary = next_number
	next_number = next_number + previous
	previous = temporary
	print(previous, end=" ")
	count += 1