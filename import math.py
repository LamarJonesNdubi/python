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
# TODAY I WILL BE CODING WITH THE HELP OF THE "IMPORT MATH" FUNCTION.


import math

print(math.pi) #will display the math formula of the pi
print(math.e)  #wull display the match formula of the E



