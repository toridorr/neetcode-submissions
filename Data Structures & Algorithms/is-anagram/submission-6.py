class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
    # SORTED SOLUTION -     
        # return sorted(s) == sorted(t)    
    
    # COUNTER SOLUTION - 
        # return Counter(s) == Counter(t)

    # HASHMAPP SOLUTION (MY SOLUTION) 
        dict_s = {}
        dict_t = {}

        for char in s: # we don't care about index so can do this 
            if char in dict_s: # if char is a key in the dict_s dictionary 
                # increase the count by 1 
                dict_s[char] += 1 
            else:
                # if not in dict_s then add it 
                dict_s[char] = 1 
        
        for char in t:
            if char in dict_t:
                dict_t[char] += 1
            else:
                dict_t[char] = 1 

        return True if dict_s == dict_t else False    
    
    # Example: s = "racecar", t = "carrace"
    # 1st loop: char = r
    # r is not in dict_s so add it, dict_s = {'r':1}
    # 2nd loop: char = a
    # a is not in dict_s so add it, dict_s = {'r':1, 'a':1}
    # 3rd loop: char = c
    # c is not in dict_s so add it, dict_s = {'r':1, 'a':1, 'c':1}
    # 4th loop: char = e
    # e is not in dict_s so add it, dict_s = {'r':1, 'a':1, 'c':1, 'e': 1}  
    # 5th loop: char = c 
    # c is in dict_s so run the if statement dict_s[char] += 1 which is dict_s[char] = 
    # dict_s[char] + 1 = dict_s['c'] + 1 = 1 + 1 = 2 therefore, run dict_s['c'] = 2 which 
    # will update dict_s = {'r':1, 'a':1, 'c':2, 'e': 1} 
    # ... 
    # do the same with t... 
    # then compare the dictonaries 

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # SORTING SOLUTION - DONE 1X 
        # return True if sorted(s) == sorted(t) else False 
        
        # this could be even cleaner than this already pretty clean code!
        # what is the time and space complexity, time - O(nlogn) for sorting 
        # and if we don't count the temporary storage used to create these sorted strings 
        # then space - O(1) constant time 

    # # DICTIONARY SOLUTION 
    #     dict_s = {}
    #     dict_t = {}

    #     for char in s:
    #         if char in dict_s:
    #             dict_s[char] += 1
    #         else:
    #             dict_s[char] = 1 

    #     for char in t:
    #         if char in dict_t:
    #             dict_t[char] += 1
    #         else:
    #             dict_t[char] = 1

    #     return True if dict_s == dict_t else False
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # because this involves sorting, it will have time complexity = O(nlogn) and O(1) space
        # if len(s) == len(t):
        #     sorted_s = sorted(s)
        #     sorted_t = sorted(t)
        #     if sorted(s) == sorted(t):
        #         return True
        # return False