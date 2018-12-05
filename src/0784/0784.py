class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        result = []
        self.dfs('', S, result, 0)
        return result

    def dfs(self, pre, S, result, index):
        if index == len(S):
            result.append(pre)
        else:
            ch = S[index]
            if ch.isdigit():
                self.dfs(pre+ch, S, result, index+1)
            else:
                ch = ch.lower()
                self.dfs(pre+ch, S, result, index+1)
                ch = ch.upper()
                self.dfs(pre+ch, S, result, index+1)


if __name__ == "__main__":
    S = "a1B2"
    print Solution().letterCasePermutation(S)
