# Exercise 4
>'''
Add code to the above program to figure out who has the
most messages in the file. After all the data has been read and the dic-
tionary has been created, look through the dictionary using a maximum
loop (see Chapter 5: Maximum and minimum loops) to find who has
the most messages and print how many messages the person has.

<pre>
fname = input('Entre file name:')

try:
    fhand = open(fname)
    print(fhand)
except:
    print('invalid file name')
    break

d = dict()

for line in fhand:
    line = line.rstrip()
    words = line.split()
    if len(words) < 2 : continue
    if words[0] != 'From' : continue
    d[(words[1])] = d.get((words[1]),0) +1

val_lst = list(d.values())

largest = 0
for i in d: # i = keys in the dictionary d
    if largest is 0 or d[i] > largest:
        largest = d[i]
        largest_entry = i

print(largest_entry, largest)
</pre>
