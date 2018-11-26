class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        import re
        str = str.strip()
        result = re.search(r"^[+-]?\d+", str)
        if result:
            result = int(result.group(0))
            print result
            if result < 0:
                return result if result > pow(-2, 31) else pow(-2, 31)
            else:
                return result if result < pow(2, 31)-1 else pow(2, 31)-1
        else:
            return 0


if __name__ == "__main__":
    str = "42"
    print Solution().myAtoi(str)
