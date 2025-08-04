# numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
# print ([i for i in numbers if i < 0])
    
# #2
# countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

# contry_list= [{"country":country,"city":city} for [((country,city) )]in countries]

# print(contry_list)


# slopevalue = lambda x1,x2,y1,y2: y2-y1/ x2-x1 

# print(slopevalue(2, 4, 3, 5))


def decorator_with_parameters(function):
    def wrapper_accepting_parameters(para1, para2, para3):
        function(para1, para2, para3)
        print("I live in {}".format(para3))
    return wrapper_accepting_parameters

@decorator_with_parameters
def print_full_name(first_name, last_name, country):
    print("I am {} {}. I love to teach.".format(
        first_name, last_name, country))

print_full_name("Asabeneh", "Yetayeh",'Finland')