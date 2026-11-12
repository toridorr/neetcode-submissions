class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Counter method 
        # return True if Counter(s) == Counter(t) else False 

        # Sorting method
        # return True if sorted(s) == sorted(t) else False 

        # dictionary solution 
        dict_s = Counter(s)

        for i in t:
            if i in t:
                dict_s[i] = dict_s[i] - 1 
                if dict_s[i] == 0:
                    del dict_s[i]
            else:
                return False 
        
        return True if len(dict_s) == 0 else False










