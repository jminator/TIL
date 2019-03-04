# Exercise 8.3
> '''Rewrite the guardian code in the above example without
two if statements. Instead, use a compound logical expression using
the and logical operator with a single if statement.'''

<pre>
fhand = open('mbox-short.txt')

fout = open('output.txt','w')
print(fout)

count = 0
for line in fhand:
	words = line.split()
	if len(words) < 2  or words[0] != 'From' : continue
	print(words[2])
	fout.write(words[2])

fout.close()
</pre>
