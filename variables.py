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
age = 22
name = "Lamar"
gpa = 4.0
online_status = True
food = ["burger", "Pizza", "traditional"]
user = {"name": "lamar", "gameID": "ID700605169"}
print(f"Scanning...online statues:{online_status}")
print(user)
print(f"Hello there, my name is {name},")
print(f"i am {age} of now.")
print(f"i know this is a joke but i imagine my gpa to be {gpa}.")
print("I am learning python to secure my chance as a AI Engineer")
print(f"i also enjoy eating {food}")
#the "f-string" makes life easier in programming.. no?