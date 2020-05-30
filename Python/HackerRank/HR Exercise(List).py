if __name__ == '__main__':
    N = int(input())

lst = []
i = 0


while i < N:

    call_id = input().split(" ")

    if call_id[0] == "insert":
        lst.insert(int(call_id[1]), int(call_id[2]))
    elif call_id[0] == "remove":
        lst.remove(int(call_id[1]))
    elif call_id[0] == "pop":
        lst.pop()
    elif call_id[0] == "sort":
        lst.sort()
    elif call_id[0] == "reverse":
        lst.reverse()
    elif call_id[0] == "append":
        lst.append(int(call_id[1]))
    elif call_id[0] == "print":
        print(lst)
    i = i + 1

