# Problem:  Write a Python program
# that will ask the user's favorite motto
# then slice and display the output string.

motto = input("What is your motto on life? ")

# string[start:end:step]
# string[start:end]
# string[start:]
# string[:end]

print("\nmotto:\t" + motto)
print("\nmotto[1:]:\t" + motto[1:])
print("\nmotto[5:10]:\t" + motto[5:10])
print("\nmotto[:10]:\t" + motto[:10])
print("\nmotto[:-1]:\t" + motto[:-1])
print("\nmotto[-1:]:\t" + motto[-1:])