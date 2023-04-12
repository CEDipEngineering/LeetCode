class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        count = i = 0
        res = []
        for j, v in enumerate(s):
            count = count + 1 if v=='1' else count - 1
            if count == 0:
                res.append('1' + self.makeLargestSpecial(s[i + 1:j]) + '0')
                i = j + 1
        return ''.join(sorted(res)[::-1])

if __name__ == "__main__":
    S = Solution()
    print_test = lambda s: print("{} -> {}".format(s, S.makeLargestSpecial(s)))

    print_test("11011000") # "11100100"
    print_test("10") # 10