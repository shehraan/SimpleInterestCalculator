#SI = P*R*T
#Input - Takes the Principal, Rate, and Time from the user.
symbols = ["`","~","!","@","$","%","^","&","*","(",")","_","+","=","/","{","}","|",":",",","<",">","?","'",'"',"[","]"]
numbers = ["1","2","3","4","4","5","6","7","8","9","0"]
areaCodeWrong=0

#Symbolchecker
def symbol(word):
    for letters in word:
        if (letters in symbols)==True:
            return True
    return False

#Numberchecker - checks for numbers in an input
def number(word):
    for letters in word:
        if (letters in numbers)==True:
            return True
    return False



while True:
    principal = input("Please enter the principal amount: ")
    while symbol(principal)==True or any(i.isalpha() for i in principal)==True or number(principal)==True:
        if symbol(principal)==True:
            print("Error, you entered a symbol which is an invalid input. Please only enter a positive number.")
            areaCodeWrong=areaCodeWrong+1
            principal = input("Please enter the principal amount: ")
        if any(i.isalpha() for i in principal)==True:
            print("Error, you entered a letter which is an invalid input. Please only enter a positive number.")
            principal = input("Please enter the principal amount: ")
            areaCodeWrong=areaCodeWrong+1
        if number(principal)==True:
            if float(principal)<0:
                print("Error, you have entered a negative principal which is not possible. Please enter a positive number.")
                principal = input("Please enter the principal amount: ")
            areaCodeWrong=areaCodeWrong+1
            else:
                break
            
    rate = input("Please enter the percentage rate of interest in numbers: ")
    while symbol(rate)==True or any(i.isalpha() for i in rate)==True or number(rate)==True:
        if symbol(rate)==True:
            print("Error, you entered a symbol which is an invalid input. Please only enter a positive number.")
            rate = input("Please enter the percentage rate of interest in numbers: ")
        if any(i.isalpha() for i in rate)==True:
            print("Error, you entered a letter which is an invalid input. Please only enter a positive number.")
            rate = input("Please enter the percentage rate of interest in numbers: ")
        if number(rate)==True:
            if float(rate)<0:
                print("Error, you have entered a negative rate of interest which is not possible. Please enter a positive number.")
                rate = input("Please enter the percentage rate of interest in numbers: ")
            else:
                break
    
    time = input("Please enter the time in years for which the principal amount is given: ")
    while symbol(time)==True or any(i.isalpha() for i in time)==True or number(time)==True:
        if symbol(time)==True:
            print("Error, you entered a symbol which is an invalid input. Please only enter a positive number.")
            time = input("Please enter the time in years for which the principal amount is given: ")
        if any(i.isalpha() for i in time)==True:
            print("Error, you entered a letter which is an invalid input. Please only enter a positive number.")
            time = input("Please enter the time in years for which the principal amount is given: ")
        if number(time)==True:
            if float(time)<0:
                print("Error, you have entered a negative rate of interest which is not possible. Please enter a positive number.")
                time = input("Please enter the time in years for which the principal amount is given: ")
            else:
                break

#Process - Calculating the Simple Interest
    principal = float(principal)
    rate = float(rate)/100
    time = float(time)
    simpleInterest = principal*rate*time
    amount = simpleInterest+principal
    
#Output - diplaying the amount that must be returned
    print("The amount that must be returned is: "+str(amount)) 
    redo = (input("If you would like to use this program again, please enter 'y' \nIf you would like to exit the program, please enter 'n': ")).lower()
    while redo!="y" and redo!="n":
        print("Error, please enter one of the given options")
        redo = (input("If you would like to use this program again, please enter 'y' \nIf you would like to exit the program, please enter 'n': ")).lower()
    if redo=="n":
        break
    else:
        print("\nRestarting program\n")