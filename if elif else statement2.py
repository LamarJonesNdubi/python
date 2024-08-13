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

name = str(input("Please let me know your name: "))
age = int(input(F"Hello {name}, please let mek know your age as well: "))

if age >= 18:
    print(f"Nice, you can drive now @{name}")
elif age < 0:
    print("You havent been born yet.")       
else:
    print("may i suggest buying a driving gaming gear for practise as you wait to age")    