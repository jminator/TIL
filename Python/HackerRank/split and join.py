def split_and_join(line):
    newLine = line.split(" ")
    newLine = "-".join(newLine)
    return newLine

print(split_and_join("this is a string"))