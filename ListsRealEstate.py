#Glen Labbe
#Professor Candido
#CIT-115
#Code Lists and Real Estate Analyzer
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
def getMedian(fPropertyList): #Create function to get median from user inputted sales.
    num = len(fPropertyList) #Count the number of user inputs in the list.
    if num % 2 == 1: #if num % 2 is equivalent to 1 then the number of lists is odd
        median = fPropertyList[num // 2] #Use integer division
        return median
    else:
        MiddleValue1 = fPropertyList[num // 2 - 1] #num // 2 - 1 finds index of the first middle value. For example, 4 indexes in a list // 2 = 2 - 1 which means index of first middle value is 1.
        MiddleValue2 = fPropertyList[num // 2] # num // 2 finds index of the second middle value
        return (MiddleValue1 + MiddleValue2) / 2 #add both middle values and divide by 2 to find median for even number of values in lisr

def getCommission(fPropertyList):
    TotalCommission = 0
    for num in fPropertyList: #create a loop to go through each property value.
        commission = num * 0.03 #multiply each num in list by .03
        TotalCommission += commission #add all commissions in list
    return TotalCommission
def main():
    fPropertyList = [] #create a list with no items
    while True: #use a loop to ask for user input
        fSalesPrice = getFloatInput("Enter property sales value: ")
        fPropertyList.append(fSalesPrice) #.append to add user input to list
        while True:
            AnotherValue = input("Enter another Value Y or N: ").upper()
            if AnotherValue == 'Y' or AnotherValue == "N":
                break
            else:
                print("Please enter Y or N.")

        if AnotherValue == "N":
            break

    fPropertyList.sort() #sort the list from lowest to highest order.

    PropertyNumber = 1
    for num in fPropertyList:
        print(f"Property {PropertyNumber}: ${num:,.2f} ")
        PropertyNumber += 1
    iMax = max(fPropertyList) #max function to find maximum value
    iMin = min(fPropertyList)#min function to find minimum value
    iSum= sum(fPropertyList)#sum function to find total value
    print(f"Maximum: ${iMax:,.2f}")
    print(f"Minimum: ${iMin:,.2f}")
    print(f"Total: ${iSum:,.2f}")
    median = getMedian(fPropertyList)
    print(f"Median: ${median:,.2f}")

    commission = getCommission(fPropertyList)
    print(f"Commission: ${commission:,.2f}")

main()
