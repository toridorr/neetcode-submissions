# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        curr = head 

        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            elif list1.val > list2.val:
                curr.next = list2 
                list2 = list2.next
            
            curr = curr.next

        if list1: # if list1 points to a node then the current node should point to the list1 node 
            curr.next = list1
        else: # if list1 does not point to a node then the current not should point to the list2 node
            curr.next = list2

        return head.next 



        


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # INITIAL ATTEMPT     
        # head = ListNode() # Creates a dummy node 'None'
        # curr = head

        # while list1 and list2: # while both of these have nodes, when either of them runs out, break out of the loop
        #     if list1.val <= list2.val: 
        #         curr.next = list1
        #         # curr = list1 # we take care of moving curr below so don't need this here
        #         # list1 = curr.next # since we are moving curr oustide this if statement then we just move list1
        #         list1 = list1.next
                
        #     else: # list1.val > list2.val:
        #         curr.next = list2
        #         # curr = list2 # we take care of moving curr below so don't need this here
        #         # list2 = curr.next # since we are moving curr outside this if statement then we just move list2 
        #         list2 = list2.next
            
        #     curr = curr.next

        # # we do this outside of the while loop    
        # if list1 is None: # so we do this instead of 'list1.val == None'
        #     curr.next = list2
        # else: # list2 is None: # so we do this instead of 'list2.val == None'
        #     curr.next = list1

        # return head.next
            



        

        




