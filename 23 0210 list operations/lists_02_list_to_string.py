# 2. Basic Initialization

"""
 * There is no limit of the number of contents of the list,
 * But an actual limit would be your computer RAM.

 * Larger lists will consume a larger space at run-time
 * Larger lists will potentially slow down your PC, or even cause a hang.
 * There are methods to handle large lists, but will be on a different topic.
"""

# converts a string into a list of individual characters
message = "Hello, world!" # immutable
print(f"\n{message = }")
# message = message.replace("Hello", "Help")
# print(f"\n{new_message = }")


# list is not immutable, can be changed at run-time
# convert string to list
letters = list(message)
print(f"\n{letters = }")

# replace the 
letters[5] = "p"
print(f"\n{letters = }")