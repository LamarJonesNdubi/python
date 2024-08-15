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

# Today i will be coding the temperature converter which conversts temperature to any unit available

unit = str(input("Is this temperature in Celsius or Fahrenheit (C/F): "))
temp = float(input(" Enter the temperature: "))

if unit == "C":
    answer = round((temp * 9/5) + 32, 1)
    print(f"the temperature is {answer} Fahrenheit")
elif unit == "F":
    answer = round((temp - 32) * 5/9, 1)
    print(f"the temperature is {answer} Celcius")
else:
    print(f"this '{unit}' is an Invalid unit of measurement.")


