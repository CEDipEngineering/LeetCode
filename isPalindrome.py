import math

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0: return False
        if x==0: return True
        digit_at_i = lambda x, i: (x%(10**(i+1))//(10**(i)))
        nDigits = int(math.log10(x))+1
        for i,j in zip(range(nDigits), reversed(range(nDigits))):
            if j<i: break
            if digit_at_i(x, i) != digit_at_i(x,j): return False
        return True


if __name__ == "__main__":
    S = Solution()
    print_test = lambda x: print("{}:\t{}".format(x, S.isPalindrome(x)))

    print_test(121)
    print_test(21)
    print_test(1221)
    print_test(15751)
