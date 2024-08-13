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
# Today i will be coding a mad libs game that allows the user to come up with a story based on the input.
# Before you start the game "for anyone who atually viewing my code: thank you" i know most of you English is not..
#  your national language..same here..but u made some notes to use:....
# .Here’s a breakdown of adjectives, nouns, and verbs with examples:

#   - **Example**: "Beautiful," "fast," "happy"

# 1. Adjective: A word that describes or modifies a noun.
#Example: "Beautiful," "fast," "happy"
#Sentence: The beautiful sunset painted the sky in vibrant colors.

# 2. **Noun**: A word that represents a person, place, thing, or idea.
#   - **Example**: "Dog," "city," "happiness"
#   - **Sentence**: The **dog** barked loudly at the stranger.

#3. **Verb**: A word that expresses an action, occurrence, or state of being.
#   - **Example**: "Run," "think," "is"
##   - **Sentence**: She **runs** every morning to stay fit.

#In the sentence "The beautiful sunset painted the sky in vibrant colors":
#- "Beautiful" is an adjective describing the noun "sunset."
#- "Sunset" is a noun.
#- "Painted" is a verb indicating the action.
# HOPE THAT HELPED..


adjective1 = input("Enter an adjective: ")
noun = input("Enter a noun: ")
adjective2 = input("Enter an adjective: ")
verb = input("Enter a verb: ")
adjective3 = input("Enter and adjective: ")

print(f"Today i went to a {adjective1} zoo")
print(f"In an exhibit, i saw a {noun}")
print(f"{noun} was {adjective2} and {verb}ing")
print(f"i was {adjective3}")