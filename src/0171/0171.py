class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict = {}
        result = 0
        for i in range(ord('A'), ord('Z')+1):
            dict[chr(i)] = i-ord('A')+1
        for i, ss in enumerate(s[::-1]):
            result = result+pow(26, i)*dict[ss]
        return result


if __name__ == "__main__":
    s = 'ZY'
    print Solution().titleToNumber(s)
