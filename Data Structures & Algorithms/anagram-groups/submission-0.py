class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana_map={} #key=anagram group, value=list of strings in this group

        for word in strs:
            group=''.join(sorted(word)) #turn list of characters into a string
            if group in ana_map:
                ana_map[group].append(word)
            else:
                ana_map[group]=[word]

        return list(ana_map.values())