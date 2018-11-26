class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        result = []
        for i in nums1:
            if i in nums2:
                if i not in result:
                    for j in range(min(nums1.count(i), nums2.count(i))):
                        result.append(i)
        return result


if __name__ == "__main__":
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    print(Solution().intersect(nums1, nums2))
