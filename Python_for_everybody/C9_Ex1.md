# Exercise 9.1

>''' Write a program that reads the words in words.txt and stores them as
keys in a dictionary. It doesn’t matter what the values are. Then you
can use the in operator as a fast way to check whether a string is in the
dictionary.
'''
<pre>
fhand = open('words.txt')

a_list = dict()

for line in fhand:
    line = line.rstrip()
    words = line.split()
    if len(words) < 1 : continue
    for word in words:
        a_list[word] = word
print(a_list)


if 'Python' in a_list:
    print('True')
else:
    print('False')
</pre>
