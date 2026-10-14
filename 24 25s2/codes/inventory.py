

def main():
    inventory = {
        "Screw": 5,
        "Hammer": 1,
        "Steel brush": 20,
        "Marine plywood 3/4": 50,
        "Boysen elastomeric paint": 4
    }
    
    print("My Inventory:")
    for item, count in inventory.items():
        print(f" * {item} x{count}")

if __name__ == "__main__":
    main()