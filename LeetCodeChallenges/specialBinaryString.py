class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        cumSum = [0]*len(s)
        def conv(c: str):
            if c == "1": return 1
            return -1
        
        for i, e in enumerate(s):
            if i == 0: cumSum[i] = conv(e)         
            else:
                cumSum[i] = cumSum[i-1] + conv(e)
        
        return cumSum

if __name__ == "__main__":
    S = Solution()
    print_test = lambda s: print("{} -> {}".format(s, S.makeLargestSpecial(s)))

    print_test("11011000") # "11100100"
    print_test("10") # 10