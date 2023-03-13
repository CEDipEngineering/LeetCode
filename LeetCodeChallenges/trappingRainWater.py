from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        """
        Function used to determine how much rain water the list of heights would trap.
        """
        if len(height) == 0: return 0
        def argmax(x):
            return max(range(len(x)), key=lambda i: x[i])

        max_i = argmax(height)
        water = 0
        k = 0
        for i, h in enumerate(height):
            if i == max_i: break
            if h > k:
                k = h
            water += k-h
        k = 0
        for i, h in enumerate(reversed(height)):
            if i == len(height)-max_i: break
            if h > k:
                k = h
            water += k-h        
        return water


if __name__ == "__main__":
    S = Solution()
    print_test = lambda x: print(f"{x}: {S.trap(x)}")
    print_test([9,2,1,4,5,3,8,1,2])#26
    print_test([9,2,1,4,5,3,9,1,2])#31