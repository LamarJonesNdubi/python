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

# TODAY I WILL BE LEARNING ABOUT CONDITIONAL EXPRESSION
# conditional expression = A one-line sortcut for the is-else statement (ternary operator) 
#                          Print or assign one of two values based on a condition 
#                          X if condition else Y
#TEST1

number = 5

result = "High" if number > 0 else "Low"

print(result)

#TEST2

