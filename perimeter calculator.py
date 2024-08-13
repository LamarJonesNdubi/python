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
# today i will be coding a perimeter calculator using python
# alright lest start..
# perimiter of a rectangle is perimeter = 2(length + width)
# so it will look like this..

length = float(input("Enter your rectangle length: "))
width = float(input("Enter your rectangle width: "))

perimeter = 2 * (length + width)

print(f"Your rectangle perimeter is {perimeter} meters")

# Thats it for today...



