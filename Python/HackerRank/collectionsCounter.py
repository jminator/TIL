shoeNumber = int(input())
shoeSizes = input().split(" ")
customerCount = int(input())
income = 0

while customerCount > 0:
    size, pay = input().split(" ")
    if size in shoeSizes :
        shoeSizes.remove(size)
        income = income + int(pay)
        customerCount -= 1
    else :
        customerCount -= 1

print(income)

# which is the same as:

# from collections import Counter
# numShoes = int(input())
# shoeSizes = Counter(map(int,input().split()))
# numCustomers = int(input())
# totalIncome = []

# for i in range(numCustomers):
#     size, pay = map(int,input().split())
#     if shoeSizes[size] > 0:
#         totalIncome.append(pay)
#         shoeSizes.subtract(Counter([size]))

# print (sum(totalIncome))