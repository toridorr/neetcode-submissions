class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
    # SORTING SOLUTION - 4TH ATTEMPT   
        # a comparison always returns a bool so we don't need to add in if-else and True/False
        # return sorted(s) == sorted(t)
    
    # COUNTER SOLUTION - 2ND ATTEMPT
        # a comparison always returns a bool so we don't need to add in if-else and True/False
        # return Counter(s) == Counter(t)

    # DICTIONARY SOLUTION (TWO DICTIONARIES) - 3RD ATTEMPT
        # counter_s = Counter(s)
        # counter_t = Counter(t)

        # for char in s:
        #     if char in counter_s:
        #         counter_s[char] += 1 
        #     else:
        #         counter_s[char] = 1 
        
        # for char in t:
        #     if char in counter_t:
        #         counter_t[char] +=1
        #     else:
        #         counter_t[char] = 1 
        
        # return counter_s == counter_t
    
    # DICTIONARY SOLUTION (1 DICTIONARY) - 2ND ATTEMPT
        counter_s = Counter(s)

        for char in t:
            if char in counter_s:
                counter_s[char] -= 1 
                if counter_s[char] == 0:
                    del counter_s[char]
            else:
                return False 
        
        return True if len(counter_s) == 0 else False 




    # counter_s = {'r':2, 'a': 2, 'c':2, 'e':1}
    # char = 'c' which is a key in counter_s. counter_s['c'] = counter_s['c'] - 1 = 2 - 1
    # so reassign counter_s['c'] to be 1. 
    # counter_s = {'r':2, 'a': 2, 'c':1, 'e':1}

    # char = 'a' which is a key in counter_s. update 'a' to be 1
    # counter_s = {'r':2, 'a': 1, 'c':1, 'e':1}  

    # char = 'r' which is a key in counter_s. update 'r' value to 1
    # counter_s = {'r':1, 'a': 1, 'c':1, 'e':1}

    # char = 'r' which is a key in counter_s. update 'r' value to 0
    # counter_s = {'r':0, 'a': 1, 'c':1, 'e':1} and since 'r' == 0 we can delete
    # it from counter_s
    # counter_s = {'a': 1, 'c':1, 'e':1}

    # char = 'a' which is a key in counter_s. update 'a' value to be 1
    # counter_s = {'a': 0, 'c':1, 'e':1} and since 'a' == 0 we can delete it from
    # counter_s
    # counter_s = {'c':1, 'e':1}

    # char = 'c' which is a key in counter_s. update 'c' value to be 0 
    # counter_s = {'c':0, 'e':1} and since 'c' == 0 we can delete it from counter_s
    # counter_s = {'e':1}

    # char = 'e' which is a key in counter_s. update 'e' value to be 0 
    # counter_s = {'e':0} and since 'e' == 0 we can delete it from counter_s
    # counter_s = {}

    # we went through everything in t so we end the for loop and the next line
    # return True if the length of counter_s is 0. Since it is empty it will return
    # True. 








        
        
   
   








   
   
   
   
   
   
   
   
   
   
   
   
   
    # SORTED SOLUTION (SHORT VERSION) - 2ND ATTEMPT  
        # return sorted(s) == sorted(t)    
    
    # COUNTER SOLUTION - 1ST ATTEMPT
        # return Counter(s) == Counter(t)

    # HASHMAPP SOLUTION (MY SOLUTION) - 2ND ATTEMPT
        # dict_s = {}
        # dict_t = {}

        # for char in s: # we don't care about index so can do this 
        #     if char in dict_s: # if char is a key in the dict_s dictionary 
        #         # increase the count by 1 
        #         dict_s[char] += 1 
        #     else:
        #         # if not in dict_s then add it 
        #         dict_s[char] = 1 
        
        # for char in t:
        #     if char in dict_t:
        #         dict_t[char] += 1
        #     else:
        #         dict_t[char] = 1 

        # return True if dict_s == dict_t else False    
    
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

        # Time complexity 
        # sorting takes O(nlogn) time 
        # Counter() takes O(n) time because you are going through every element 
        # Dictionaries have constant time O(1) complexity for key lookup and insertion 

    # HASHMAP SOLUTION (1 DICTIONARY) - 1ST ATTEMP
        # dict_s = Counter(s)

        # for char in t:
        #     # if char is not in dict_s then not an anagram and return False
        #     if char not in dict_s:
        #         return False
        #     # if char is in dict_s then subtract 1 from the count of that letter. If the 
        #     # count for that letter is 0 then remove it from the dictionary
        #     elif char in dict_s: # I actually don't need this elif statement
        #         dict_s[char] -=1 
        #         if dict_s[char] == 0: 
        #             dict_s.pop(char) # this is wrong. It should be 'del dict_s[char]'
            
        #     # if we get through looping through all of t and dict_s is empty then s and t 
        #     # are anagrams. If we iterate through all of t and there are still key-value 
        #     # pairs in dict_s then s and t are not anagrams because s has more letters than t
        #     return True if dict_s == {} else False  # this is incorrect, we want to use the length of dict_s instead 
  
    # SORTING SOLUTION - 1ST ATTEMPT 
        # return True if sorted(s) == sorted(t) else False 
        
        # this could be even cleaner than this already pretty clean code!
        # what is the time and space complexity, time - O(nlogn) for sorting 
        # and if we don't count the temporary storage used to create these sorted strings 
        # then space - O(1) constant time 

    # HASHMAP SOLUTION (MY VERSION) - 1ST ATTEMPT
        # dict_s = {}
        # dict_t = {}

        # for char in s:
        #     if char in dict_s:
        #         dict_s[char] += 1
        #     else:
        #         dict_s[char] = 1 

        # for char in t:
        #     if char in dict_t:
        #         dict_t[char] += 1
        #     else:
        #         dict_t[char] = 1

        # return True if dict_s == dict_t else False
        
        
       
    # SORTING (LONG VERSION)  
        # because this involves sorting, it will have time complexity = O(nlogn) and O(1) space
        # if len(s) == len(t):
        #     sorted_s = sorted(s)
        #     sorted_t = sorted(t)
        #     if sorted(s) == sorted(t):
        #         return True
        # return False