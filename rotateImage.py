from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n):
            for j in range(n-1, i//2-1, -1):
                new_i = j
                new_j = n-i-1
                matrix[i][j], matrix[new_i][new_j] = matrix[new_i][new_j], matrix[i][j]
        # matrix[0][0], matrix[n-1][n-1] = matrix[n-1][n-1], matrix[0][0]

if __name__ == "__main__":
    S = Solution()
    print_test = lambda x: (print(x), S.rotate(x), print(x))
    print_test([[0,1,2],[3,4,5],[6,7,8]])
    print_test([[0 ,1 ,2 ,3 ],
                [4 ,5 ,6 ,7 ],
                [8 ,9 ,10,11],
                [12,13,14,15]])
    