def main(count=0):
    
    try:
        number = int(input("Enter a number: "))
    except ValueError as e:
        print("Warning: Value must be an integer.")
        if count==3:
            print("Error: Gahia'g itlog uy!.")
            return
        main(count+1)

if __name__ == "__main__":
    main()