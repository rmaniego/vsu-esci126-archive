def main():
    grades = [92, 89, 93, 95, 79, 88, 98]
    print("Minimum:", min(grades))
    print("Maximum:", max(grades))
    
    average = sum(grades) / len(grades)
    print(f"Average: {average:.2f}")

if __name__ == "__main__":
    main()