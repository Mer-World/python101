#to declare
# students=dict()
#or
students={'name':'hanna','age':26,"sec":'B'}
print(students)
#length
print(len(students))
#accessing an element
print(students['name'])
#adding an item
students['last_name']='kebede'
#modifying an item
students['last_name']="yakob"
#check if the key exists
print('name' in students) #true
print('first_name' in students) #false
#pop
students.pop('last_name')#removes age
#to print the keys only as a list
print(students.keys())
#to print the values as a list
print(students.values())