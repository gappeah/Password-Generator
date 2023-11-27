This a simple password generator written in Python where the user can enter the length of the password and it will generate a random password of that length numbers, letters and symbols.
The project serves as an example of how to use the `random` module in Python, the `string` module in Python.
In addition, it also serves as a good example of how to use the Git and GitHub in Python

Password Generator

This program generates random passwords based on specified criteria.
Usage

Run the program and follow the prompts to enter the minimum password length, whether numbers are required, and whether special characters are required. The program will then generate a password meeting the specified criteria.

Example Usage

![image](https://github.com/gappeah/Password-Generator/assets/114095068/4973b65b-da84-4911-a808-780bcd435ca7)


Code Breakdown

The code first imports the random and string modules, which are used for generating random characters and accessing string constants, respectively.

The generate_password function takes three arguments: min_length, numbers, and special_characters. The min_length argument specifies the minimum length of the password. The numbers argument indicates whether numbers should be included in the password. The special_characters argument indicates whether special characters should be included in the password.

The function first initializes three strings: letters, digits, and special_characters. These strings contain the characters from the ASCII letters, digits, and punctuation, respectively.

The function then constructs the characters string, which contains all of the characters that will be used to generate the password. The characters string is constructed by concatenating the letters string with the digits string and the special_characters string, depending on whether the numbers and special_characters flags are set to True.

The function then initializes an empty string called pwrd, which will be used to store the generated password. The function also initializes three boolean flags: meets_criteria, has_number, and has_special. The meets_criteria flag indicates whether the generated password meets all of the specified criteria. The has_number flag indicates whether the generated password contains at least one number. The has_special flag indicates whether the generated password contains at least one special character.

The function then enters a loop that continues until the generated password meets all of the specified criteria and is at least the minimum length. Inside the loop, a new character is selected from the characters string and appended to the pwrd string. The has_number and has_special flags are also updated accordingly.

After the loop exits, the function returns the generated password.

The min_length variable is set to the value entered by the user. The has_numbers variable is set to True if the user entered "y" when prompted for whether numbers are required. The has_special variable is set to True if the user entered "y" when prompted for whether special characters are required.

The pwrd variable is set to the result of calling the generate_password function with the specified parameters. The generated password is then printed to the console.
