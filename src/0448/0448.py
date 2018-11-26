class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        tmp = [0]*len(nums)
        for num in list(nums):
            tmp[num-1] = 1
        return [i+1 for i, t in enumerate(tmp) if t == 0]


if __name__ == "__main__":
    nums = [4, 3, 2, 7, 8, 2, 3, 1]
    print Solution().findDisappearedNumbers(nums)
