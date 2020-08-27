def countString(str):
    print("String: ", str)
    count = 0
    for i in range(len(str) - 1):
        count += str[i: i + 4] == 'Emma'
    return count

count = countString("Emma is good developer. Emma is a writer")
print("Emma appeared : ", count, "times")