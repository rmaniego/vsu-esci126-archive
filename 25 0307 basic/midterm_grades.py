def main():
    
    grades = [92, 89, 93, 95, 79, 88, 98]
    
    total = sum(grades)
    length = len(grades)
    
    average = total / length
    
    print(f"Average grade: {average:.2f}")
    

if __name__ == "__main__":
	main()