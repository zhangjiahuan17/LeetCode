class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        '''solution 1:'''
#         if len(strs)==0:
#             return ''
#         if len(strs)==1 and strs[0]=='':
#             return ''
#         if len(strs)==1 and strs[0]!='':
#             return strs[0]
#         same = samepart(strs[0], strs[1])
#         if same == '':
#             return same
#         for i in range(2, len(strs)):
#             same = samepart(same, strs[i])
#         return same


# def samepart(s1, s2):
#     res = ''
#     if len(s2) < len(s1):
#         tmp = s2
#         s2 = s1
#         s1 = tmp
#     for i, s in enumerate(s1):
#         if s2[i] == s:
#             res = res + s
#         else:
#             break
#     return res
        '''solution 2:'''
        res = ''
        strs = zip(*strs)
        for i in strs:
            if len(set(i)) == 1:
                res = res+i[0]
            else:
                break
        return res


if __name__ == "__main__":
    strs = ["flower", "flow", "flight"]
    print Solution().longestCommonPrefix(strs)
