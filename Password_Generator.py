import random
import string

def generate_password(min_length, numbers=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special_characters = string.punctuation
    
    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special_characters
        
    pwrd = ""
    meets_criteria = False
    has_number = False
    has_special = False
    
    while not meets_criteria or len(pwrd) < min_length:
        new_char = random.choice(characters)
        pwrd += new_char
        
        if new_char in digits:
            has_number = True
        elif new_char in special_characters:
            has_special = True
            
        meets_criteria = True
        if numbers:
            meets_criteria = has_number
        if special_characters:
            meets_criteria = meets_criteria and has_special
    
    return pwrd
        
min_length = int(input("Minimum password length: "))
has_numbers = input("Need numbers? (y/n): ").lower() == "y"
has_special = input("Need special characters? (y/n): ").lower() == "y"
pwrd = generate_password(min_length, has_numbers, has_special)
print("Generated password: ", pwrd)
