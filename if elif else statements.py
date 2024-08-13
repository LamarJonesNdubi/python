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
# TODAY I WILL BE LEARNING ABOUT THE IF, ELSE ELIF STATEMENTS

# if = it does some code only if some conditions is true
#       ELSE do something else

name = str(input("Please enter your name: "))
age = int(input(f"Hello {name} please tell me your age: "))

if age >= 18:
    print(f"Nice...that is nice {name}, we can be friends then :)")
elif age < 0:
    print("Not born")    
else:
    print(f"@{name} Rap with me:....Tryna strike a chord and it's probably A-Minor") 
    print("They not like us, they not like us, they not like us")   
