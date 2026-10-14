

def main():
    grades = [92, 89, 93, 95, 79, 88, 98]
    print(min(grades))
    print(max(grades))
    
    total = sum(grades)
    count = len(grades)

    average = total / count
    
    print(f"Your average grade is {average:.2f}.")

if __name__ == "__main__":
    main()