

def main():
    
    bsce_majors = [ "Structural Engineering",
                    "Construction Engineering",
                    "Transportation Engineering",
                    "Geotechnical Engineering",
                    "Water Resources"
                ]
    
    index = int(input("What is the major on the nth index: "))
    major = bsce_majors[index]
    print(f"{major}")
    
    major = input("\nEnter your major: ")
    count = bsce_majors.count(major)
    print(f"{major}: {count}")


if __name__ == "__main__":
    main()