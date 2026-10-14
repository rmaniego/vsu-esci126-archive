from datetime import datetime


def main():
    seconds_since_1970 = int(datetime.now().timestamp())
    print(f"Seconds since January 1, 1970: {seconds_since_1970} seconds")


if __name__ == "__main__":
    main()