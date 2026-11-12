class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dict = defaultdict(list) # from collections import defaultdict

        for word in strs:
            sorted_word = "".join(sorted(word)) 
            # check if the word is an anagram of an existing key, if so then append it to the 
            # value list 
            # if sorted_word in dict:
            #     dict[sorted_word].append(word) # I am actually shocked that this may be right! 
            # if it's anagram does not exist, then add it to the dictionary, but add it's 
            # sorted version as the key 
            # else:
            #     dict[sorted_word].append(word)
            dict[sorted_word].append(word)

        # At the end you are going to return just all the values in the dictionary 
        return list(dict.values())

            # Example: strs = ["act","pots","tops","cat","stop","hat"]
            # 1st loop: word = "act"
            # sorted_word = "act"
            # the key is empty so run the else statement -> add 'act': 'act' as a new
            # key-value pair in the dictionary 
            # dict = {'act': ['act']}
            # 2nd loop: word = "pots"
            # sorted_word = 'opst'
            # this is not a key in the dictionary so run else statement -> add 'opst' : 'pots'
            # as a new key-value pair in the dictionary 
            # dict = {'act': ['act'], 'opst': ['pots']}
            # 3rd loop: word = 'tops'
            # sorted_word = 'opst'
            # this is a key in the dictionary so run the if statement -> add 'tops' as a value 
            # of the 'opst' key
            # dict = {'act': ['act'], 'opst': ['pots', 'tops']}


