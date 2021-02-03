import traceback

def calculator():
    
    # Get dog age
    age = input("Input dog years: ")
    try: 
        age = int(age)
    except ValueError as e:
        print(age, "is invalid")
    try:
        # Cast to float
        d_age = float(age)
        # If user enters negative number, print message
        
        if d_age < 0:
            print("Age cannot be a negative number")
        # Otherwise, calculate dog's age in human years
        if (d_age >= 0.1 and d_age <= 1):
            h_age = d_age * 15
            print("The given dog age" , d_age , "is" , h_age , "in human years")
        elif (d_age >= 1.1 and d_age <= 2):
            h_age = d_age * 12
            print("The given dog age" , d_age , "is" , h_age , "in human years")
        elif (d_age >= 2.1 and d_age <= 3):
            h_age = round((d_age * 9.3), 2)
            print("The given dog age" , d_age , "is" , h_age , "in human years")
        elif (d_age >= 3.1 and d_age <= 4):
            h_age = d_age * 8
            print("The given dog age" , d_age , "is" , h_age , "in human years")
        elif (d_age >= 4.1 and d_age <= 5):
            h_age = d_age * 7.2
            print("The given dog age" , d_age , "is" , h_age , "in human years")
        else:
            h_age = d_age * 7 + 1
            print("The given dog age" , d_age , "is" , h_age , "in human years")
        
        # your code here
         
            
            
    except:
        print(age, "is an invalid age.")
        print(traceback.format_exc())
    
calculator()
