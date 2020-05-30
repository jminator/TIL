def mutate_string(string, position, character):
    newString = list(string)
    i = int(position)
    newString[i - 1] = character
    newString = "".join(newString)
    return newString


string = input()
position, character = input().split()

print(mutate_string(string, position, character))