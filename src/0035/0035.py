class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i, num in enumerate(nums):
            print num
            if num == target:
                return i
            elif target < nums[0]:
                return 0
            elif target > nums[len(nums)-1]:
                return len(nums)
            elif target > nums[i-1] and target < nums[i]:
                return i


if __name__ == "__main__":
    nums = [1, 3, 5, 6]
    target = 5
    print(Solution().searchInsert(nums, target))
