from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.append(0)
        n = len(nums)
        for i in range(len(nums)): #delete those useless elements
            if nums[i]<0 or nums[i]>=n:
                nums[i]=0
        for i in range(len(nums)): #use the index as the hash to record the frequency of each number
            nums[nums[i]%n]+=n
        for i in range(1,len(nums)):
            if nums[i]//n==0:
                return i
        return n

if __name__ == "__main__":
    S = Solution()

    print_test = lambda nums: print("{} -> {}".format(nums, S.firstMissingPositive(nums)))

    print_test([1,2,4,5]) # 3
    print_test([1,2,0]) # 3
    print_test([7,8,9,10,11,12]) # 1
    print_test([3,4,-1,1]) # 2
    print_test([2,2]) # 1
