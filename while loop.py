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

# today i will be learning about while loops

# while loop = execute some code WHILE some condition remains true

name = input("Enter your name: ")

#if name == "":
#    print("you did not enter your name")
#else:
#    print(f"Hello {name}")    

while name == "":
    print("you did not enter your name")
    name = input("Enter your name: ")

print(f"Hello {name} nice to meet you :)")    