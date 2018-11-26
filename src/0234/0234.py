class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        '''solution 1:'''
        # list=[]
        # p=head
        # while p:
        #     list.append(p.val)
        #     p=p.next
        # for i in range(len(list)/2):
        #     if list[i]!=list[len(list)-i-1]:
        #         return False
        # return True
        '''solution 2:'''
        # fast=slow=head
        # left_half=[]
        # while fast and fast.next:
        #     left_half.append(slow.val)
        #     slow=slow.next
        #     fast=fast.next.next
        # if fast:
        #     slow=slow.next
        # for i in left_half[::-1]:
        #     if i!=slow.val:
        #         return False
        #     slow=slow.next
        # return True
        '''solution 3:'''
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        if fast:
            slow = slow.next
        slow = reverseList(slow)
        while slow:
            if slow.val != head.val:
                return False
            slow = slow.next
            head = head.next
        return True


def reverseList(head):
    newhead = None
    while head:
        p = head
        head = head.next
        p.next = newhead
        newhead = p
    return newhead


def createList():
    head = ListNode(0)
    cur = head
    for i in range(1, 3):
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
    res = Solution().isPalindrome(head)
    print(res)
