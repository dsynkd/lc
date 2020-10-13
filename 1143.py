import numpy
class Solution:
    def longestCommonSubsequence(self, a: str, b: str) -> int:
        m = len(a)
        n = len(b)
        d = numpy.zeros((m+1,n+1))
        for i in range(1,m+1):
            for j in range(1,n+1):
                d[i][j] = d[i-1][j-1]+1 if a[i-1] == b[j-1] else max(d[i-1][j], d[i][j-1])
        return int(d[m][n])
