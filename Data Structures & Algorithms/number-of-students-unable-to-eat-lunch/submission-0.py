from collections import deque

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        queue = deque(students)
        sandwich_idx = 0
        no_match_count = 0

        while queue and no_match_count < len(queue):
            if queue[0] == sandwiches[sandwich_idx]:
                queue.popleft()
                sandwich_idx += 1
                no_match_count = 0
            else:
                queue.rotate(-1)
                no_match_count += 1

        if not queue:
            return 0
        else:
            return no_match_count