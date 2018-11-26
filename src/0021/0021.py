# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        '''solution 1:'''
        # if l1==None:
        #     return l2
        # if l2==None:
        #     return l1
        # list1 = []
        # list2 = []
        # while l1:
        #     list1.append(l1.val)
        #     l1 = l1.next
        # while l2:
        #     list2.append(l2.val)
        #     l2 = l2.next
        # rlist = []
        # for i, b in enumerate(list2):
        #     aa = filter(lambda x: x <= b, list1)
        #     print b, aa
        #     rlist = rlist + aa + [b]
        #     for a in aa:
        #         list1.remove(a)
        # if list1 != []:
        #     rlist = rlist + list1
        # print rlist
        # head = ListNode(0)
        # p = head
        # for r in rlist:
        #     p.next=ListNode(r)
        #     p=p.next
        # return head.next
        '''solution 2:'''
        # if l1 == None:
        #     return l2
        # elif l2 == None:
        #     return l1
        # head = ListNode(0)
        # p = head
        # while l1 is not None and l2 is not None:
        #     if l1.val < l2.val:
        #         p.next = ListNode(l1.val)
        #         l1 = l1.next
        #     else:
        #         p.next = ListNode(l2.val)
        #         l2 = l2.next
        #     p = p.next
        # if l1 is None:
        #     p.next = l2
        # if l2 is None:
        #     p.next = l1
        # return head.next
        '''solution 3:'''
        if l1 == None:
            return l2
        elif l2 == None:
            return l1
        head = None
        if l1.val < l2.val:
            head = l1
            head.next = self.mergeTwoLists(l1.next, l2)
        else:
            head = l2
            head.next = self.mergeTwoLists(l1, l2.next)
        return head


def createList():
    head = ListNode(0)
    cur = head
    cur.next = ListNode(0)
    cur.next.next = ListNode(1)
    cur.next.next.next = ListNode(2)
    return head


def printList(head):
    cur = head
    while cur != None:
        print cur.val, '-->',
        cur = cur.next

    print('NULL')


if __name__ == "__main__":
    l1 = createList()
    printList(l1)
    l2 = createList()
    printList(l2)
    res = Solution().mergeTwoLists(l1, l2)
    printList(res)
