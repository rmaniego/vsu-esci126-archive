keyword = "GramNegativeFacultativeAnaerobicRodShapedColiformBacterium"
for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    if letter not in keyword:
        continue
    keyword = keyword.replace(letter, f"_{letter}")
print(keyword[1:].lower())