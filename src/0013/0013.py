class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                'C': 100, 'D': 500, 'M': 1000}
        s = list(s)
        sumlist = []
        while len(s) > 1:
            print sumlist
            if s[0] == 'I' and s[1] == 'V':
                sumlist.append(4)
                s.pop(1)
                s.pop(0)
            elif s[0] == 'I' and s[1] == 'X':
                sumlist.append(9)
                s.pop(1)
                s.pop(0)
            elif s[0] == 'X' and s[1] == 'L':
                sumlist.append(40)
                s.pop(1)
                s.pop(0)
            elif s[0] == 'X' and s[1] == 'C':
                sumlist.append(90)
                s.pop(1)
                s.pop(0)
            elif s[0] == 'C' and s[1] == 'D':
                sumlist.append(400)
                s.pop(1)
                s.pop(0)
            elif s[0] == 'C' and s[1] == 'M':
                sumlist.append(900)
                s.pop(1)
                s.pop(0)
            else:
                sumlist.append(dict[s[0]])
                s.pop(0)
        if len(s) == 1:
            sumlist.append(dict[s[0]])
        return sum(sumlist)


if __name__ == "__main__":
    s = "III"
    print Solution().romanToInt(s)
