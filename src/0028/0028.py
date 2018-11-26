class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        import re
        result = re.search(needle, haystack)
        if result:
            return result.start(0)
        else:
            return -1


if __name__ == "__main__":
    haystack = "hello"
    needle = "ll"
    print Solution().strStr(haystack, needle)
