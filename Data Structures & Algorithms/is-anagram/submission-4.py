class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # because this involves sorting, it will have time complexity = O(nlogn) and O(1) space
        if len(s) == len(t):
            sorted_s = sorted(s)
            sorted_t = sorted(t)
            if sorted(s) == sorted(t):
                return True
        return False

        # this is a one-line solution and will return 'True' or 'False'
        # return sorted(s) == sorted(t)

        # there are more efficient solutions but I'm not there yet