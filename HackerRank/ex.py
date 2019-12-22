from fractions import Fraction
from functools import reduce

def product(fracs):
    t = reduce(lambda x, y : Fraction(x * y), fracs)
    return t.numerator, t.denominator

if __name__ == '__main__':

    entries = int(input())
    fracs =[]
    
    for _ in range(entries):
        fracs.append(Fraction(*map(int, input().split())))
    result = product(fracs)
    print(*result)  # *은 unpacking에 사용
    # https://mingrammer.com/understanding-the-asterisk-of-python/ 참고

    # for i in range(0, entries):
    #     nums = list(map(int, input().split(" ")))
    #     frac = Fraction(nums[0], nums[1])
    #     fracs.append(frac)

    # a, b = product(fracs)
    # print('%d %d' % (a, b))

