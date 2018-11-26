class Solution(object):
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        dict = {}
        linenum = 1
        linecount = 0
        for i in range(ord('a'), ord('z')+1):
            dict[chr(i)] = i-ord('a')
        for i in range(len(S)):
            if linecount+widths[dict[S[i]]] > 100:
                linenum = linenum+1
                linecount = widths[dict[S[i]]]
            else:
                linecount = linecount+widths[dict[S[i]]]
        return [linenum, linecount]


if __name__ == "__main__":
    widths = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10,
              10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
    S = "abcdefghijklmnopqrstuvwxyz"
    print Solution().numberOfLines(widths, S)
