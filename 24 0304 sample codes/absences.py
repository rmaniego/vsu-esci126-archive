students = {
        "Aldaya": 1,
        "Galagaran": 0,
        "Abueva": 1,
        "Palo": 1,
        "Patano": 0,
        "Resusta": 1,
        "Isip": 1,
        "Juntilla": 0,
        "Ocubillo": 1,
        "Montano": 1,
    }

print("Active Students:")
for name, present in students.items():
    
    if not present:
        continue
    
    print(f" * {name}")