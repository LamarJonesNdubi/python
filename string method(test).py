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

# TODAY I WILL BE LEARNING STRINGS  METHODS IN PYTHON

# strings are long texts of words

#Test
# Validate user input exercise
#1. username is no more than 12 characters
#2. username must not contain spaces
#3. username must not contain digits

username = input("Enter your username: ")




if len(username) > 12:
    print("Your username can not be more than 12 characters.")
elif not username.find(" ") == -1:
    print("Your username can not contain spaces")        
else:
    print(f"welcome {username}")

