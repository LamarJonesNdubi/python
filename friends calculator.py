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

# an input / a calculator to calculate friends.
# this is more like a "miserable-life calculator"

name = str(input("Please enter your name: "))
friends = int(input(f"Hello {name}, How many friends do you have?: "))
print(f"i see you have {friends}, my programmer 'Lamar' has fewer that that.")



