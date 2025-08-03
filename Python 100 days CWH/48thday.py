print("Solution of Exercise 4th of python 100 days")
# Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language

# Coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end
#   now append three random characters at the starting and the end
# else:
#   simply reverse the string

# Decoding:
# if the word contains less than 3 characters, reverse it
# else:
#   remove 3 random characters from start and end. Now remove the last letter and append it to the beginning
# Your program should ask whether you want to code or decode
print("Enter your Message or String:")
message = input()
print("Enter your choice:")
print("1. Code")
print("2. Decode")
choice = int(input())
if choice == 1:
    words = message.split()
    secret_code = []
    for word in words:
        if len(word) >= 3:
            new_word = word[1:] + word[0] + "abc" + word + "xyz"
            secret_code.append(new_word)
        else:
            secret_code.append(word[::-1])
    print("Secret Code:", " ".join(secret_code))
elif choice == 2:
    words = message.split()
    decoded_message = []
    for word in words:
        if len(word) < 3:
            decoded_message.append(word[::-1])
        else:
            new_word = word[3:-3]
            decoded_message.append(new_word[-1] + new_word[:-1])
    print("Decoded Message:", " ".join(decoded_message))
else:
    print("Invalid Choice")
# Output:
# Enter your Message or String:
# Hello World
# Enter your choice:
# 1. Code
# 2. Decode
# 1
# Secret Code: elloHabcHello Worldxyz
#
# Enter your Message or String:
# elloHabcHello Worldxyz
# Enter your choice:
# 1. Code
# 2. Decode
# 2
# Decoded Message: Hello World
#
# Enter your Message or String:
# Hello
# Enter your choice: