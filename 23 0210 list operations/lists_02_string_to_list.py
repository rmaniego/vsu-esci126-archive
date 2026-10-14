# 2. Basic Initialization

message = "Hello, world!"   # immutable
letters = list(message)     # mutable - can be changed
print(f"\n{letters = }")

print("".join(letters))

print("-".join(letters))

## \n - backslash-n or newline
print("\n".join(letters))

## backslash-t or tab
print("\t".join(letters))
