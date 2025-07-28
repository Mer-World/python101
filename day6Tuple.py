#ex-1  
#1
empty_tuple = ()
#2
brothers=('Isreal','kerod','eluid')
sisters=('Tsionawit','Jeswit','Shalom')
#3
siblings = brothers + sisters
#4
print(len(siblings))  #6
#5
family_members=list(siblings)
family_members.extend(['Dejene','Konjit'])
print(family_members)

#ex-2
#1
print(family_members[0:6]) #siblings
print(family_members[-2:]) #family

#2
fruits=('banana','mango')
vegetables=('tomato','potato')
animal_products=('milk','meat')
food_stuff_tp=fruits+vegetables+animal_products
#3
food_stuff_lt=list(food_stuff_tp)
#4
length = len(food_stuff_lt)
half=length//2
if length%2 == 0:
    middle_items=food_stuff_lt[half-1:half+1]
else:
    middle_items=[food_stuff_lt[half]]

print("Middle item(s): ", middle_items)
#5
print(food_stuff_lt[0:half+1]) # First half
print(food_stuff_lt[half:]) # Second half
#6
del food_staff_tp # Deleting the tuple
#7
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

if 'Estonia' in nordic_countries:
    print("Estonia is a Nordic country")
else:
    print("Estonia is not a Nordic country")

if 'Iceland' in nordic_countries:
    print("Iceland is a Nordic country")
else:
    print("Iceland is not a Nordic country")

