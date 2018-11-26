# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):


class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        minboard = 1
        maxboard = n
        if minboard == maxboard:
            return minboard
        while minboard < maxboard:
            if maxboard-minboard == 1:
                if isBadVersion(minboard) == True:
                    return minboard
                else:
                    return maxboard
            else:
                cur = (minboard + maxboard) / 2
                print 'before', minboard, maxboard, cur
                if isBadVersion(cur) == False:
                    minboard = cur
                elif isBadVersion(cur) == True:
                    maxboard = cur
                print 'after ', minboard, maxboard, cur
