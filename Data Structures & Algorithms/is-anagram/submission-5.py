class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_count = {}
        t_count = {}

        for s_char, t_char in zip(s, t):
            if s_char in s_count:
                s_count[s_char] += 1
            else:
                s_count[s_char] = 1

            if t_char in t_count:
                t_count[t_char] += 1
            else:
                t_count[t_char] = 1

        return s_count == t_count