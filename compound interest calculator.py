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


# today i will be programming a compound interest calculator using python.

name = str(input("Please enter your name: "))
currency = input("Please enter the type of currency you wish to use,(e.g.Ksh, euros, pounds, dollar/$): ")
principle = 0
rate = 0
time = 0

while principle <= 0:
    principle = float(input("Enter the principle amount: "))
    if principle <= 0:
        print("Principle can not be less than or equal to zero")

while rate <= 0:
    rate = float(input("Enter the Interest rate: "))
    if rate <= 0:
        print("Interest rate can not be less than or equal to zero")

while time <= 0:
    time = int(input("Enter the time in years: "))
    if time <= 0:
        print("Time can not be less than or equal to zero")

total = principle * pow((1 + rate / 100), time)
print(f"Dear {name}, the balance after {time} year/s will be: {currency}{total}")