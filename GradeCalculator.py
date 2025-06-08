stuName = input("What is your name? ")
dsa = int(input("Your data structure mark? "))
web = int(input("Your web programming mark? "))
discrete = int(input("Your discrete mark? "))
graphics = int(input("Your graphics mark? "))
numerics = int(input("Your numerics mark? "))

avg = (dsa + web + discrete + graphics + numerics) / 5

if avg >= 90 and avg <= 100:
    print ("Hello " + stuName+ " your Grade is A")
elif avg >= 80 and avg <= 89:
    print ("Hello " + stuName+ " your Grade is B")
elif avg >= 70 and avg <= 79:
    print ("Hello " + stuName+ " your Grade is C")
elif avg >= 60 and avg <= 69:
    print ("Hello " + stuName+ " your Grade is D")
else:
    print ("Hello " + stuName+ " your Grade is E")