class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        '''solution 1'''
        # if x == 0:
        #     return 0
        # left = 1
        # right = x
        # while left <= right:
        #     mid = (left+right)/2
        #     if mid*mid > x:
        #         right = mid-1
        #     elif mid*mid < x:
        #         left = mid+1
        #     else:
        #         return mid
        # return right
        '''solution 2'''
        if x < 2:
            return x
        left = 0
        right = x
        while left <= right:
            mid = (left+right)/2
            if x > mid * mid:
                left = mid + 1
                ans = mid
            elif x < mid*mid:
                right = mid - 1
            else:
                return mid
        return ans


if __name__ == "__main__":
    x = 8
    print(Solution().mySqrt(x))
