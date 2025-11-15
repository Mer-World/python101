user_gender=input("What's your gende? F= for female and M= for male")
user_age=int(input("How old are you? "))
user_weight=float(input("Enter your weight "))
user_height=float(input("Enter your height "))


def calculate_BMI():
    print("Your BMI is: ")
    print(user_weight/(user_height*user_height))


def calculate_calorie():
    bmr=0
    if(user_gender=="F"):
        bmr = 447.593+(9.247*user_weight)+(3.098*user_height)-(4.330*user_age)
        print(bmr)
    elif(user_gender=="M"):
        bmr = 88.362+(13.397*user_weight)+(4.799*user_height)-(5.677*user_age)
        print(bmr)
    else:
        print("Please insert M or F for gender")


    
print(calculate_BMI())
print(calculate_calorie())
