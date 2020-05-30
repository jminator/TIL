# A valid credit card from ABCD Bank has the following characteristics: 

# ► It must only consist of digits (0-9). check
# ► It must start with a 4, 5 or 6. check
# ► It must contain exactly 16 digits. check
# ► It may have digits in groups of 4, separated by one hyphen "-". check
# ► It must NOT use any other separator like ' ' , '_', etc. check
# ► It must NOT have 4 or more consecutive repeated digits.

# 4567-9876-9866-9574
# 456-79876-9866-9574


# Instruction: input 6 credit card numbers,
# validate each of them and label 'Valid' or 'Invalid'


# test 2: start with 4, 5, or 6
def test1(inputno):
    testlist = [4, 5, 6]
    digit = int(inputno[0])
    if digit in testlist :
        continue
    else: 
        print("Invalid")
        exit()

inputno = input()
allowed = [0,1,2,3,4,5,6,7,8,9,"-"]
allowed = list(map(str, allowed))

# test1: only consists of 0-9
print("test 1 initiated")
for i in range(0,len(inputno)):
    if inputno[i] not in allowed :
        print("Invalid")
        exit()
print("test 1 success")

newlst = []
for i in range(0, len(inputno)):
    if inputno[i] != "-":
        newlst.append(inputno[i])

test1(inputno)

# test 3: exactly 16 digits
print("test 3 initiated")
if len(newlst) == 16:
    print("test 3 success")

print("test 4 initiated")
for i in range(0, len(inputno)):
    if inputno[i] == "-":
        splitlst = inputno.split("-")
        for j in range(0,len(splitlst)):
            if len(splitlst[j]) == 4: continue
            else : 
                print("Invalid")
                exit()
    else: continue
    print("test 4 success")

# test 5 : must not have more than 4 consecutive digits
# 0-9까지 각 digit의 substring(iiii) 만들어서
# inputno에서 해당 substring 찾을 수 있는지 검사
print("test 5 initiated")
for i in range(0,len(inputno)):
    t = inputno[i]
    sstr = "".join(map(str,[t, t, t, t]))
    index = inputno.find(sstr, 0, len(inputno))
    if index >= 1:
        print("Invalid")
        exit()
    
