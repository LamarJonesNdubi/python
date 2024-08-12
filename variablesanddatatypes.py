#< PYTHON NOTES>
#-variables and data types

# variables = this are containers used for stroing a value
#             variables behaves as if it were the value it contains
#variables are containers for storing data values. They can hold different types of data such as numbers, texts and more.

#DECLARATION OF VARIABLES
#in python, you do not need to declare the type of variables you, you just assign a value to it using the '=' sign.
#in example...
x = 5 #integer
name = "Lamar" #string
Price = 300.000 #float

#NAMING RULES
#variables names must start with a letter or underscore ( _ )
#they can not start with a number and should not contain spaces or special characters ( except _ )
#examples of vaid variable names: ' user_name', 'age', '_ score'
#example of invalid variables name: '2user', 'first-name', '@age'

age = 22
print(age)
print("you are " + str(age) + " years old ")
print("you are" ,age, "years old")
print(f"you are {age} years old")#the "f" inside the brackets is know as "f-string" this is a popular way.
#from now on i will be using the f-string.

#DATA TYPES
#common data types in python include the following:
# > Integers(int): whole numbers without a decimal point, for example: '10', '-3', '0'
# > Floating-point numbers(float): numbers with a decimal point, for example: '3.14', '-0.01'
# > String(str): text enclosed within quotes, sometimes with numbers in it but we treat them defferently from floats, for example: "Hello, Earth!", "The warzone player with the in game name: ID700605169"
# > Booleans(bool): represents one of two values: 'True' or 'False'
# > List: ordered collection of items, for example: 'numbers = [1, 2, 3, 4]'
# > Dictionaries(dit): collection of key-value pairs, for example: 'person = {"name": "Lamar", "age":22}'
#Example of all different data types:
age = 22 #int
temperature = 21.1 #float
greeting = "Hello" #string str
gametag = "ID700605169" #string str (with numbers included)
is_logged_in = True #boolean bool
fruits = ["watermellon", "jackfruit", "grapes", "kiwi fruit"] #list
person = {"name": "Lamar", "city": "Nairobi"} #dictionaries dict


#PRACTICAL EXAMPLES:
#################################################################################################################################################
#strings str
name = "Lamar"
profession = "A.I Engineer"
food = "Burgers"
Email = "Lamar@fakemail.com"
activision_gamer_tag = "ID700605169"
##################################################################################################################################################
#floats 
gdp = 4.0
kd = 10.0
score = 100.00
##################################################################################################################################################
#boolean bool
online = True
self_taught = True
broke = True
###################################################################################################################################################
#integer int
age = 22
future_salary = 300000
bank_balance = 0
###################################################################################################################################################
#list
games = ["warzone", "call of duty mobile", "Battlefield"]
###################################################################################################################################################
#dictionary dit
person = {"name": "Lamar", "city": "Nairobi"} 
###################################################################################################################################################



