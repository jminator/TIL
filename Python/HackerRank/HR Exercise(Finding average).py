a = list([[50., 60., 70.],[56.,78.,98.],[34.,78.,66.]])

name = list(["a","b","c"])
d = dict({"a":a[0], "b":a[1], "c":a[2]})

print(d)

input_name = input("input name:")

ans = d[input_name]  # this is a list

average_a = sum(ans) / len(ans)

print(average_a)
    