class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
    # Counter Method 
        # count_s = Counter(s)
        # count_t = Counter(t)

        # return True if count_s == count_t else False 

    # Sorted Method
        # sorted_s = sorted(s)
        # sorted_t = sorted(t)
        # return True if sorted_s == sorted_t else False

    # Dictionary Method
        dict_s = Counter(s)

        for elt in t:
            if elt in dict_s:
                dict_s[elt] -= 1 
                if dict_s[elt] == 0:
                    del dict_s[elt]
            else:
                return False 
        
        return False if dict_s else True 







