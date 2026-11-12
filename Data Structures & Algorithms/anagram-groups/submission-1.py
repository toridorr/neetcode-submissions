class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = defaultdict(list)

        for str in strs:
            sorted_joined_str = ''.join(sorted(str))
            dict[sorted_joined_str].append(str)
        
        return list(dict.values())
    
        # Example: strs = ["act","pots","tops","cat","stop","hat"]
        # 1st loop: str = "act"
        # sorted(str) = ['a', 'c', 't']
        # sorted_joined_str = 'act' -> new so add sorted_joined_str as key and str as key in its list
        # dict = {'act': ['act']}
        # 2nd loop: str = "pots"
        # sorted(str) = ['o', 'p', 's', 't']
        # sorted_joined_str = 'opst' -> new so add sorted_joined_str as key and str as key in its list
        # dict = {'act': ['act'], 'opst': ['pots']}
        # 3rd loop: str = "tops"
        # sorted(str) = ['o', 'p', 's', 't']
        # sorted_joined_str = 'opst'  -> this is already a key in dict, so add 'tops' to it's value list
        # dict = {'act': ['act'], 'opst': ['pots', 'tops']}
        # 4th loop: str = "cat"
        # sorted(str) = ['a', 'c', 't']
        # sorted_joined_str = 'act' -> already a key in dict, so add 'cat' to its value list
        # dict = {'act': ['act', 'cat'], 'opst': ['pots', 'tops']}
        # 5th loop: str = "stop"
        # sorted(str) = ['o', 'p', 's', 't']
        # sorted_joined_str = 'opst'  -> this is already a key in dict, so add 'stop' to it's value list
        # dict = {'act': ['act', 'cat'], 'opst': ['pots', 'tops', 'stop']}
        # 6th loop: str = "hat"
        # sorted_str = ['a', 'h', 't']
        # sorted_joined_str = 'aht' -> new key so add to dict
        # dict = {'act': ['act', 'cat'], 'opst': ['pots', 'tops', 'stop'], 'aht': ['hat']}
        # return only the keys of dict in list form [['act', 'cat'], ['pots', 'tops', 'stop'], ['hat']]


    

    # EASIER VERSION - INITIAL ATTEMPT    
        # dict = defaultdict(list) # from collections import defaultdict

        # for word in strs:
        #     sorted_word = "".join(sorted(word)) 
        #     # check if the word is an anagram of an existing key, if so then append it to the 
        #     # value list 
        #     # if sorted_word in dict:
        #     #     dict[sorted_word].append(word) # I am actually shocked that this may be right! 
        #     # if it's anagram does not exist, then add it to the dictionary, but add it's 
        #     # sorted version as the key 
        #     # else:
        #     #     dict[sorted_word].append(word)
        #     dict[sorted_word].append(word)

        # # At the end you are going to return just all the values in the dictionary 
        # return list(dict.values())


