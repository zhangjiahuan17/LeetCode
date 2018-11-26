# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        '''!!!'''
        newhead = ListNode(0)
        newhead.next = head
        p = newhead
        q = newhead
        for i in range(n+1):
            p = p.next
        while p:
            p = p.next
            q = q.next
        q.next = q.next.next
        return newhead.next


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

    print 'NULL'


if __name__ == "__main__":
    head = createList()
    printList(head)
    res = Solution().removeNthFromEnd(head, 2)
    printList(res)
