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
# today i will be coding a weight convertor that coverts every weight units to user prefference

weight = float(input("Enter your weights: "))
unit = str(input("Kilograms-'non freedom' or Pounds-'freedom-democracy'? (K OR L): ")) # in CAPS LOCK

if unit == "K":
    weight = weight * 2.205
    unit = "Lbs"
    print("So..you have joined 'Freedom and Democracy'!")
    print(f"Your weight is: {round(weight, 1)}{unit}") 
elif unit == "L":
    weight = weight / 2.205
    unit = "Kgs"
    print("Sounds pretty Communist to me..")
    print(f"Your weight is: {round(weight, 1)}{unit}") 
else:
    print(f"{unit} was not valid")

