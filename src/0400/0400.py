class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        '''solutiuon 1'''
        count = 0
        countlist = []
        lastmaxlist = []
        for i in range(1, 500):
            lastmax = int('9'*i)
            nowcount = 9*10**(i-1)*i
            count = count+nowcount
            if n > count:
                countlist.append(count)
                lastmaxlist.append(lastmax)
                continue
            else:
                if countlist == []:
                    count = 0
                    lastmax = 0
                else:
                    count = countlist[-1]
                    lastmax = lastmaxlist[-1]
                nowmin = lastmax+1
                now = nowmin
                nowmax = int('9'*(i))
                if n > 9:
                    n = n-count
                a = n/(i)
                b = n % (i)
                if b == 0:
                    a = a-1
                    b = i
                now = now+a
                return int(str(now)[b-1])
                # OR
                # return ord(str(nowmin+a)[b-1])-ord('0')
        '''solution 2'''

        # digit=1
        # base=9
        # ith=1
        # while n>base*digit:
        #     n=n-base*digit
        #     digit=digit+1
        #     ith=ith+base
        #     base=base*10
        # return ord(str(ith+(n-1)/digit)[(n-1)%digit])-ord('0')
if __name__ == "__main__":
    n = 3
    print Solution().findNthDigit(n)
