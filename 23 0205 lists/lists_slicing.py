## Looping on lists using indices

## Alternative
animals = ["bird", "cat", "dog",
            "giraffe", "lion", "turtle",
            "fish", "dinosaur", "crab",
            "tiger", "elephant", "cockroach",
            "cheetah", "lizard", "monkey"]

# NOTE: Counting is based on actual contents of the list.

# dinosaur: 0-based index
print(animals[7])

# dinosaur: negative index
print(animals[-8])


# bird to dog
print(animals[0:3])
print(animals[:3]) #equivalent

# fish to lizard
print(animals[6:14])


