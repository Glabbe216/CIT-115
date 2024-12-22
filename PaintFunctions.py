#Glen Labbe
#Professor Candido
#CIT-115
#Paint Functions

import math

def getFloatInput(sPrompt): #Convert input to float and make sure user inputs positive numeric value.
    iVal = 0
    while True:
        try:
            iVal = float(input(f"{sPrompt}"))
            if iVal > 0:
                break
            else:
                print("Please provide a positive number.")
        except ValueError:
            print("Please provide a valid numeric value.")
    return iVal

def getGallonsOfPaint(fSqFt, fFeetPerGal): #Divide SqFt by FeetPerGal to get gallons of paint needed
    iGallonsOfPaint = fSqFt / fFeetPerGal
    iGallonsOfPaint = math.ceil(iGallonsOfPaint) #Round Gallons of paint needed up
    print(f"Gallons of paint needed: {iGallonsOfPaint:}")
    return iGallonsOfPaint

#Multiply Labor Hours by Gallons of paint needs to find how long the job will take
def getLaborHours(fLaborHours, iGallonsOfPaint):
    fHoursOfLabor = fLaborHours * iGallonsOfPaint
    print(f"Hours of Labor: {fHoursOfLabor:,.1f}")

#Multiply Labor hours by Labor charge and gallons of paint to find the cost
def getLaborCost(fLaborHours, fLaborCharge, iGallonsOfPaint):
    fCostOfLabor = fLaborHours * fLaborCharge * iGallonsOfPaint
    print(f"Labor Charges: ${fCostOfLabor:,.2f}")
    return fCostOfLabor

#Multiply Gallons of paint by paint price to find total paint cost
def getPaintCost(iGallonsOfPaint, fPaintPrice):
    fTotalPaintCost = iGallonsOfPaint * fPaintPrice
    print(f"Paint Charges: ${fTotalPaintCost:,.2f}")
    return fTotalPaintCost

# if/elif statements to find tax rate for each of the states listed
def getSalesTax(JobState, fTotalPaintCost, fCostOfLabor):
    fTaxRate = 0

    if JobState == "MA":
        fTaxRate = 0.0625
        fTaxAmount = (fTotalPaintCost + fCostOfLabor) * fTaxRate
        print(f"Tax for MA: ${fTaxAmount:,.2f}")
    elif JobState == "CT":
        fTaxRate = 0.06
        fTaxAmount = (fTotalPaintCost + fCostOfLabor) * fTaxRate
        print(f"Tax for CT: ${fTaxAmount:,.2f}")
    elif JobState == "ME":
        fTaxRate = 0.085
        fTaxAmount = (fTotalPaintCost + fCostOfLabor) * fTaxRate
        print(f"Tax for ME: ${fTaxAmount:,.2f}")
    elif JobState == "NH":
        fTaxRate = 0.0
        fTaxAmount = (fTotalPaintCost + fCostOfLabor) * fTaxRate
        print(f"Tax for NH: ${fTaxAmount:,.2f}")
    elif JobState == "RI":
        fTaxRate = 0.07
        fTaxAmount = (fTotalPaintCost + fCostOfLabor) * fTaxRate
        print(f"Tax for RI: ${fTaxAmount:,.2f}")
    elif JobState == "VT":
        fTaxRate = 0.06
        fTaxAmount = (fTotalPaintCost + fCostOfLabor) * fTaxRate
        print(f"Tax for VT: ${fTaxAmount:,.2f}")
    else:
        print("Tax rate is 0.")
    return fTaxAmount

#add Cost of labor and total paint cost and tax amount to find the Total cost of the whole project
def showCostEstimate(fTaxAmount, fTotalPaintCost, fCostOfLabor):
    fTotalCost = (fCostOfLabor + fTotalPaintCost) + fTaxAmount
    print(f"Total cost: ${fTotalCost:,.2f}")
    return fTotalCost


#Logic and inputs and create a file
def main():
    fSqFt = getFloatInput(f"Enter Wall Space in Square feet: ")

    fPaintPrice = getFloatInput("Enter paint price per gallon: ")

    fFeetPerGal = getFloatInput("Enter feet per gallon: ")

    fLaborHours = getFloatInput("How many labor hours per gallon: ")

    fLaborCharge = getFloatInput("Labor charge per hour: ")

    JobState = input("State the job is in: ")

    LastName = input("Customer last name: ")


    iGallonsOfPaint = getGallonsOfPaint(fSqFt, fFeetPerGal)

    getLaborHours(fLaborHours, iGallonsOfPaint)

    fTotalPaintCost = getPaintCost(iGallonsOfPaint, fPaintPrice)

    fCostOfLabor = getLaborCost(fLaborHours, fLaborCharge, iGallonsOfPaint)

    fTaxAmount = getSalesTax(JobState, fTotalPaintCost, fCostOfLabor)

    fTotalCost = showCostEstimate(fTaxAmount, fTotalPaintCost, fCostOfLabor)

    FileName = (f"{LastName}_PaintJobOutput.txt")

    with open(FileName, 'w') as OfInfo:
        OfInfo.write(f"{iGallonsOfPaint}\n")
        OfInfo.write(f"${fTotalPaintCost:,.2f}\n")
        OfInfo.write(f"${fCostOfLabor:,.2f}\n")
        OfInfo.write(f"${fTaxAmount:,.2f}\n")
        OfInfo.write(f"${fTotalCost:,.2f}\n")

    print(f"File: {FileName} was created.")

main()















