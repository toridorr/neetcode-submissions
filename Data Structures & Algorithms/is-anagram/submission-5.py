class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return True if sorted(s) == sorted(t) else False
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # because this involves sorting, it will have time complexity = O(nlogn) and O(1) space
        if len(s) == len(t):
            sorted_s = sorted(s)
            sorted_t = sorted(t)
            if sorted(s) == sorted(t):
                return True
        return False