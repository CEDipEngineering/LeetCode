from typing import List

class Solution():
    def getMaxLen(self, nums: List[int]):
        paridade, inicio_seq, fim_seq, primeiro_neg, ultimo_neg, res = True, 0, 0, -1, -1, 0
        while fim_seq <= len(nums):
            if fim_seq == len(nums) or nums[fim_seq] == 0:
                if paridade:
                    res = max(res, fim_seq-inicio_seq)
                else:
                    res = max(res, fim_seq-primeiro_neg-1, ultimo_neg-inicio_seq)
                paridade, inicio_seq, primeiro_neg, ultimo_neg = True, fim_seq+1, -1, -1
            elif nums[fim_seq] < 0:
                paridade = not paridade
                ultimo_neg = fim_seq
                if primeiro_neg < 0: primeiro_neg = fim_seq
            fim_seq += 1
        return res
    
if __name__ == "__main__":
    S = Solution()
    print_test = lambda nums: print("{}: {}".format(nums, S.getMaxLen(nums)))

    print_test([-1, 2, 0, 2, -3, 4, -1])
    print_test([0, 1, -2, -3, -4])