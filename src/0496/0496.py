class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        numsdict = {}
        len_nums = len(nums)
        for i, num in enumerate(nums):
            numsdict[str(num)] = i
        for i, num in enumerate(findNums):
            indexInnums = numsdict[str(num)]
            findNums[i] = -1
            if indexInnums != len_nums-1:
                for j in nums[indexInnums+1:]:
                    if j > num:
                        findNums[i] = j
                        break
        return findNums


if __name__ == "__main__":
    findNums = [4, 1, 2]
    nums = [1, 3, 4, 2]
    print Solution().nextGreaterElement(findNums, nums)
