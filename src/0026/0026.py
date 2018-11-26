class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        count = 1
        for i in range(0, len(nums)-1):
            if nums[i+1] != nums[i]:
                nums[count] = nums[i+1]
                count = count+1

        return count


if __name__ == "__main__":
    nums = [1, 1, 2]
    print Solution().removeDuplicates(nums)
