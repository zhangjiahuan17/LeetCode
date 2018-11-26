class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        '''solution 1'''
        # result=[]
        # for i in nums1:
        #     if i in nums2 and i not in result:
        #         result.append(i)
        # return result
        '''solution 2'''
        return list(set(nums1) & set(nums2))


if __name__ == "__main__":
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    print(Solution().intersection(nums1, nums2))
