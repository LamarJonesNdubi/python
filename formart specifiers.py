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

#formart specifiers = {value:flags} format a value based on what flag are inserted.

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




# using the .(number)f "round to that many decimal places"
price1 = 3.14159
price2 = -987.65
price3 = 12.34

print(f"Price 1 is Ksh{price1:.2f}")
print(f"Price 2 is Ksh{price2:.2f}")
print(f"Price 3 is Ksh{price3:.2f}")




# using the :(number) "allocate that many space"
price1 = 3.14159
price2 = -987.65
price3 = 12.34

print(f"Price 1 is Ksh{price1:10}")
print(f"Price 2 is Ksh{price2:10}")
print(f"Price 3 is Ksh{price3:10}")




# using the :03 "allocate and zero pad that many space"
price1 = 3.14159
price2 = -987.65
price3 = 12.34

print(f"Price 1 is Ksh{price1:010}")
print(f"Price 2 is Ksh{price2:010}")
print(f"Price 3 is Ksh{price3:010}")



# using the :< "left justified"
price1 = 3.14159
price2 = -987.65
price3 = 12.34

print(f"Price 1 is Ksh{price1:010}")
print(f"Price 2 is Ksh{price2:010}")
print(f"Price 3 is Ksh{price3:010}")
