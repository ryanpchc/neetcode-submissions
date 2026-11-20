class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        size = len(s1) # window size = s1 length
        # create maps for s1 and s2 to compare
        s1_map = {}
        s2_map = {}
        l = 0

        # initialize s1 map
        for c in s1:
            s1_map[c] = s1_map.get(c, 0) + 1

        # iterate through s2
        for r in range(len(s2)):
            # add r to s2_map
            s2_map[s2[r]] = s2_map.get(s2[r], 0) + 1

            # if maps are equal, return
            if len(s2_map) == size:
                if s1_map == s2_map:
                    return True
                else:
                    leaving = s2[l]
                    s2_map[leaving] -= 1
                    if s2_map[leaving] == 0:
                        del s2_map[leaving]
                        l += 1
            
        return False
            
            
        


