class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        indices = list(range(len(intervals)))
        start_indices = sorted(indices, key=lambda i: intervals[i][0])
        end_indices = sorted(indices, key=lambda i: [intervals[i][1], intervals[i][0]])
        output = [-1 for _ in range(n)]
        j = 0
        for i in end_indices:
            while j < n and intervals[start_indices[j]][0] < intervals[i][1]:
                j += 1
            if j >= n:
                break
            output[i] = start_indices[j]
        return output