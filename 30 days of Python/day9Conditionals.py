# #1
# age = int(input("Enter your age: "))
# left = 18 - age

# if age >= 18:
#     print("Youre old enough to drive")
# else:
#     print("You need ", left, "years more to drive")


#Ex-2
# #2
# month = input("Enter the month? ")
# autumn = ['September','October','November']
# winter=['December','January','Feburary']
# spring=['March','April','May']
# summer=['June','July','August']

# if month in autumn:
#     print("Its Autumn")
# elif month in winter:
#     print("Its Winter")
# elif month in spring:
#     print("Its Spring")
# else:
#     print("Its Summer")

#3
# inputFruit = input("Enter your fruit ")
# fruits = ['banana', 'orange', 'mango', 'lemon']

# # If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')

# if inputFruit in fruits:
#     print("That fruit already exist in the list")
# else:
#     print("That fruit does not exist in the list, adding it now.")
#     fruits.append(inputFruit)
#     print("Modified list:", fruits)

#Ex-3
#1
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }



if person["is_marred"] == True:
    print(person["first_name"] , "lives in", person["country"], "and is married.")