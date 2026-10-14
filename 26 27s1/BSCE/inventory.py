

def main():
    toolbox = {}
    print(toolbox)
    
    tool = input("\nEnter the name of the tool: ")
    count = input(f"How many {tool}?")
    
    toolbox[tool] = count
    print(toolbox)

if __name__ == "__main__":
    main()