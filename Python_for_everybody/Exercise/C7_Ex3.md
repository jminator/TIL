## Exercise 7.3

Sometimes when programmers get bored or want to have a
bit of fun, they add a harmless Easter Egg to their program. 

Modify the program that prompts the user for the file name so that it prints a
funny message when the user types in the exact file name “na na boo
boo”. 

The program should behave normally for all other files which
exist and don’t exist. Here is a sample execution of the program:

> python egg.py <br/>
> Enter the file name: mbox.txt<br/>
> There were 1797 subject lines in mbox.txt<br/>

> python egg.py<br/>
> Enter the file name: missing.tyxt<br/>
> File cannot be opened: missing.tyxt<br/>

> python egg.py<br/>
> Enter the file name: na na boo boo<br/>
> NA NA BOO BOO TO YOU - You have been punk'd!<br/>

<pre>
fname = input('Enter file name: ')

try:
    if fname == 'na na boo boo':
        print("NA NA BOO BOO TO YOU - You have been punk'd!")
        exit()
    else:
        fhand = open(fname)

except:
    print('file cannot be opened:',fname)
    exit()

count = 0

for line in fhand:
    line = line.rstrip()
    count = count +1

print('There were %d subject lines in %s' % (count, fname))

</pre>
