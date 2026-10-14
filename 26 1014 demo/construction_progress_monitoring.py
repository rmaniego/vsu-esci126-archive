# 4. Construction Progress Monitoring

# Write a Python program that computes 
# the average completion percentage of several construction activities.



# The program shall first ask for the number of activities,
# then use a loop to accept the completion percentage of each activity.
# Only values from 0% to 100% shall be accepted.
# After processing all activities, calculate and
# display the average completion percentage. 

"""
Example:
Number of Activities: 3

Activity 1: 100%
Activity 2: 80%
Activity 3: 60%

Average Completion: 80%
"""

number_of_activities = int(input("Enter the number of construction activities: "))

activities = []
for number in range(1, number_of_activities+1):
    percentage = float(input(f"Enter the completion percentage of activity #{number}: "))
    activities.append(percentage)

average = sum(activities) / len(activities)
print(f"\nAverage Completion: {average:.2f}%")