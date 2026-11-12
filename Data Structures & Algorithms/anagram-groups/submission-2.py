class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = defaultdict(list)

        for str in strs:
            sort_str = sorted(str)
            joined_sort_str = ''.join(sort_str)
            dict[joined_sort_str].append(str)
        return list(dict.values())

        