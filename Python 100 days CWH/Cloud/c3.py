# print("=== SECTION 1: Basic For Loops ===")

# # Simple counting from 0 to 4
# print("Counting with range(5):")
# for i in range(5):
#     print("Count:", i)

# print("\nCounting from 1 to 5:")
# for i in range(1, 6):  # Start at 1, stop before 6
#     print("Number:", i)

# print("\nCounting by 2s:")
# for i in range(0, 11, 2):  # Start, stop, step
#     print("Even number:", i)

# print("\nCounting backwards:")
# for i in range(10, 0, -1):  # Start at 10, stop before 0, step -1
#     print("Countdown:", i)
# print("Blast off! 🚀")

# print("\n\nMultiplication table : ")
# for i in range (1,11):
#     result = i*7
#     print(f"7 x {i} = {result}")

# print("\nSection : Loops with Strings:-")
# word = "Python"
# print(f"letter in word '{word}':")
# for letter in word:
#     print(f"{letter}")


# text = input("Enter your text: ")
# vowels = "aeiouAEIOU"
# vowel_count = 0

# print(f"Analyzing : {text}")
# for char in text:
#     if char in vowels:
#         print(f"Found vowel, {char}")
#         vowel_count +=1
# print(f"Total vowel : {vowel_count}")


# print("Password Validator ")
# correct_password = input("Enter the password and then check it")

# attempts =0
# while attempts <=5:
#     attempts+=1
#     check = input("Enter Random password to check")
#     if(check == correct_password):
#         print("Access Granted")
#         break
#     else:
#         remaining_attempts = 5 - attempts
#         if remaining_attempts > 0 :
#             print(f"Access Denied remaining attempts = {remaining_attempts}")
#         else:
#             print("Access denied. Password limit Reached")
#             break

# print("\n----Number Guessing Game ----")
# import random

# secret = random.randint(1,10)
# guessed = False
# attempts = 0
# print("I am thinking a number between 1 and 10 \nYou have 3 attempts to guess it ")
# while not guessed and attempts<3:
#      attempts+=1
#      guess = int(input("Enter your guess:-"))

#      if guess == secret:
#             print(f"You win the number is {guess}")
#             guessed = True
        
#      elif guess < secret:
#          print("too low!")

#      else:
#          print("too high!")

#      if not guessed and attempts < 3:
#             print(f"Attempts left :{3-attempts}")

#      if not guessed:
#         print(f"Game over! The number was {secret}")

for row in range(1,6):
    for star in range(row):
        print("*",end = "")
    print()

print("/nCreating a multiplication table:")
print("   ", end = "")
for i in range (1,6):
    print(f"{i:4}", end = "")

print()

for i in range(1,6):
    print(f"{i}: ", end = "")
    for j in range(1,6):
        result = i*j
        print(f"{result: 4}", end= "")
    print()



print("\n=== SECTION 5: Loop Control ===")

# Using break to exit early
print("Finding the first number divisible by 7:")
for num in range(20, 100):
    if num % 7 == 0:  # % is modulo operator (remainder)
        print(f"Found it: {num}")
        break

# Using continue to skip iterations
print("\nPrinting odd numbers from 1 to 10:")
for num in range(1, 11):
    if num % 2 == 0:  # If number is even
        continue  # Skip the rest and go to next iteration
    print(f"Odd number: {num}")


print("\nSimple Calculator: ")
while(True):
    operation = input("Enter any operator + , - , * or /  Or Enter 'quit' to quit the calculator")

    if operation.lower() == 'quit':
        print("calculator shutting down. Goodbye!")
        break

    if operation in ['+', '-', '*', '/']:
        try:
            num1 = float(input("First number: "))
            num2 = float(input("Second number: "))

            if operation == '+':
            result = num1 + num2
            elif operation == '-':
            result = num1 - num2
            elif operation == '*':
            result = num1 * num2
            elif operation == '/':
            if num2 == 0:
                    print("❌ Error: Cannot divide by zero!")
                    continue
                result = num1 / num2

    