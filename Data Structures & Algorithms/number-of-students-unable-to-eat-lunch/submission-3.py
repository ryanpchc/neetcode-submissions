from collections import deque

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        queue = deque(students)
        sandwiches_idx = 0
        no_match_idx = 0

        while queue and no_match_idx < len(queue):
            if queue[0] == sandwiches[sandwiches_idx]:
                queue.popleft()
                sandwiches_idx += 1
                no_match_idx = 0
            else:
                queue.rotate(-1)
                no_match_idx += 1

        return len(queue)