class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 0
        if len(nums) == 1:
            return nums[0]
        result = [0]*len(nums)
        result[0] = nums[0]
        result[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            result[i] = max(result[i-1], result[i-2]+nums[i])
        return result[-1]


if __name__ == "__main__":
    nums = [1, 2, 3, 1]
    print Solution().rob(nums)
