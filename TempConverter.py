#Glen Labbe
#Professor Candido
#CIT-115
#Temperature Converter 10/16/24

#input
print("Welcome to Glen's Temperature Converter")
fTemp = float(input("Enter a temperature: "))
sForC = input(f"Is the Temperature F for Fahrenheit or C for Celsius?: ").upper()

USER_ENTERED_TEMP = fTemp



#if statements
if sForC != "F" and sForC != "C":
     raise SystemExit ("Enter an F or C")

if sForC == "F":
    if fTemp > 212:
        raise SystemExit("Temp can't be > than 212")
    else:
        fConvertTemp = (5.0 / 9) * (USER_ENTERED_TEMP - 32)
        print(f"The Celsius equivalent is {fConvertTemp:.1f}")

else:
    if fTemp > 100:
        raise SystemExit("Temp can't be > than 100")
    else:
        fConvertTemp = ((9.0/5.0) * USER_ENTERED_TEMP) + 32
        print(f"The Fahrenheit equivalent is {fConvertTemp:.1f}")





















