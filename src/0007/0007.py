class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            x = str(0-x)
            x = 0-reverseStr(x)
            if x < pow(-2, 31):
                return 0
            return x
        else:
            x = str(x)
            x = reverseStr(x)
            if x > pow(2, 31)-1:
                return 0
            return x


def reverseStr(strX):
    return int(strX[::-1])


if __name__ == "__main__":
    x = 123
    print Solution().reverse(x)
