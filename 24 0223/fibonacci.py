previous = 1
temp = 0
count = 1
next_ = 0

limit = int(input("Sequence count: "))

while count <= limit:
	temp = next_
	next_ += previous
	previous = temp
	print(previous, end=" ")
	count += 1