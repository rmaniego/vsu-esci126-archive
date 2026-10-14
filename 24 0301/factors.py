

# that will ask a number from the user
number = int(input("Enter a number: "))

# and will display its factors.
for divisor in range(1, number+1):
    # modulo operation
    remainder = number % divisor
    if remainder == 0:
        print(divisor, end=", ")