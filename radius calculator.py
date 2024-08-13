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
# TODAY I WILL BE CODING THE Area CALCULATOR OF A CIRCLE using the 'import match'
# area = pi * r^2

import math

pi = (math.pi)
name = str(input("Please enter your name: "))
radius = float(input(f"Hello there {name}, please enter the radius of your circle: "))

area = pi * pow(radius, 2)

print("calculating...")
print(f"The area of your circle is {area}cm^2")



