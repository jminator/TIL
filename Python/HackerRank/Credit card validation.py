# A valid credit card from ABCD Bank has the following characteristics: 

# ► It must only consist of digits (0-9). check
# ► It must start with a 4, 5 or 6. check
# ► It must contain exactly 16 digits. check
# ► It may have digits in groups of 4, separated by one hyphen "-". check
# ► It must NOT use any other separator like ' ' , '_', etc. check
# ► It must NOT have 4 or more consecutive repeated digits.


# Instruction: input 6 credit card numbers,
# validate each of them and label 'Valid' or 'Invalid'

# sample input
# 6
# 4123456789123456
# 5123-4567-8912-3456
# 61234-567-8912-3456
# 4123356789123456
# 5133-3367-8912-3456
# 5123 - 3567 - 8912 - 3456

# test1: only consists of 0-9:
def testdigit(card):
    allowed = list(map(str, [0,1,2,3,4,5,6,7,8,9,"-"]))
    for i in range(0, len(card)):
        if card[i] not in allowed:
            return 1
        else: continue
    return 0

# test2: the first number starts with 4, 5, or 6
def test456(card):
    digit = int(card[0])
    testlist = [4, 5, 6]
    if digit in testlist :
        return 0
    else: 
        return 1

# test 3: exactly 16 digits:
def test16(card):
    strip_hyp = "".join(card.split("-"))
    if len(strip_hyp) == 16:
        return 0
    else: 
        return 1

# test 4: combination of 4 numbers
def test4comb(card):
    for i in range(0, len(card)):
        if card[i] == "-":
            splitlst = card.split("-")
            for j in range(0,len(splitlst)):
                if len(splitlst[j]) == 4: 
                    continue
                else : 
                    return 1
        else: continue
    return 0

# test 5: must not have more than 4 consecutive digits:
def testcons(card):
    strip_hyp = "".join(map(str, card.split("-")))
    for i in range(0, len(strip_hyp)):
        t = strip_hyp[i]
        sstr = "".join(map(str,[t, t, t, t]))
        index = strip_hyp.find(sstr, 0, len(strip_hyp))
        if index >= 1:
            return 1
        else:
            continue
    return 0

# main 
def main():
    entries = int(input())
    cards = []
    results = 0
    outputs =[]

    for i in range(0,entries):
            cards.append(input())

    for card in cards:
        results = testdigit(card) + test456(card) + test16(card) + test4comb(card) + testcons(card)
        if results > 0:
            outputs.append("Invalid")
        else:
            outputs.append("Valid")

    print(*outputs, sep='\n')

main()