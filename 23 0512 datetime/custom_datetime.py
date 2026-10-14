from datetime import datetime

def main():    
    # https://help.gnome.org/users/gthumb/stable/gthumb-date-formats.html.en
    code = input("Enter datetime format (%Y-%m-%d): ")
    
    is_supported = check_if_supported(code)
    
    if not is_supported:
        print(f"Error: The '{code}' contains unsupported values.")
        return

    formatted = convert(code)
    print(f"Formatted: {formatted}")

def convert(code):
    return datetime.now().strftime(code)

def check_if_supported(code):
    """
    Valid
    %Y-%m-%d %I:%M:%S %p
    %B %d, %Y %A
    %b-%d, %Y %A

    Invalid
    %Y %H:%M%q
    %B %d, %N
    """
    # https://help.gnome.org/users/gthumb/stable/gthumb-date-formats.html.en
    supported = "AaBbCcDdFGgHhIjklMmOPpRrSsTUuVvWwXxYyZz"
    for character in code:
        if not character.isalpha():
            continue
        if character not in supported:
            return False
    return True

if __name__ == "__main__":
    main()