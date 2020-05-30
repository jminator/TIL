


def swap_cases(string):
    newString = str()
    for i in string:
        if i.islower() == True:
            newString = newString + i.upper()
        elif i.isupper() == True:
            newString = newString + i.lower()
        else: newString = newString + i
    return newString

print(swap_cases("Hello, World"))