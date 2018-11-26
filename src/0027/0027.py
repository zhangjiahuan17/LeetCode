class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        for num in nums[::-1]:
            if num == val:
                nums.remove(val)
        return len(nums)


if __name__ == "__main__":
    nums = [3, 2, 2, 3]
    val = 2
    print(Solution().removeElement(nums, val))
