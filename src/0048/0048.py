class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        '''solution 1:'''
        list = []
        l1 = len(matrix)
        l2 = len(matrix[0])
        for i in range(l1):
            for j in range(l2):
                for t in range(4):
                    if t == 0:
                        dst = [j, l1-i-1]
                        if dst in list:
                            continue
                        else:
                            list.append(dst)
                            tmp = matrix[dst[0]][dst[1]]
                            matrix[dst[0]][dst[1]] = matrix[i][j]
                    else:
                        dst = [dst[1], l1-dst[0]-1]
                        if dst in list:
                            continue
                        else:
                            list.append(dst)
                            tmp1 = matrix[dst[0]][dst[1]]
                            matrix[dst[0]][dst[1]] = tmp
                            tmp = tmp1
        '''solution 2: T --> reverse'''


if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    Solution().rotate(matrix)
    print(matrix)
