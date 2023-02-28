import random
import string

def pass_generate(min_length, numbers=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    # print(letters,digits,special)
    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special

    pwd = ""
    meets_criteria = False
    has_number = False
    has_special = False

    while not meets_criteria or len(pwd) < min_length:
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True
        
        meets_criteria = True
        if numbers:
            meets_criteria = has_number
        if special_characters:
            meets_criteria = meets_criteria and has_special

    return pwd

min_length = int(input("Enter The Minimum Length: "))
has_number = input("Do You Want a have Number (y/n)? ").lower() == "y"
has_special = input("Do You Want a special character (y/n)? ").lower() == "y"

pwd = pass_generate(min_length, has_number, has_special)
print("The Generated Password is: ",pwd)