# Kevin and Stuart want to play the 'The Minion Game'.

# Game Rules

# Both players are given the same string, S.
# Both players have to make substrings using the letters of the string S.
# Stuart has to make words starting with consonants.
# Kevin has to make words starting with vowels. 
# The game ends when both players have made all possible substrings. 

# Scoring
# A player gets +1 point for each occurrence of the substring in the string S.

# For Example:
# String  = BANANA
# Kevin's vowel beginning word = ANA
# Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points. 

# consonant : 자음, vowel: 모음 = a, e, i, o, u

# the example that will be used: 'BANANA' 

vowel = ['A', 'E', 'I', 'O', 'U'] # make sure they are in uppercase


s = input()

stw_point = 0
kev_point = 0

# kev's points
# 1. string에서 첫번째로 발생하는 vowel의 index i 탐색
# 2. substring = string[i:l]
# 3. point = point + string에서 그 substring의 갯수
# 4. 다음 substring = 그 vowel~다음 letter
# 5. point = point + string에서 그 substring의 갯수
# 3~5 반복

def occurrences(string, sub): # use this function since string.count() only gives us non-overlapping counts
    count = start = 0
    while True:
        start = string.find(sub, start) + 1 # +1 since 맨 앞에 위치하면 start가 0이 되므로
        if start > 0:
            count+=1
        else:
            return count


# stw's points
# 1. string의 첫 글자가 vowel인지 구분
# 2. false면 subs 구성하여 단어 수 계산
# 3. true면 다음 letter로 이동하여 vowel인지 구분
# 4. 단어 내 모든 consonant에 대해서 적용되어야 함 e.g. banana 면 b와 n but only once for each consonant

# kev's points
# 1. string의 첫 글자가 vowel인지 구분
# 2. true면 subs 구성하여 단어 수 계산
# 3. false면 다음 letter로 이동하여 vowel 구분
# 4. 단어 내 모든 vowel에 대해 적용

startv_s = ''
startv_k = ''

# stw's point
for i in range(0,len(s)):
    if s[i] not in vowel:
        if s[i] != startv_s:
            startn_s = i
            startv_s = s[i]
            subs_s = str(startv_s)
            stw_point = stw_point + s.count(subs_s)

            for i in range(1, len(s)-startn_s):
                subs_s = subs_s + s[startn_s + i]
                stw_point = stw_point + occurrences(s, subs_s)

# kev's point
for i in range(0,len(s)):
    if s[i] in vowel:
        if s[i] != startv_k:
            startn_k = i
            startv_k = s[i]
            subs_k = str(startv_k)
            kev_point = kev_point + s.count(subs_k)

            for i in range(1, len(s)-startn_k):
                subs_k = subs_k + s[startn_k + i]
                kev_point = kev_point + occurrences(s, subs_k)

if stw_point > kev_point:
    print("Stuart {}".format(stw_point))
else: print("Kevin {}".format(kev_point))


# However, the whole code can be simplified as follows:

stw_sc, kev_sc = 0, 0
vowels = 'AEIOU' # make sure they are in uppercase
for i in range(0,len(s)):
    if s[i] in vowels:  
        kev_sc = kev_sc + len(s)-i 
    else:
        stw_sc = stw_sc + len(s)-i

print(stw_sc, kev_sc)