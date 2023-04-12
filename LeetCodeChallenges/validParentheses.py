class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in ['(', '[', '{']:
                stack.append(c)
                continue
            if len(stack) == 0: return False # Close before open
            for bracket, close in zip(['(', '[', '{'], [')', ']', '}']):
                if c == close:
                    if stack[-1] == bracket:
                        stack.pop()
                        break
                    else:
                        return False
        return len(stack) == 0
                    

if __name__ == "__main__":
    S = Solution()

    print_test = lambda s: print("{} : {}".format(s, S.isValid(s)))

    print_test(r"()[]{}")

    print_test(r"()")
    
    print_test(r"(]")
    