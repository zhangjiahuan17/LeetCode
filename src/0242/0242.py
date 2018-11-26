import collections


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        dicts = collections.Counter(s)
        dictt = collections.Counter(t)
        for str in t:
            if str not in dicts.keys():
                return False
            elif dictt[str] != dicts[str]:
                return False
        return True


if __name__ == "__main__":
    s = "anagram"
    t = "nagaram"
    print(Solution().isAnagram(s, t))
