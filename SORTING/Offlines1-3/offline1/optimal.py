"""
NOTE: We had to implement the  min heap ds ourselves

Solved using min heap - optimal for this problem
Valentyn Oliinyk
T/S - O(n*log(k)/O(1)
-- similar to: sort a nearly sorted array( K sorted array)
"""
import heapq
from zad1testy import Node, runtests

def sortKSortedLinkedList(head, k):
    if not head:
        return head
    
    dummy = Node()
    curr = dummy
    heap = []
    
    node = head
    for _ in range(k + 1):
        if node:
            heapq.heappush(heap, (node.val, node))
            node = node.next
    
    while heap:
        val, smallest = heapq.heappop(heap)
        curr.next = smallest
        curr = curr.next
        
        if node:
            heapq.heappush(heap, (node.val, node))
            node = node.next
    
    curr.next = None
    return dummy.next

def SortH(p, k):
    return sortKSortedLinkedList(p, k)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( SortH, all_tests = True )
