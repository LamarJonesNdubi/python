####################################################################################################################################################
#                                                             [LAMAR]
####################################################################################################################################################
import subprocess
import sys

# Function to install a package if it's not already installed
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Try importing the package; if it fails, install it
try:
    import pyfiglet
except ImportError:
    print("pyfiglet not found. Installing...")
    install("pyfiglet")
    import pyfiglet

# Now you can use pyfiglet as usual
ascii_art = pyfiglet.figlet_format("Lamar")
print(ascii_art)
###################################################################################################################################################
#self practice...
#today i will be programming a simple and basic buyer credit checker using python

# Price of  house is $1,000,000
# if the buyer has good credit, they need to put down 10%
# else they need to put down 20%
# and should print a down payment

import math # i dont know how i will use this here

name = str(input("Please enter your name: "))
house_price = 1000000
credit_score = int(input("Enter your credit score: "))
exellent_credit = 5
good_credit = 10
bad_credit = 20

if credit_score >= 740:
    print(f"Your credit score is remarkable, you have earned {exellent_credit}% as your down payment of the house.")
    result = house_price * exellent_credit / 100
    print(f"Dear {name}, your down payment will be {result}")
elif credit_score >= 670:
    print(f"Your credit score is good, you have earned {good_credit}% as your down payment of the house.")
    result = house_price * good_credit / 100
    print(f"Dear {name}, your down payment will be {result}")
else:
    print(f"We find your credit score lower than our requiements, but you have earned {bad_credit}% as your down payment of the house.")
    result = house_price * bad_credit / 100
    print(f"Dear {name}, your down payment will be {result}")
print(f"Thank you for using our service {name}.")   
