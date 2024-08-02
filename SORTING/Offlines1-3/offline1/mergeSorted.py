"""
Solved using merge sort - not optimal for this problem
Valentyn Oliinyk
T/S - O(nlogn)/O(1)

"""
from zad1testy import Node, runtests

def getMid(head):
    slow,fast = head,head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow

def merge(head1, head2):
    tail = dummy = Node()
    while head1 and head2:
        if head1.val < head2.val:
            tail.next = head1
            head1 = head1.next
        else:
            tail.next = head2
            head2 = head2.next
        tail = tail.next
    if head1:
        tail.next = head1
    if head2:
        tail.next = head2
    
    return dummy.next
def sortList(head):
    if head is None or head.next is None:
        return head
    left = head
    right = getMid(head)
    tmp = right.next
    right.next = None
    right = tmp

    left = sortList(left)
    right = sortList(right)
    return merge(left, right)
def SortH(p, k):
   return sortList(p)
    

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( SortH, all_tests = True )
