class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        res = 0
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[i])):
                if matrix[i][j] == "0":
                    continue
                a = i+1
                b = j+1
                s = 1
                print("starting:", i, ",", j, "=", matrix[i][j])
                while a < len(matrix) and b < len(matrix[i]):
                    p = False
                    for x in range(i, a+1):
                        for y in range(j, b+1):
                            if matrix[x][y] == "0":
                                p = True
                                break
                        if p: break
                    if p: break
                    a += 1
                    b += 1
                    s += 1
                area = s*s
                if area > res: res = area
        return res
