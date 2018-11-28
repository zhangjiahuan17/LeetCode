'''
STAIR       WAYS                                            COUNT
1           1                                               1
2           11, 2                                           2
3           111, 12, 21                                     3
4           1111, 112, 211, 121, 22                         5
5           11111, 1112, 1121, 1211, 2111, 122, 212, 221    8
'''


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        '''solution 1'''
        # a = 0
        # b = 1
        # while n > 0:
        #     a, b = b, a+b
        #     n -= 1
        #     print a, b
        # return b
        '''solution 2'''
        result = [1, 1]
        if n >= 2:
            for i in range(2, n+1):
                result.append(result[i-1]+result[i-2])
        return result


if __name__ == "__main__":
    n = 5
    print Solution().climbStairs(n)
