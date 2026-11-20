class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        n = len(nums)
        num_set = set(nums)
        for x in range(1, n + 2):
            if x not in num_set:
                return x