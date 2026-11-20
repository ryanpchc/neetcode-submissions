class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # init window size + maps
        size = len(s1)
        l = 0
        s1_map = {}
        s2_map = {}

        # populate map
        for c in s1:
            s1_map[c] = s1_map.get(c, 0) + 1

        # iterate through s2 and search for permutation
        for i in range(len(s2)):
            # compare freq maps
            if len(s2_map) == size:
                if s1_map == s2_map:
                    return True
                else:
                    leaving = s2[l]
                    s2_map[leaving] -= 1
                    if s2_map[leaving] == 0:
                        del s2_map[leaving]
                    l += 1

            s2_map[s2[i]] = s2_map.get(s2[i], 0) + 1
            
        return False