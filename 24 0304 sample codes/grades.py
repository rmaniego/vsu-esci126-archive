grades = [92, 89, 93, 98, 79, 88, 98, 92, 89, 93, 95, 79, 88, 98, 58, 89, 93, 95, 67, 88, 98, 92, 89, 93, 95, 79, 88, 98]

count = len(grades)

print("# of Grades:", count)
print("Min. Grade:", min(grades))
print("Max. Grade:", max(grades))

total = sum(grades)

print("Sum of Grades:", total)

average = total / count

print(f"Ave. of Grades: {average:.1f}")