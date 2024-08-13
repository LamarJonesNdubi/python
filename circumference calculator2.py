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

#this time i will make a calculator that aloows the user to input there own pi formula and diameter as well

pi = float(input("Please enter desired pi formula: "))
diameter = float(input("Please enter your diameter: "))

circumference = pi * diameter

print(f"The circumference of your 'wierd circle' is {circumference}cm")
print("LOL, The founding fathers of Mathematics are rolling in there graves right now..")
# yeah..thats it for today's calculator..feels free to experiment.