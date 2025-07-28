#Ex-1
#1
def add_two_numbers(a,b):
  return a+b
add_two_numbers(3,8)

#2
def area_of_circle(r):
  area=3.14*r*r
  print(area)

area_of_circle(10)

#3
def add_all_nums(*nums):
  total=0
  for num in nums:
    if not isinstance(num,(int,float)):
      print("All arguments must be numbers")
    total += num
  return total

print(add_all_nums(12,5,64,6,1,))