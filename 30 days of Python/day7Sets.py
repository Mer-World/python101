#Ex -1

# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
#1
print(len(it_companies))
#2
it_companies.add('Twitter')
#3
it_companies.update(['Mer-World','Ict','A Rc'])
#4
it_companies.pop()
#5
#remove:-have to check if the item exist or else raises error
#discard:- doesnt raise error

#Ex-2

#1
print(A.union(B))
#2
print(A.intersection(B))
#3
print(A.issubset(B))
#4
print(A.isdisjoint(B))
#7
del A

#Ex-3
#1
setAge = set(age)
if len(setAge) > len(age):
    print("set")
elif len(setAge) < len(age):
    print("list")
else:
    print("equal")
#2

sentence="I am a teacher and I love to inspire and teach people" 

sentence =  sentence.replace('.','')

words= sentence.split()

uniqueWords = set(words)   
print("Unique words in the sentence:", uniqueWords)
print("Number of unique words:", len(uniqueWords))