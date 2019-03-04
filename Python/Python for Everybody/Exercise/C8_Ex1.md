# Exercise 8.6

> Rewrite the program that prompts the user for a list of </br>
numbers and prints out the maximum and minimum of the numbers at </br>
the end when the user enters “done”. Write the program to store the </br>
numbers the user enters in a list and use the max() and min() functions to </br>
compute the maximum and minimum numbers after the loop completes. </br>

<pre>
a_list = list()

while True:
    key_in = input('Enter a number:')

    if key_in == 'done':
        print('Maximum:',max(a_list))
        print('Minimum:',min(a_list))
        break
    try:
        a_list.append(int(key_in))

    except:
        print('invalid input')
        continue
</pre>
