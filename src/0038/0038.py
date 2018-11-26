import re


class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        tmp = '1'
        for i in range(n-1):
            tmp = iter(tmp)
            print tmp
        return tmp


def iter(n):
    n = str(n)
    matcher = re.compile(r'(\d)\1*')
    ret = [match.group() for match in matcher.finditer(n)]
    for i, r in enumerate(ret):
        ret[i] = str(len(r)*10+int(r[0]))
    return ''.join(ret)


if __name__ == "__main__":
    n = 1
    print Solution().countAndSay(n)
