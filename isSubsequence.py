class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0: return True
        if len(t) == 0: return False
        index = 0
        for i in range(len(t)):
            if t[i] == s[index]:
                if index == len(s) - 1: return True
                index += 1
        return False

if __name__ == "__main__":
    S = Solution()
    print(S.isSubsequence("acb", "ahbgdc"))
    print(S.isSubsequence("bgc", "ahbgdc"))
    print(S.isSubsequence("abc", "ahbgdc"))