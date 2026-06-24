# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        


        # lists = [[1,2,4],[1,3,5],[3,6]]
        # result = [1,1,2,3,3,4,5,6]

        nodes = []

        for list in lists:
            while list:
                nodes.append(list.val)
                list = list.next
        
        nodes.sort()


        result = ListNode(0)
        curr = result

        for node in nodes:
            curr.next = ListNode(node)
            curr = curr.next

        return result.next
        