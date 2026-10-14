def main():
    accounts = {"Juan": 1, "Maria": 1, "Pedro": 0}
    print("Active Accounts:")
    for name, active in accounts.items():
        if not active:
            continue
        print(f" * {name}")
if __name__ == "__main__":
    main()