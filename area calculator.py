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
# Today i will be creating a simple calculator that calculates the area of a triangle

length = float(input("Enter the length of a rectangle: "))
width = float(input("Enter the width of a rectangle: "))

area = length * width

print(f"The area is {area}cm^2")