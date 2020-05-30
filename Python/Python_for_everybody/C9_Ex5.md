# Exercise 5
>'''
This program records the domain name (instead of the
address) where the message was sent from instead of who the mail came
from (i.e., the whole email address). At the end of the program, print
out the contents of your dictionary.

<pre>
fhand = open('mbox-short.txt')
d = dict()
a_list = list()
domain = list()

for line in fhand:
    line = line.rstrip()
    words = line.split()
    if len(words) < 2 : continue
    if words[0] != 'From' : continue
    a_list.append(words[1])

for address in a_list:
    domain_start = address.find('@')
    domain_end = len(address)
    domain.append(str(address[domain_start+1:domain_end]))

for i in domain:
    d[i] = d.get(i,0) +1
print(d)
</pre>
