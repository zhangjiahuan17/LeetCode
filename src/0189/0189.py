class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        while(k > 0):
            nums.insert(0, nums[-1])
            del nums[-1]
            k = k-1


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 1
    Solution().rotate(nums, k)
    print(nums)
