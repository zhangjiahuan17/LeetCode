class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        '''solution 1:'''
        # return s[::-1]
        '''solution 2:'''
        s = list(s)
        for i in range(len(s)/2):
            tmp = s[i]
            s[i] = s[len(s)-1-i]
            s[len(s)-1-i] = tmp
        return ''.join(s)


if __name__ == "__main__":
    s = "hello"
    print(Solution().reverseString(s))
