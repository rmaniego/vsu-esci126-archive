def main():
    
    """
    crops = {}
    
    crop = input("\nWhat crop? ")
    harvest = float(input(f"How many tonnes of '{crop}'? "))
    crops[crop] = harvest
    print(crops)
    
    crop = input("\nWhat crop? ")
    harvest = float(input(f"How many tonnes of '{crop}'? "))
    crops[crop] = harvest
    print(crops)
    
    crop = input("\nWhat crop? ")
    harvest = float(input(f"How many tonnes of '{crop}'? "))
    crops[crop] = harvest
    print(crops)
    """
    
    crops = {'Rice': 1000000.0, 'Marijuana': 50000.0, 'Cacao': 3000.0}
    
    
    search = input("\nWhat crop to search? ")
    total = crops.get(search, 0)
    print(f"There are {total:,.2f} tonnes of {search} in the warehouse.")
    

if __name__ == "__main__":
	main()