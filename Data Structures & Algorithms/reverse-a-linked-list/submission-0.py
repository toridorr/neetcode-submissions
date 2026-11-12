# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head 

        while curr is not None:
            next_node = curr.next # storing the next node so we can move our current pointer there 
            curr.next = prev # switch the arrow direction, so the current node points to the previous node 

            prev = curr 
            curr = next_node
            
        return prev

# 1st loop: 
# prev = None
# curr = head = 0 -> not None so while loop runs
# next_node = 2 
# None <- 0 switching the direction of the arrow between these 
# Move prev pointer to 1 
# Move the curr pointer to 2 

# 2nd loop:
# prev = 1 
# curr = 2 
# next_node = 3 
# 1 <- 2 swicthing the direction of the arrow between these 
# Move the prev pointer to 2 
# Move the curr pointer to 3 

# 3rd loop:
# by the end curr will be moved to None and then in the 4th loop the while loop condition is
# False so should return head 
            



        