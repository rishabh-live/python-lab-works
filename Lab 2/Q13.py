centimeterInput = int(input("Enter Centimeter(s) : "))
if centimeterInput < 0:
    print("Invalid Entry !!")
else:
    inch = 2.54 * centimeterInput
    print(f'{centimeterInput} cm. = {inch}')