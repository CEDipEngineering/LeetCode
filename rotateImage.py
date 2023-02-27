from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(n):
            matrix[i].reverse()

if __name__ == "__main__":
    S = Solution()
    print_test = lambda x: (print(x), S.rotate(x), print(x))
    print_test([[0,1,2],[3,4,5],[6,7,8]])
    print_test([[0 ,1 ,2 ,3 ],
                [4 ,5 ,6 ,7 ],
                [8 ,9 ,10,11],
                [12,13,14,15]])
    