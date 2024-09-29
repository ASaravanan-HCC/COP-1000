"""
This program calculates prices for custom house signs.
"""

# Declare and initialize variables here.
charge = 0.00           # Cost of the sign
numChars = 0            # Number of characters on the sign
color = "gold"          # Color of the characters
woodType = "oak"        # Type of wood


# Base charge
charge = 35.00

# Write assignment and if statements here as appropriate.

# Additional charge for characters beyond 5
if numChars > 5:
    charge += (numChars - 5) * 4

# Additional charge for wood type
if woodType == "oak":
    charge += 20.00

# Additional charge for color
if color == "gold":
    charge += 15.00
  
# Output Charge for this sign.
print("The charge for this sign is $" + str(charge))
