class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        indexScores = list(enumerate(score))
        sortedScores = sorted(indexScores, key=lambda x: x[1], reverse=True)
        for i,e in enumerate(sortedScores):
            if i == 0:
                score[e[0]] = "Gold Medal"
            elif i == 1:
                score[e[0]] = "Silver Medal"
            elif i == 2:
                score[e[0]] = "Bronze Medal"
            else:
                score[e[0]] = str(i+1)
        return score

if __name__ == "__main__":
    S = Solution()
    print(S.findRelativeRanks([10, 20, 2, 5, 7, 10, 17, 25]))