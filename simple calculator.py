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

# SIMPLE PYTHON CALCULATOR
# today i will be coding a simple python calculator with basic functions..

name = input("Please let me know your name: ")
operator = input(f"Hello there {name}, Please enter an operator you wish to use (+ - * /): ")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if operator == "+":
    result = num1 + num2
    print(round(result, 3))
elif operator == "-":
    result = num1 - num2  
    print(round(result, 3)) 
elif operator == "*":
    result = num1 * num2 
    print(round(result, 3))
elif operator == "/":
    result = num1 / num2
    print(round(result, 3))
elif operator == "#":
    print(f"Who is your maths teacher {name} ?") 
elif operator == "$/$":
    print(f"Downloading Democracy into {name}' computer files and system....... ?")  
    print(f"Download completed!")    
else:
    print(f"Math error...{operator} not valid")    