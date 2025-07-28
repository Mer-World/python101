#Ex-1
#1
log={}
#2
log={'name':'Meronawit',
     'Color':'Brown',
     'Breed':'Ethiopian',
     'legs':2,
     'age':22
     }
#3
student = {
    "first_name": "John",
    "last_name": "Doe",
    "gender": "Male",
    "age": 21,
    "marital_status": "Single",
    "skills": ["Python", "JavaScript", "HTML"],
    "country": "USA",
    "city": "New York",
    "address": "123 Main Street"
}
#4
print(len(student))
#5
skillValue = student["skills"]
print(type(skillValue))
#6
student["skills"].extend(["Java","CSS","ERP"])
print(student)
#7
print(list(student.keys()))
#8
print(list(student.values()))
#9
student_tpl = student.items()
#10
del student["skills"][0]

#11
del student["address"]
