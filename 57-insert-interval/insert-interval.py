class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        merged = []
        start, end = newInterval

        for s, e in intervals:
            if e < start:
                # Current interval ends before our active interval starts
                merged.append([s, e])
            elif s > end:
                # Current interval starts after our active interval ends
                merged.append([start, end])
                start, end = s, e
            else:
                # Overlapping: expand the active interval
                start = min(start, s)
                end = max(end, e)

        merged.append([start, end])
        return merged