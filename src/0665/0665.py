class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        needChange = 0
        for i in range(len(nums)-1):
            if nums[i+1] < nums[i]:
                needChange += 1
                if needChange > 1:
                    return False

                if i > 0 and nums[i+1] < nums[i-1]:
                    nums[i+1] = nums[i]
                else:
                    nums[i] = nums[i+1]
        return True


if __name__ == "__main__":
    nums = [4, 2, 3]
    print Solution().checkPossibility(nums)
