class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        res = [ [1]*i for i in range(1,numRows+1)]
        for row in range(2,numRows):
            for i in range(1,len(res[row])-1):
                res[row][i] = res[row-1][i-1] + res[row-1][i]         
        return res
