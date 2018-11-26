class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = [str for str in s if str.isalnum()]
        for i in range(len(s)/2):
            if s[i].lower() != s[len(s)-i-1].lower():
                return False
        return True


if __name__ == "__main__":
    s = "A man, a plan, a canal: Panama"
    print(Solution().isPalindrome(s))
