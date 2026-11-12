class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_dict = defaultdict(list)

        for str in strs:
            string_sorted_in_list = sorted(str) # will give you an array that contains each letter of the string in alphabetical order 
            new_alphabetical_string = ''.join(string_sorted_in_list)
            my_dict[new_alphabetical_string].append(str)

        return list(my_dict.values())

        

        