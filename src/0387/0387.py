import collections


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        '''solution 1:'''
        # dict={}
        # for i,str in enumerate(s):
        #     if str not in dict.keys():
        #         dict[str]=1
        #     else:
        #         dict[str]+=1
        # for str in s:
        #     if dict[str]==1:
        #         return s.find(str)
        # return -1
        '''solution 2:'''
        dict = collections.Counter(s)
        for str in s:
            if dict[str] == 1:
                return s.find(str)
        return -1


if __name__ == "__main__":
    s = "leetcode"
    print Solution().firstUniqChar(s)
