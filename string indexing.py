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
# Today i will be learning about string indexing in python

# indexing = accessing elements of a sequence using [] (indexing operator)
#            [start : end : step]

credit_number = "1234-5678-9012-3456" # not an actual credit card number of-course :)

print(credit_number[0])      #the counting in machines always start from 0..so here 0 will be 1 in the credit number.
print(credit_number[:4])     #the :4 the machine assumes the missing number before : is the start
print(credit_number[3])
print(credit_number[:7])
print(credit_number[0:15])   #i think it includes the - in the count as well 
print(credit_number[4:])
print(credit_number[-2])     #it looks like when using a negative number the machine counts backwards without starting from 0.
print(credit_number[-5])
print(credit_number[-8])
print(credit_number[::2])    #here we will be using the 'step' part of the indexing. it will count and print any number skipped from 2.
print(credit_number[::3])    #it seems like the counting always start witht he first digit in the credit card number.

#now lets create a programme that displays the last four digits of the credit card number.

last_four_digits = credit_number[-4:]
print(f"XXXX-XXXX-XXXX-{last_four_digits}") #i used the 'XXXX-XXXX-XXXX' to mimik the hidden digits in every verification platform and to hide
                                            #the rest of the numbers.

#now lets programme the numbers in the credit card to revearse

revearsed_credit_number = credit_number[::-1]

print(revearsed_credit_number)