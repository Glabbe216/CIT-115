'''
#Glen Labbe
#Professor Candido
#CIT-115
#Compound Interest 10/11/24
# #fFV = fPrincipalValue * (1 + (fRate /fM)) **(fM * iTime)


#Convert variables
#Input
fPrincipalValue = float(input(f"Enter the starting principle: "))
fRate = float(input(f"Enter the annual interest rate: ")) / 100
iM = int(input(f"How many times per year is the interest compounded? "))
iTime = int(input(f"For how many years will the account earn interest? "))

#Do the math
#Logic
fFinalValue = fPrincipalValue * (1 + (fRate / iM)) ** (iM * iTime)

#Output
print (f"At the end of the {iTime} years you will have: ${fFinalValue:,.2f}")
'''
'''
for iNumber in range (1, 100):
    print(iNumber)
'''
iNumber = 1
while iNumber <= 100:
 print(iNumber)
 iNumber += 1

