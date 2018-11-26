class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        nums = bin(n)
        for i in range(len(nums)-1):
            if nums[i+1] == nums[i]:
                return False
        return True


if __name__ == "__main__":
    n = 5
    print Solution().hasAlternatingBits(n)
