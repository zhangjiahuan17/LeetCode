class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        minIndex = []
        tmp = []
        result = []
        for i, s in enumerate(S):
            if s == C:
                minIndex.append(i)
        for i, s in enumerate(S):
            for minidx in minIndex:
                tmp.append(abs(minidx-i))
            result.append(min(tmp))
            tmp = []
        return result


if __name__ == "__main__":
    S = "loveleetcode"
    C = "e"
    print Solution().shortestToChar(S, C)
