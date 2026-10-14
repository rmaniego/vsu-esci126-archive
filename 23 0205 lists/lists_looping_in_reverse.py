## Looping on lists using indices

## Advisable
## for item in list:

# set: {1,2,3,3,2,2,1}  # no ordering, distinct {1,2,3} or {2,3,1}
# tuple = (1,2,3)       # ordered
# list = [1,2,3]        # ordered

## Alternative
animals = ["bird", "cat", "dog",
            "giraffe", "lion", "turtle",
            "fish", "dinosaur", "crab",
            "tiger", "elephant", "cockroach",
            "cheetah", "lizard", "monkey"]

# range - generator of numbers from `x` to `y`
# if `x` is not specified, it will start with 0

# Long-hand method
# number_of_animals = len(animals)
# for index in range(0, number_of_animals):

# (Reverse) Looping on Lists using its index
# range(start, stop, step)
# count = 15, but max index = 14
for index in range(len(animals)-1, -1, -1):
    # access the item at the specified index
    animal = animals[index]
    
    # print using f-string
    print(f"{index} {animal}")


