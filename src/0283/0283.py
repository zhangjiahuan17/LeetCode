class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        '''solution 1:'''
        # numberOfZero=nums.count(0)
        # for num in nums[:]:
        #     if num==0:
        #         nums.remove(0)
        # for i in range(numberOfZero):
        #     nums.append(0)
        '''solution 2: ???'''
        # condition=lambda x:x!=0
        # numberOfZero=nums.count(0)
        # nums=list(filter(condition,nums))
        # for i in range(numberOfZero):
        #     nums.append(0)
        # print nums
        '''solution 3: !!!'''
        numberOfZero = nums.count(0)
        for num in reversed(nums):
            if num == 0:
                nums.remove(0)
        for i in range(numberOfZero):
            nums.append(0)


if __name__ == "__main__":
    arr = [0, 1, 0, 3, 12]
    Solution().moveZeroes(arr)
    print(arr)
