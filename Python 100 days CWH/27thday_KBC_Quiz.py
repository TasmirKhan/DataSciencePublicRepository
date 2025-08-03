# print("Create a program capable of displaying questions to the user like KBC. Use List data type to store the questions and their correct answers. Display the final amount the person is taking home after playing the game.")

print("Welcome to KBC quiz!\a")
questions = ("Q.1 Which is the National bird of india", "Q.2 What is the Name of the first prime miniter of India ", "Q.3 How many continents are there in  the world.", "Q.4 What is the inverse of conductor.", "Q.5 What is the approx. radius of Earth.","Q.6 What is the capital of Australia.","Q.7 Which planet is Known as The Red planet ?","Q.8 What is the chemical symbol of Gold ","Q.9 In java which keyword is used to create an object ", "Q.10 Which company developed the java programmin lanugage?" )
answers = ("peacock", "Pt. Jawaharlal Nehru", 7, "insulator", "3200km", "canberra", "Mars", "Au", "new", "Sun Microsystem")
options = (["lion","tiger", "Swan", "peacock"], ["Sardar Vallabh Bhai patel", "Pt. Jawaharlal Nehru", "Mahatama Gandhi", "Dr.Rajendra Prasad"], [6,9,11,7], ["un-conductor","lines","insulator","cable"], ["64000km", "32000km", "6400km", "3200km"], ["canberra", "italy","Austria", "London"], ["uranus", "jupiter", "Venus", "Mars"], ["Ag", "Au", "Gd", "Gl"], ["new", "create", "object", "instance"], ["Oracle Company", "Java Industries", "Oak Microsystem", "Sun Microsystems"])
# print(len(questions))
# print(len(answers))
# print(len(options))
# # while(True):
print("Here the total no. of Questions are 10")
print("If you win then you can achieve a massive amount : So be ready :")
print("And the questions are:")
i=0
finalamount = 0
incorrect = False
# quit = False
while(True):
   if(i==len(questions)):
       break
   print(questions[i])
   print(options[i])
   temp = int(input("Enter your option "))-1
   if(options[i][temp] == answers[i]):
        print("Correct")
        if(finalamount==0):
            finalamount = 1000
        else:
            finalamount = finalamount + (2*finalamount)
   else:
        incorrect = True
        print("Answer is incorrect\a")
        break
   i = i+1

if(incorrect):
    print("Actual amount you can recieve = ", finalamount)
    print("But Now you due to incorrect answer amount= ", finalamount/2)
    
else:
    print("Your winning Amount is ", finalamount)