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
# today i will be programming a age calculator that uses the user's birth year and current year input.

name = str(input("Enter your name: "))
current_year = int(input("Enter the current year e.g 2024: "))
birth_year = int(input("Enter your year of birth: "))

if current_year > birth_year:
    result = current_year - birth_year
    print(f"Dear {name} you are {result} years old.") 
else:
    print(f"Are you Time travelling {name}?")

   