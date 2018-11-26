class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums_len = len(nums)
        set_len = len(set(nums))
        if nums_len == set_len:
            return False
        else:
            return True
