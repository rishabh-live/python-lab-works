stringOne = input("Enter First String : ")
stringTwo = input("Enter Second String : ")
finalString = ""
if len(stringOne) == len(stringTwo):
    i = 0
    while i < len(stringOne):
        finalString = finalString + stringOne[i] + stringTwo[i]
        i = i + 1
    print(f'Final String is : {finalString}')
else:
    print("String are not equal")