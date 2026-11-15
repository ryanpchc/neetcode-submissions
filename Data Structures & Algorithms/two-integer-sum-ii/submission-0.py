class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1

        for i in range(len(numbers)):
            target_sum = numbers[l] + numbers[r]

            if target_sum == target:
                return [l + 1, r + 1]

            elif target_sum < target:
                l += 1

            else:
                r -= 1

        