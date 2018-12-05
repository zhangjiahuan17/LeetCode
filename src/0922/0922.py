class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        '''solution 1'''
        # now = 0
        # result = []
        # for i in range(len(A)):
        #     if now == 0:
        #         for a in A:
        #             if not isOdd(a):
        #                 result.append(a)
        #                 A.remove(a)
        #                 now = 1
        #                 break
        #     else:
        #         for a in A:
        #             if isOdd(a):
        #                 result.append(a)
        #                 A.remove(a)
        #                 now = 0
        #                 break
        # return result
        '''solution 2'''
        A_len, i, j = len(A), 0, 1
        while i < A_len:
            if A[i] % 2 != 0:
                while A[j] % 2 != 0:
                    j += 2
                A[i], A[j] = A[j], A[i]
            i += 2
        return A


def isOdd(n):
    if n % 2 != 0:
        return True
    else:
        return False


if __name__ == "__main__":
    A = [4, 2, 5, 7]
    print Solution().sortArrayByParityII(A)
