from typing import List
from itertools import combinations

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        """
        For every combination, store pair->len_product
        for every pair from high to low, chekc if intersection of pairs is empty
        """
        pairs = []
        for a,b in combinations(words, 2):
            pairs.append((a,b,len(a)*len(b)))
        pairs = sorted(pairs, key=lambda x: x[2], reverse=True)
        for p in pairs:
            if len(set(p[0]).intersection(set(p[1]))) == 0:
                return p[2]
        return 0

if __name__ == "__main__":
    S = Solution()
    print_test = lambda x: print("Input:  {}\nOutput: {}".format(x, S.maxProduct(x)))

    words = ["abcw","baz","foo","bar","xtfn","abcdef"]
    print_test(words) # should output 16
    
    words = ["a","ab","abc","d","cd","bcd","abcd"]
    print_test(words) # should output 4

    words = ["a","aa","aaa","aaaa"]
    print_test(words) # should output 0