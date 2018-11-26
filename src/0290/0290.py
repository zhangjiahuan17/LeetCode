class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        dict = {}
        str = str.split()
        if len(pattern) != len(str):
            return False
        for i, p in enumerate(pattern):
            if p not in dict.keys():
                dict[p] = []
            dict[p].append(str[i])
        for p in dict.keys():
            if len(set(dict[p])) != 1 or len(set(pattern)) != len(set(str)):
                return False

        return True


if __name__ == "__main__":
    pattern = "abba"
    str_ = "dog dog dog dog"
    print(Solution().wordPattern(pattern, str_))
