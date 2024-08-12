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




statues_online = True
item_for_sale = True
server_running = True
members_online = False
access = True

print("Running server URL..")
print("Routing secure portals to URL..")
print("Scanning for bridge breaks..")
print("Scanning for bridge injections..")
print("No bridge breaks or injections found..")
print("CONNECTION SECURE..")
print("Redirecting to destionation URL..")

print(f"Server active running statues: {server_running}")
print(f"Market place: Items availability verification: {item_for_sale}")
print(f"User available: {statues_online}")
print(f"User online active: {statues_online}")
print(f"Market Place memebers availability verification: {members_online}")

#just for fun..non of this is live or real..you are safe..
if access:
    print("Game over..we got you :)")
else:
    print("Smart..we invite you to the Squad")

