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
ascii_art = pyfiglet.figlet_format("Lamar") # You can change my name "Lamar" to your name or any name..eg (FOOD-STOP, FAST FOODS)
print(ascii_art)
###################################################################################################################################################
#self practice...
# Today i will be coding a simple shopping cart price calculator, which included the quantity of item and price.

name = str(input("Please enter your name to surve you better: "))
title = str(input("Please enter your title here, eg'mr.', 'miss.': "))
item = str(input(f"Hello {title}. {name}, What item would you like to buy?: "))
price = float(input(f"What is the price of the {item}?: "))
quantity = int(input(f"How many {item}/s would you like to buy?: "))

total = price * quantity

print(f"You have bought {quantity} x {item}/s")
print(f"Your total is: ksh{total}") #use any currency you like..my Motherland's (KENYA) currency is "ksh"
print(f"Thank you for shopping with us {title}. {name}, we hope to serve you once again in the future.")

# python is lovely..