## Exercise 7.2

Write a program to prompt for a file name, and then read through the file and look for lines of the form:

X-DSPAM-Confidence: 0.8475

When you encounter a line that starts with “X-DSPAM-Confidence:” pull apart the line to extract the floating-point number on the line.

Count these lines and then compute the total of the spam confidence values from these lines. When you reach the end of the file, print out the average spam confidence.

<pre>
fname = input('Enter file name: ')
fhand = open(fname)

x = 0
sum = 0
count = 0

for line in fhand:
    line = line.rstrip()
    if line.find('X-DSPAM-Confidence: ') == -1: continue
    x_start = line.find(':')
    x_end = len(line)
    x = float(line[x_start+2:x_end])
    count = count +1
    sum = sum + x
    
print('Average spam confidence:', sum/count)
</pre>
