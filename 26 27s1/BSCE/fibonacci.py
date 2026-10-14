def main():
    previous, temp, count, subsequent = 1, 0, 1, 0
    limit = int(input("Sequence count: "))
    while count <= limit:
        temp = subsequent
        subsequent += previous
        previous = temp
        print(previous)
        count += 1
if __name__ == "__main__":
    main()