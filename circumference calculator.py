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

# today i will be trying to code a circumference calculator
# circumference = pi * diameter
# in which the pi of every circle is 3.14159
# so..

pi = 3.14159 #it is a float..meaning the rest of everything should be a float
diameter = float(input("Please enter Diameter: ")) 

circumference = pi * diameter

print(f"The Circumference of your circle is {circumference}cm")










