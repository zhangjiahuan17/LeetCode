class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        slist = []
        tlist = []
        for s in S:
            if s.isalpha():
                slist.append(s)
            elif s == '#':
                if len(slist) > 0:
                    slist.pop(-1)
        for t in T:
            if t.isalpha():
                tlist.append(t)
            elif t == '#':
                if len(tlist) > 0:
                    tlist.pop(-1)
        return ''.join(slist) == ''.join(tlist)


if __name__ == "__main__":
    S = "ab#c"
    T = "ad#c"
    print Solution().backspaceCompare(S, T)
