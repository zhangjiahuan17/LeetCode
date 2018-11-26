class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        return A.index(max(A))


if __name__ == "__main__":
    A = [0, 1, 0]
    print Solution().peakIndexInMountainArray(A)
