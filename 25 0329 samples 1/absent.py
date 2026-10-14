

def main():
    students = {
        "Juan": 1,
        "Maria": 1,
        "Pedro": 0,
        "Grace": 1,
        "Jovan": 0,
        "Feddy": 0,
        "Renz": 1
    }
    
    print("Present Students:")
    for student, present in students.items():
        if not present:
            continue
        print(f" * {student}")

if __name__ == "__main__":
    main()