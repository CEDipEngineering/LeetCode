class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        if numRows == 2:
            return s[::2] + s[1::2]
        
        return s

if __name__ == "__main__":
    S = Solution()
    print(S.convert("PAYPALISHIRING", 1))
    print(S.convert("PAYPALISHIRING", 2))
    print(S.convert("PAYPALISHIRING", 3))
    print(S.convert("PAYPALISHIRING", 4))