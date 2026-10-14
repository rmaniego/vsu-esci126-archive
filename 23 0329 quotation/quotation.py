# ask the user for the quotation
# strip: remove extra spaces on both sides
# lower: convert the quotation to lower case
quotation = input("What's your favorite quotation? ").strip().lower()

# if quotation is not empty,
# perform the code inside the if-statement
if quotation:
    # characters = sorted(list(set(list(quotation))))
    characters = list(quotation)    # convert quotation string to a list
    characters = set(characters)    # remove duplicate characters (set)
    characters = list(characters)   # convert characters back to a list
    characters = sorted(characters) # sort characters alphabetically
    
    for character in characters:
        # check if character is an alphabet
        if not character.isalpha():
            continue
        
        # count the occurence of each unique character
        count = quotation.count(character)
        # print character count
        print(f"{character}: {count}")