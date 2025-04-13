string1=input("Enter a string for converting it to uppercase: ")
str = string1
upper_lambda = lambda string:string.upper()
print(upper_lambda(str))

string2 = input("Enter a string to check if it starts with a specific letter: ")
start_char = input("Enter the character to check if the string starts with it: ")
starts_with = lambda string, char: string.startswith(char)
result = starts_with(string2, start_char)
print(f"Does the string '{string2}' start with '{start_char}'? {result}")
