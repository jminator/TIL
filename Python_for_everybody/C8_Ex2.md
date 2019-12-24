# Exercise 8.2

>'''Figure out which line of the above program is still not properly
guarded. See if you can construct a text file which causes the program to fail
and then modify the program so that the line is properly guarded and test it to
make sure it handles your new text file.'''

<pre>
# there may be lines with less than 2 words

fhand = open('mbox-short.txt')

fout = open('output.txt','w')
print(fout)

count = 0
for line in fhand:
	words = line.split()
	if len(words) < 2 : continue
	if words[0] != 'From' : continue

	fout.write(words[2])

fout.close()
</pre>
