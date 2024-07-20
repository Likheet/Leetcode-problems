class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        result = [[0 for i in range(len(colSum))] for j in range(len(rowSum))]
        for i in range(len(result)):
            for j in range(len(result[0])):
                curr = min(rowSum[i], colSum[j])
                result[i][j] = curr
                rowSum[i] -= curr
                colSum[j] -= curr
        return result