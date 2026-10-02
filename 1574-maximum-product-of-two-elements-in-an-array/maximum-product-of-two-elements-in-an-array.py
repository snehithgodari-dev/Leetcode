class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        nums.sort()
        maxproduct = ((nums[-1])-1) * ((nums[-2])-1)
        return maxproduct