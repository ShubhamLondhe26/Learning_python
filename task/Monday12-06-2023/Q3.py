#3. Write a program to check if a string contains any special character

import re

def has_special_characters(string):
    # Regular expression pattern to match special characters
    pattern = r"[!@#$%^&*(),.?\":{}|<>]"

    # Check if the string contains any special characters
    if re.search(pattern, string):
        return True
    else:
        return False

def main():
    string = input("Enter a string: ")
    if has_special_characters(string):
        print("The string contains special characters.")
    else:
        print("The string does not contain any special characters.")

if __name__ == "__main__":
    main()
