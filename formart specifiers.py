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

#today i will be learning about format specifiers.

#formart specifiers = {:flags} format a value based on what flag are inserted.

# .(number)f = round to that many decimal places (fixed point)
# :(number)  = allocate that many spaces
# :03        = allocate and zero pad that many spaces
# :<         = left justified
# :>         = right justified
# :^         = centre justified
# :+         = use a plus sigh to indicate positive value 
# :=         = place sign to indicate positive value 
# :          = insert a space before positive value
# :,         = comma separator