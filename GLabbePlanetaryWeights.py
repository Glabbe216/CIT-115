#Glen Labbe
#CIT-115L-D01
#Professor Candido
#Planetary Weights Assignment 10/02/24

#Constants
fMERCURY_CONV = .38
fVENUS_CONV = .91
fMOON_CONV = .165
fMARS_CONV = .38
fJUPITER_CONV = 2.34
fSATURN_CONV = .93
fURANUS_CONV = .92
fNEPTUNE_CONV = 1.12
fPLUTO_CONV = .066

#input
sName = input("What is your name? ")
fYourWeight = float(input(f"{sName}, How much do you weigh? "))

#calculate

fMercury = fYourWeight * fMERCURY_CONV
fVenus = fYourWeight * fVENUS_CONV
fMoon = fYourWeight * fMOON_CONV
fMars = fYourWeight * fMARS_CONV
fJupiter = fYourWeight * fJUPITER_CONV
fSaturn = fYourWeight * fSATURN_CONV
fUranus = fYourWeight * fURANUS_CONV
fNeptune = fYourWeight * fNEPTUNE_CONV
fPluto = fYourWeight * fPLUTO_CONV

#Output
print(f"Hello, {sName}! Here are your weights on our Solar System's planets")
print(f"{'Weight on Mercury:':20s}{fMercury:20,.2f}")
print(f"{'Weight on Venus:':20s}{fVenus:20,.2f}")
print(f"{'Weight on our Moon:':20s}{fMoon:20,.2f}")
print(f"{'Weight on Mars:':20s}{fMars:20,.2f}")
print(f"{'Weight on Jupiter:':20s}{fJupiter:20,.2f} ")
print(f"{'Weight on Saturn:':20s}{fSaturn:20,.2f}")
print(f"{'Weight on Uranus:':20s}{fUranus:20,.2f}")
print(f"{'Weight on Neptune:':20s}{fNeptune:20,.2f}")
print(f"{'Weight on Pluto:':20s}{fPluto:20,.2f}")





