class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        result = 0
        g.sort()
        s.sort()
        gi = 0
        si = 0
        while gi < len(g) and si < len(s):
            if s[si] >= g[gi]:
                result += 1
                gi += 1
                si += 1
            else:
                si += 1
        return result


if __name__ == "__main__":
    g = [1, 2, 3]
    s = [3]
    print Solution().findContentChildren(g, s)
