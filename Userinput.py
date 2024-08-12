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

# [today i will be trying to code a user input and make it accept user input as well.
# we an have the 'name' valerable to store the name instead.
# since i am using a vscode editor it seems i cant input my name in the output box..
# unless you click the 'down arrow' on your right next to the execution button.
# and and click "run python file" instead of "run code".
# in this lesson of creating the use input via the terminal we can learn that each imput..
# has to be identified by the data type they represent in order to function]

print("Hello There..please be patient as i gather data form for you.")
name = str(input("Enter your name: "))
age = int(input("Enter your age: "))
print(f"Nice to see you {name} its been a long time.")
print(f"You are {age} years of age.")