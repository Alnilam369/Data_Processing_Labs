text = input("short sentence: ")

characters = len(text)
vowels = 0
spaces = 0

for character in text:
    if character.lower() in "aeiou":
        vowels += 1

    if character == " ":
        spaces += 1

print("Number of characters:", characters)
print("Number of vowels:", vowels)
print("Number of spaces:", spaces)