#created list
names = list()
stu_list=['hanna','alex','abel','yakob','miki']
#to know type
print(type(names))
#to know length(to know if its empty)
print(len(names))
#negative indexing
print(stu_list[-2])
#list unpacking
first,second,*third=stu_list
print(third)
#slicing
new_list= stu_list[2:4]
print(new_list)
#slicing+negative index
neg_list=stu_list[-4:-2]
print(neg_list)

#modifying list
stu_list[0]='Meron'
print(stu_list)

#check if a name exists in list
#you can do it using "in"
print('Meron' in stu_list)
#adding items to a list
stu_list.append('hermi')
print(stu_list)
#adding items to a list in specific index
stu_list.insert(2,'kal')
print(stu_list)

#remove
# stu_list.remove('hanna')
#pop
print(stu_list.pop())
#clear
#stu_list.clear() clear all elemets

#to copy alist
newest_list=stu_list.copy()

#to delete on lits
del stu_list[4]
print (stu_list)

#concatination
numbers=[1,3,5,0,33,12]
combined_list=numbers+stu_list
print(combined_list)

#extend
#another way to concatinate(join)
combined_list=numbers.extend(stu_list)

#to count
# print(combined_list.count())

#finding index
index=stu_list.index("miki")
print(index)

#reverse
print(combined_list.reverse())

#sorting method
print(numbers.sort())