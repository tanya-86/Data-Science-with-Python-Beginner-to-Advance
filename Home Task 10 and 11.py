#Q. A Caesar cipher is a simple substitution cipher in which each letter of the plain text is substituted with a letter
# found by moving n places down the alphabet. For example, assume the input plain text is the following:

# abcd xyz

# If the shift value, n, is 4, then the encrypted text would be the following:

# efgh bcd

# You are to write a function that accepts two arguments, a plain-text message and a number of letters to shift in the cipher.
# The function will return an encrypted string with all letters transformed and all punctuation and whitespace remaining unchanged.

# Note: You can assume the plain text is all lowercase ASCII except for whitespace and punctuation.

# Remember, this part of the question is really about how well you can get around in the standard library. If you find yourself
# figuring out how to do the transform without the library, then save that thought! You’ll need it later!


print("Ans to Q:\n")

text = str(input('Please enter the text message: '))
n = int(input('Please enter the number of letters to shift: '))

import string
def encryption(text, n):
    result = ""
    for i in range(len(text)):
        a = text[i]

        # Encrypt uppercase characters
        if (a.isupper()):
            result += chr((ord(a) + n - 65) % 26 + 65)

        # Encrypt lowercase characters
        elif (a.islower()):
            result += chr((ord(a) + n - 97) % 26 + 97)

        # Encrypt spaces
        elif (ord(a) == 32):
            result += chr(ord(a))

        # Encrypt puncuations
        elif a in string.punctuation:
            result += a
    return result

print("\nGiven string: ", text)
print("Shift : ", n)
print("Encrypted string: ", encryption(text, n))
