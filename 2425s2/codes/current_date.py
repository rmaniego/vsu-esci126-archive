from datetime import datetime

def main():
    dt = datetime.now()
    print(dt.strftime("%Y-%m-%d %H:%M:%S %p (%A)"))
    print(int(dt.timestamp()))

if __name__ == "__main__":
    main()