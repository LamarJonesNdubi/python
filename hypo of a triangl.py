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
# TODAY I WLL BE CODING THE HYPOTE..HYPOTENUSS..HYPOT..NEVER MIND...OF A TRIANGLE.
# so the formula of that is c = (square root of): a^2 + b^2

import math

name = input("Please let me know your name: ")
print(f"Hello there {name}, hope you are well today, lets calculate the hypotenus of your triangle...")
a = float(input("Please enter the distance of your length: "))
b = float(input("and the distance of your width: "))
print(f"that it ok {name}")
print("calculating.....")

c = (math.sqrt(pow(a, 2) + pow(b, 2)))
print(f"Hey {name}, your hypotenus is: {c}^2")












