# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        '''solution 1:'''
        # valList=[]
        # p=head
        # while p:
        #     valList.append(p.val)
        #     p=p.next
        # result=ListNode(0)
        # q=result
        # for i in valList[::-1]:
        #     q.next=ListNode(i)
        #     q=q.next
        # return result.next
        '''solution 2:'''
        # newhead=None
        # while head:
        #     p=head
        #     head=head.next
        #     p.next=newhead
        #     newhead=p
        # return newhead
        '''solution 3: ??????'''
        newhead = None
        while head:
            p = head
            p.next = newhead
            newhead = p
            head = head.next

        return newhead


def createList():
    head = ListNode(0)
    cur = head
    for i in range(1, 10):
        cur.next = ListNode(i)
        cur = cur.next
    return head


def printList(head):
    cur = head
    while cur != None:
        print cur.val, '-->',
        cur = cur.next

    print('NULL')


if __name__ == "__main__":
    head = createList()
    printList(head)
    res = Solution().reverseList(head)
    printList(res)
