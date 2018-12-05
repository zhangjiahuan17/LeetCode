class Solution(object):
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        result = 0
        columns = len(A[0])
        strs = len(A)-1
        for column in range(columns):
            for s in range(strs):
                if A[s][column] > A[s+1][column]:
                    result += 1
                    break
        return result


if __name__ == "__main__":
    A = ["cba", "daf", "ghi"]
    print Solution().minDeletionSize(A)
