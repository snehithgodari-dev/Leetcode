from itertools import accumulate

class NumArray:

    def __init__(self, nums: list[int]):
        # Precompute prefix sums starting with 0 using accumulate
        self.pref = list(accumulate(nums, initial=0))

    def sumRange(self, left: int, right: int) -> int:
        # Calculate sum in O(1) time
        return self.pref[right + 1] - self.pref[left]