import random

##################################################################################################
# Function: Return User Selection From a List
##################################################################################################
def ReturnSelection(lstSelections, strSelectionType):
    Selections = ""
    for item in lstSelections:
        Selections += item + ", "
    Selections = Selections[:-2] + "."
    Selection = input("Please select one of the following " + strSelectionType + ": " + Selections + " ")
    blnFound = False
    for item in lstSelections:
        if Selection in item:
            Selection = item
            blnFound = True
            break
    if not blnFound:
        return ""
    else:
        return Selection

##################################################################################################
# Function: Return Specific Brandname Color Selection
##################################################################################################
def ReturnSpecificColor(GenColor, PaintBrand):
    if PaintBrand == "Valspar/Behr":
        match GenColor:
            case "Grey":
                lstSpcColors = ["vbGrey1", "vbGrey2", "vbGrey3"]
            case "Green":
                lstSpcColors = ["vbGreen1", "vbGreen2", "vbGreen3"]
            case "Blue":
                lstSpcColors = ["Valspar Blissful Blue", 
                                "Valspar Lucy Blue", 
                                "Behr French Colony",
                                "Behr Watery",
                                "Behr Blueprint",
                                "Behr Blue Reflection",
                                "Valspar Memory Book Blue",
                                "Valspar Pacific Pleasure",
                                "Behr Oslo"]
    else:
        match GenColor:
            case "Grey":
                lstSpcColors = ["sbGrey1", "sbGrey2", "sbGrey3"]
            case "Green":
                lstSpcColors = ["sbGreen1", "sbGreen2", "sbGreen3"]
            case "Blue":
                lstSpcColors = ["sbBlue1", "sbBlue2", "sbBlue3"]
    
    random.shuffle(lstSpcColors)
    return lstSpcColors[0]


##################################################################################################
# Select Paint Brand
##################################################################################################
HighEndPaint = "Sherwin Williams/Benjamin Moore"
LowEndPaint = "Valspar/Behr"
PaintQuality = input("Please select 'Big Box' or 'Professional' brand paint. ")
PaintBrand = ""
if "Prof" in PaintQuality:
    PaintBrand = HighEndPaint
else:
    PaintBrand = LowEndPaint

print("Your selected Paint Brands will be: " + PaintBrand + ".")


##################################################################################################
# Select Room
##################################################################################################
lstRooms = ["Living Room", "Kitchen", "Dining Room", "Bedroom", "Bathroom", "Office"]
Room = ReturnSelection(lstRooms, "rooms")

if Room == "":
    print("Invalid Room Choice.")
else:
    print("Let's select a " + PaintBrand + " color for the " + Room + ".")


##################################################################################################
# Select General Color
##################################################################################################
lstGenColors = ["Grey", "Green", "Blue"]
GenColor = ReturnSelection(lstGenColors, "general colors")

if GenColor == "":
    print("Invalid General Color Choice.")
    exit()

##################################################################################################
# Select Specific Color
##################################################################################################
SpecficColor = ReturnSpecificColor(GenColor, PaintBrand)
print("Here's a specific " + PaintBrand + " " + GenColor + " color for the " + Room + ": " + SpecficColor)