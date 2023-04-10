class Solution:

    # def convert(self, string):
    #     out = ""
    #     for s in string:
    #         if s == '0':
    #             out += "01"
    #         else:
    #             out += "10"
    #     return out

    def kthGrammar(self, n: int, k: int) -> int:
        # s = "0"
        # for i in range(n):
        #     s = self.convert(s)
        # return s[k-1]
        return bin(k - 1).count('1') & 1
    
if __name__ == "__main__":
    S = Solution()
    print_test = lambda n, k: print("({}, {}) => {}".format(n, k, S.kthGrammar(n, k)))

    print_test(1,1)
    print_test(2,1)
    print_test(1000,30)