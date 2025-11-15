#while conditions:
    #statement
# #print 1 to 5
# n=1
# while n<=5:
#     if(n==4):
#         continue #we want it to break on 4
#     print(n)
#     n+=1
# else:#we can add else on while
#     print("The Loop is done!")


# #adding even numbers from 1 to 10
# count=1
# sum=0
# while count<=10:
#     if(count%2!=0):
#         continue
#     sum=sum+count
# print(sum)



#for x in collection(could be list,dictionary,set...):
    #statement

#range
#example
# sum=0
# for x in range(1,10,2):
#     sum+=x
# print(sum)


#Question
square=1
total=0
target = int(input("Enter your number:"))
for number in range(target):
    square=number*number
    total=total+square
print(total)

    