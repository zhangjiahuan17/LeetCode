class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        fivecnt = 0
        tencnt = 0
        for bill in bills:
            if bill == 5:
                fivecnt += 1
            if bill == 10:
                tencnt += 1
            charge = bill-5
            if charge == 15:
                if tencnt >= 1 and fivecnt >= 1:
                    tencnt -= 1
                    fivecnt -= 1
                elif tencnt == 0 and fivecnt >= 3:
                    fivecnt -= 3
                else:
                    return False
            elif charge == 5:
                if fivecnt >= 1:
                    fivecnt -= 1
                else:
                    return False
        return True


if __name__ == "__main__":
    bills = [5, 5, 5, 10, 20]
    print Solution().lemonadeChange(bills)
