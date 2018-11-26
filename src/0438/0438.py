class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        '''solution 1'''
        # from collections import Counter
        # result=[]
        # pdict=Counter(p)
        # tdict=Counter()
        # lens=len(s)
        # lenp=len(p)
        # for i in range(lens):
        #     tdict[s[i]]+=1
        #     if i>=lenp:
        #         tdict[s[i-lenp]]-=1
        #         if tdict[s[i-lenp]]==0:
        #             del tdict[s[i-lenp]]
        #     if pdict==tdict:
        #         result.append(i-lenp+1)
        # return result
        '''solution 2'''


if __name__ == "__main__":
    s = "cbaebabacd"
    p = "abc"
    print(Solution().findAnagrams(s, p))
