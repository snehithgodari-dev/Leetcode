class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        if not nums:
            return []

        grps = []
        start = nums[0]
        prev = nums[0]

        for b in nums[1:]:
            if b != prev + 1:
                grps.append(f"{start}->{prev}" if start != prev else f"{start}")
                start = b
            prev = b

        grps.append(f"{start}->{prev}" if start != prev else f"{start}")
        return grps