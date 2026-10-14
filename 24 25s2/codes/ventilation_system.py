

def main():
    humidity = float(input("Enter humidity: "))
    if 60 <= humidity <= 70:
        print("Relative Humidity is optimal.")
    else:
        print("Adjust ventilation...")

if __name__ == "__main__":
    main()