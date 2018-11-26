class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        '''solution 1'''
#         result = ''
#         c = 0
#         if len(a) < len(b):
#             a = '0'*(len(b)-len(a))+a
#         elif len(a) > len(b):
#             b = '0'*(len(a)-len(b))+b

#         for aa, bb in zip(a[::-1], b[::-1]):
#             aa = int(aa)
#             bb = int(bb)
#             if aa+bb+c == 0:
#                 result = '0'+result
#                 c = 0
#             elif aa+bb+c == 1:
#                 result = '1'+result
#                 c = 0
#             elif aa+bb+c == 2:
#                 result = '0'+result
#                 c = 1
#             elif aa+bb+c == 3:
#                 result = '1'+result
#                 c = 1
#         if c == 1:
#             result = '1'+result
#         return result
        '''solution 2'''
        return bin(int(a, 2)+int(b, 2))[2:]


if __name__ == "__main__":
    a = "11"
    b = "1"
    print(Solution().addBinary(a, b))
