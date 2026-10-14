# 1. Creating a List

# Python Method (Advisable)
# This is fast and not memory-heavy at first
# It reuses available memory recently freed up by Python
items = []

# Alternative Method
# This is a slower option as it requests a new space in the memory.
items = list()

# Ultimately, they are all the same afterwards