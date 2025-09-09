print("Section 1 : Comparison operators :")
age =19
print("Age :",age)
print("is Age Not equal to 18", age != 18 )
print("Is age not equal to 20?", age != 20)    # Not equal to
print("Is age greater than 16?", age > 16)     # Greater than
print("Is age less than 25?", age < 25)        # Less than
print("Is age >= 18?", age >= 18)              # Greater than or equal
print("Is age <= 17?", age <= 17)  

print("\nLet's try with String :")
name = "Sameer"
print("\nName Comparison:")
print("Is name 'Alice'", name == 'Alice')
print("Is name 'Sameer'", name == 'Sameer')
print("Is name 'SAMEER'", name =='SAMEER')

temp = int(input("Enter the temparature of your city: "))
if(temp > 35):
    print("It's very Hot")


elif(temp>35 and temp<45):
    print("It's Hot")

else:
    print("It's cool")


print("Section 3 : Logical Operator")
age = int(input("Enter Your age"))
has_license = True

if age >= 18 and has_license == True:
    print("You can drive")
else:
    print("You can't drive")

is_weekend = bool(input("Enter 0 for weekend and 1 for holiday"))
if(is_weekend or age<18):
    print("Relax You can")
else:
    print("Keep working and growing")

is_raining = bool(input("Enter 1 for rain and 0 for not rain"))
if not is_raining:
    print("Let's Roam in Rome")
else: 
    print("Let's sit at home")


print("nested if statment already done")


print("\nPersonal Finance Advisor: ")
income = int(input("Enter the monthly salary:"))
exp = int(input("Enter the monthly Expenses"))

Savings = income - exp
sav_percent = Savings/income *100

if(sav_percent >= 20):
    print("Excellent Savings")
elif(sav_percent>=10):
    print("Good savings but can be better")
elif(sav_percent>0):
    print("Try to start some savings")
else:
    print("Increase Your income or reduce the expenses")


