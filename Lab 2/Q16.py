mainString = input("Enter a String with letter 'a' : ")

brokenString = mainString.split("a")

print(brokenString[0] + "a")

i = 1

while i < len(brokenString):
    print(brokenString[i])
    i =  i + 1