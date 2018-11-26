class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        '''solution 1:'''
#         dotCount=0
#         for i in range(9):
#             for j in range(9):
#                 if board[i][j]=='.':
#                     dotCount+=1
#                     if dotCount==81:
#                         return True
#                 else:
#                     if validInLine(board,board[i][j],i,j)==False:
#                         print 'line {} {}'.format(i,j)
#                         return False
#                     elif validInColumn(board,board[i][j],i,j)==False:
#                         print 'column {} {}'.format(i,j)
#                         return False
#                     elif validInBlock(board[i][j],board,i,j)==False:
#                         print 'block {} {}'.format(i,j)
#                         return False
#         return True
                
                    
        
        
# def validInLine(board,number,line,column):
#     if board[line].count(number)>1:
#         print number
#         print board[line]
#         return False
#     else:
#         return True
# def validInColumn(board,number,line,column):
#     list=[board[i][column] for i in range(9)]
#     if list.count(number)>1:
#         return False
#     else:
#         return True
# def validInBlock(number,board,i,j):
#     if i<=2:
#         mini=0
#         maxi=2
#         if j<=2:
#             minj=0
#             maxj=2
#         elif j>=6:
#             minj=6
#             maxj=8
#         else:
#             minj=3
#             maxj=5
#     elif i>=6:
#         mini=6
#         maxi=8
#         if j<=2:
#             minj=0
#             maxj=2
#         elif j>=6:
#             minj=6
#             maxj=8
#         else:
#             minj=3
#             maxj=5
#     else:
#         mini=3
#         maxi=5
#         if j<=2:
#             minj=0
#             maxj=2
#         elif j>=6:
#             minj=6
#             maxj=8
#         else:
#             minj=3
#             maxj=5
#     list=[]
#     for i in range(mini,maxi+1):
#         for j in range(minj,maxj+1):
#             list.append(board[i][j])
#     if list.count(number)>1:
#         return False
#     else:
#         return True
        '''solution 2: !!!'''
        Row=[[] for i in range(9)]
        Col=[[] for i in range(9)]
        Box=[[] for i in range(9)]
        
        for i,row in enumerate(board):
            for j,number in enumerate(row):
                if number!='.':
                    # which box should number in
                    b=(i//3)*3+j//3
                    if number in Row[i]+Col[j]+Box[b]:
                        return False
                    else:
                        Row[i].append(number)
                        Col[j].append(number)
                        Box[b].append(number)
        return True


if __name__ == "__main__":
    board=[["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    print Solution().isValidSudoku(board)