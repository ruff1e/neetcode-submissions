# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        
        # fist create an empty array nodes and put all the elements from the linked list in there

        nodes = []
        curr = head

        while curr:
            nodes.append(curr)
            curr = curr.next

        
        # then initialize 2 pointers from the start and the end and start appending them to the result
        left, right = 0, len(nodes) - 1

        while left < right:
            nodes[left].next = nodes[right]
            left += 1

            if left >= right:
                break
            
            nodes[right].next = nodes[left]
            right -= 1
        
        nodes[left].next = None