class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = {}

        for s in strs:
            count = [0] * 26
            
            for c in s:
                count[ord(c) - ord("a")] += 1
            
            count = tuple(count)
            # if anagram is in map
            if count not in anagram_map:
                anagram_map[count] = [s]

            # else if anagram not in map
            else:
                anagram_map[count].append(s)

        return list(anagram_map.values())
