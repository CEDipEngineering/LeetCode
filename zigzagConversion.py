class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        if numRows == 2:
            return s[::2] + s[1::2]
        mat = [[] for _ in range(numRows)]
        string_index = 0
        mat_index = 0
        step = 1
        # Gather ZigZag pattern
        while string_index < len(s):
            mat[mat_index].append(s[string_index])
            # Alternate direction on edges
            if mat_index == numRows-1:
                step = -1
            elif mat_index == 0:
                step = 1
            mat_index += step
            string_index += 1
        # Concatenate strings
        out = ""
        for l in mat:
            out += "".join(l)
        return out

if __name__ == "__main__":
    S = Solution()
    print(S.convert("PAYPALISHIRING", 1))
    print(S.convert("PAYPALISHIRING", 2))
    print(S.convert("PAYPALISHIRING", 3))
    print(S.convert("PAYPALISHIRING", 4))