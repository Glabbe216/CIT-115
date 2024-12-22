# Glen Labbe
# Professor Candido
# CIT-115
# Grade Analyzer
# 10/28/24

# Input and conversions
sName = input("Name of person we are calculating grades for: ")
iTest1 = int(input("Test 1: "))
iTest2 = int(input("Test 2: "))
iTest3 = int(input("Test 3: "))
iTest4 = int(input("Test 4: "))
sYorN = input("Do you wish to drop the lowest grade Y or N? ").upper()

# Logic
if iTest1 <= 0 or iTest2 <= 0 or iTest3 <= 0 or iTest4 <= 0:
    raise SystemExit("Test scores must be > 0")

if sYorN != "Y" and sYorN != "N":
    raise SystemExit("Enter Y or N to drop the lowest grade")

LowestGrade = 0

if sYorN == "Y":
    if iTest1 < iTest2 and iTest1 < iTest3 and iTest1 < iTest4:
        LowestGrade = iTest1
    elif iTest2 < iTest3 and iTest2 < iTest4:
        LowestGrade = iTest2
    elif iTest3 < iTest4:
        LowestGrade = iTest3
    else:
        LowestGrade = iTest4
if LowestGrade != 0:
    fFinalGrade = (iTest1 + iTest2 + iTest3 + iTest4 - LowestGrade) / 3
else: 
    fFinalGrade = (iTest1 + iTest2 + iTest3 + iTest4) / 4
    

LetterGrade = ""
if fFinalGrade <= 59.9:
    LetterGrade = "F"
elif fFinalGrade <= 63.9:
    LetterGrade = "D-"
elif fFinalGrade <= 66.9:
    LetterGrade = "D"
elif fFinalGrade <= 69.9:
    LetterGrade = "D+"
elif fFinalGrade <= 73.9:
    LetterGrade = "C-"
elif fFinalGrade <= 76.9:
    LetterGrade = "C"
elif fFinalGrade <= 79.9:
    LetterGrade = "C+"
elif fFinalGrade <= 83.9:
    LetterGrade = "B-"
elif fFinalGrade <= 86.9:
    LetterGrade = "B"
elif fFinalGrade <= 89.9:
    LetterGrade = "B+"
elif fFinalGrade <= 93.9:
    LetterGrade = "A-"
elif fFinalGrade <= 96.9:
    LetterGrade = "A"
else:
    LetterGrade = "A+"

# Output
print(f"{sName} test average is: {fFinalGrade:.1f}")
print(f"Letter Grade for the test is: {LetterGrade}")


