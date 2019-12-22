n = int(input())
s = set(map(int, input().split()))

nOrder = int(input())

for i in range(0, nOrder):
    order = input().split()

    if order[0] == 'remove':
        s.remove(int(order[1]))

    elif order[0] == 'discard':
        s.discard(int(order[1]))

    elif order[0] == 'pop':
        s.pop() # 맨 앞의 element 제거

print(sum(s))
        
