from typing import List

class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        r, c = set(), set()
        for i in arr:
            c = {i | j for j in c} | {i}
            r |= c
        return len(r)

if __name__ == "__main__":
    S = Solution()
    print_test = lambda arr: print("{}: {}".format(arr, S.subarrayBitwiseORs(arr)))

    print_test([1,1,2])
    print_test([1,2,4])
    print_test([3])
    # print_test(list(range(100)))
    