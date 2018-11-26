class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        '''solution 1: if Line 10 --> dict.keys()'''
        '''            out of time'''
#         dict={}
#         for num in nums:
#             if num in dict:
#                 dict[num]+=1
#             else:
#                 dict[num]=1

#         for num in dict:
#             if dict[num]==1:
#                 return num
        '''solution 2: ??????'''
        res = 0
        for i in nums:
            res ^= i
        return res


if __name__ == "__main__":
    nums = [2, 2, 1]
    print(Solution().singleNumber(nums))
