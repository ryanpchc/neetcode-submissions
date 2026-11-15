class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window_size = len(s1)
        l = 0
        s1_map = {}
        s2_map = {}

        for c in s1:
            s1_map[c] = s1_map.get(c, 0) + 1
        
        for r in range(len(s2)):
            c = s2[r]
            s2_map[c] = s2_map.get(c, 0) + 1

            if r - l + 1 > window_size:
                leaving = s2[l]
                s2_map[leaving] -= 1
                if s2_map[leaving] == 0:
                    del s2_map[leaving]
                l += 1

            if r - l + 1 == window_size and s1_map == s2_map:
                return True

        return False
