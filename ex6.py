# Exercise 6, Learn Python the Hard Way
# define a variable
types_of_people = 10

# define var x with a formatted string
x = f"There are {types_of_people} types of people."

# define variable
binary = "binary"
# define variable
do_not = "don't"
# define var y with formatted string
y = f"Those who know {binary} and those who {do_not}."

#print var x and y
print(x)
print(y)

#use fstring to print x and y.  Same as before, but string in string
print(f"I said: {x}")
print(f"I also said: '{y}'")

#define variable
hilarious = False
# define variable with input
joke_evaluation = "Isn't that joke so funny?! {}"

#print using .format and variable 
print(joke_evaluation.format(hilarious))

#define variables
w = "This is the left side of..."
e = "a string with a right side."

#concatenate strings
print(w + e)