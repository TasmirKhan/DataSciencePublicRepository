# print("Today is the 28th day of python we will Study about f-strings")
# letter = "Hey my name is {1} and I am from {0}"
# country = "India"
# name = "Harry"

# print(letter.format(country, name))
# print(f"Hey my name is {name} and I am from {country}")
# print(f"We use f-strings like this: Hey my name is {{name}} and I am from {{country}}")
# price = 49.09999
# txt = f"For only {price:.2f} dollars!"
# print(txt)
# # print(txt.format())
# print(type(f"{2 * 30}"))
print("today we are going to learn about the f-strings which is used for easy formating")
letter = "Hello my name is {1} and I am from {0}"
country = "India"
name = "Tasmir Khan"
print(letter.format(country,name))
print(f"Hello myself {name} and I am from {country}")
print(f"We use f strings like this : \nHello myself {{name}} and I am from {{country}}")
price = 49.08909899
txt  = f"for only {price: .2f} dollars:"
print(txt)
print(txt.format())
print(type(f"{2*30}"))