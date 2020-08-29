theString = input("Enter a String : ")

print(f'1) No. of characters in the string : {len(theString)}')

print(f'2) The String repeated 10 Times : ')

i = 0
while i < 10:
    print(f'\tPrinting {theString} {i + 1} time') 
    i = i + 1


print(f'3) First Character of the string is : {theString[0]}')
print(f'4) First Three Characters of the String are : {theString[0:3]}')
print(f'5) Last Three Characters of the String are : {theString[-3:]}')
print(f'6) The string backwards is : {theString[::-1]}')

if len(theString) >= 7:
    print(f'7) {theString} is Seven Characters or More !!')
else:
    print(f'7) {theString} is less than Seven Characters !!')

print(f'8) First and Last Characters removed from the string : {theString[1:-1]}')
print(f'9) String is All Caps : {theString.upper()}')
print(f'10) The string with every a replaced with an e : {theString.replace("a","e")}')
print(f'11) The string replaced with a Space : {theString.replace(theString," ")}')
