class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 2:
            return False
        count = 1
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                count = count+i+num/i
        if count == num:
            return True
        return False


if __name__ == "__main__":
    num = 28
    print Solution().checkPerfectNumber(num)
