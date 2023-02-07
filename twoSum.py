from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complements = [target] * len(nums)
        size = range(len(nums))
        for i in size:
            complements[i] = target - nums[i]
        for i in size:
            for j in size:
                if nums[i] == complements[j] and i != j:
                    return [i,j]