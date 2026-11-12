# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head 
        while curr is not None: # Recall, I cannot use 'curr != None' here because 'None' is not a value like '3' or something. I need to use 'is not None' here. 
            next_node = curr.next 
            curr.next = prev 
            prev = curr 
            curr = next_node 
        return prev # I originally had this as 'return curr' which would have returned 'None' instead of the new head  


        
        # Example: head = [0, 1, 2, 3]
        # None  ->  0  ->  1 ->  2  ->  3
        # prev     curr 
        # 1st loop: prev = None, curr = 0 
        # next_node = 1 
        # curr.next = None 
        # prev = 0
        # curr = 1 
        # None  <-  0  ->  1 ->  2  ->  3
        #         prev    curr 
        # 2nd loop: prev = o, curr = 1 
        # next_node = 2 
        # curr.next = 0 
        # prev = 1 
        # curr = 2 
        # None  <-  0  <-  1   ->  2  ->  3
        #                 prev    curr 
        # 3rd loop: prev = 1, curr = 2 
        # next_node = 





















    # ITERATIVE SOLUTION - 1ST ATTEMPT 
        # prev = None
        # curr = head 

        # while curr is not None:
        #     next_node = curr.next # storing the next node so we can move our current pointer there 
        #     curr.next = prev # switch the arrow direction, so the current node points to the previous node 

        #     prev = curr # now we need to move the previous pointer over. The order we move these pointers matters! 
        #     curr = next_node # and move the current pointer over
            
        # return prev # This will return just the number the previous pointer is pointing at 

        # 1st loop: 
        # prev = None
        # curr = head = 0 -> not None so while loop runs
        # next_node = 2 
        # None <- 0 switching the direction of the arrow between these 
        # Move prev pointer to 1 
        # Move the curr pointer to 2 
        # So we have: None <- 1  2 -> 3 -> None 
        #                     p  c 

        # 2nd loop:
        # prev = 1 
        # curr = 2 
        # next_node = 3 
        # 1 <- 2 swicthing the direction of the arrow between these 
        # Move the prev pointer to 2 
        # Move the curr pointer to 3 
        # So we have: None <- 1 <- 2   3 -> None
        #                          p   c 

        # 3rd loop:
        # prev = 2 
        # curr = 3 
        # next_node = None
        # 2 <- 3 
        # Move the prev pointer to 3 
        # Move the curr pointer to None 
        # So we have: None <- 1 <- 2 <- 3 -> None
        #                               p    c            
        # 4th loop:
        # prev = 3 
        # curr = None 
        # The while loop condition fails do exit out of the while loop and return prev = 3 
        