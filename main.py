#Landen Dale
#Main.py
#Main purpose is to get input from the user about their car and print the info in a easible readly manner

#Main class for code
class Vehicel:  
        #Input car type
        Type = input("Insert the type of your vehicel you own: ")
        #Input make of car
        Make = input("Insert the make of your vehicel: ")
        #Input model of car
        Model = input ("Insert the model of your vehicel: ")
        #Input year of car
        Year = input('Input the year of your vehicel: ')
        #Input nimber of doors
        Numberofdoors = input("Input the number of doors your vehicel has: ")
        #Input type of roof 
        Roof = input("Input the type of roof your vehicel has:")

        #Print the inputs
        print("Your car type is:", Type)
        print("You car make is:" ,Make)
        print("Your cars model is:" ,Model)
        print("Your cars year is:", Year)
        print("Your cars has:" ,Numberofdoors ,"number of doors")
        print("Your car has a:" ,Roof, "roof")