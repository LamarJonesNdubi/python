# typeasting = The process of converting a value of one data to another.
#             (string, booleans, float, integer)
#             Explicit vs Implicit
# to make it simple.. its is the changone of data from it original...
# data type to another..like from string to boolean, integer to float
# float to boolean i guess....

# we can use the type function to undestand the type of data we aded
# example as show bellow: 

age = 22 #integer int
name = "Lamar" #string str
gpa = 4.0 #float
student = False #boolean bool

print(type(age))
print(type(name))
print(type(gpa))
print(type(student))
# and we run it...should display every data type of each variable..
# in the output terminal..depending with the text editor in use

# now example as an Explicit typecast: from integer to float
age = float(age) #will change the integer 22 into a float 22.0
print(age)
# should display as 22.0
# if you try: print(type(age))
# it will tell you that it is a float now.
print(type(age))

# other examples..from float to integer
gpa = int(gpa)
print(gpa)
# should display as 4
# it olso gets reed or hides thw decimal sides even if the gpa could have been 4.09..the .09 part is hidden
# if you try: print(type(gpa))
# it will tell you that it is a integer now.
print(type(gpa))

#another example..from boolean to string
student = str(student)
print(student)
# nothing much happens because they 'false' is both in texts
# if you try: print(type(student)
# it will tell you that it is a string now.
print(type(student))

name = bool(name)
print(name)

# alright..thats done for now.


#############################################################################################################################################
#NOW..USING IMPLICIT
# IMPLICIT are typecasts deployed automatically
# in Example...

x = 2 #integer
y = 2.0 # float
# lets divide an integer by a float we see what will display
x = x / y
print(x)
# and it brings back 1.0 which we know it is a float data type
# but since we are experimentiong with code..lest confirm that shall we :)....with typecast
print(type(x))
# the execution output returns 'float'...it typasted it automaticaly

