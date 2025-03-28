from datetime import datetime


def main():
    dt = datetime.now()
    print(dt.strftime("%B %d, %Y (%A)"))


if __name__ == "__main__":
    main()
