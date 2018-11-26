class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        x = str(x)
        for i in range(len(x)):
            if x[i] != x[len(x)-1-i]:
                return False
        return True


if __name__ == "__main__":
    x = 121
    print Solution().isPalindrome(x)
