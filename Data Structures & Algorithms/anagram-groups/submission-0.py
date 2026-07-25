class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # sort word so we can group anagrams 
        # (refer to same key in a dictionary)
        # values will have og strings, at the end we can just return list(dict.values())
        s = {};
        for word in strs:
            key = tuple(sorted(word))
            if(key in s):
                s[key].append(word)
            else:
                s[key] = [word]
        return list(s.values())
