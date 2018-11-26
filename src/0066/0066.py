class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        '''solution 1: '''
        # result=[]
        # number=0
        # for i,digit in enumerate(reversed(digits)):
        #     number=number+digit*pow(10,i)
        # number=int(number+1)
        # return map(int,str(number))
        '''solution 2: '''
        if digits[-1] != 9:
            digits[-1] += 1
            return digits
        else:
            for i in reversed(range(len(digits))):
                if i > 0:
                    if digits[i]+1 == 10:
                        digits[i] = 0
                    else:
                        digits[i] += 1
                        return digits
                else:
                    if digits[i]+1 == 10:
                        digits[i] = 0
                        digits.insert(0, 1)
                    else:
                        digits[i] += 1
            return digits


if __name__ == "__main__":
    digits = [0]
    print(Solution().plusOne(digits))
