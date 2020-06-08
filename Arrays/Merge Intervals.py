class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        s = []
        i = 0
        while i < len(intervals):
            if not s:
                s.append(intervals[0])
                i = i + 1
            elif s[-1][-1] >= intervals[i][0] and s[-1][-1] <= intervals[i][1]:
                s[-1] = [s[-1][0], intervals[i][-1]]
                i = i + 1
            elif s[-1][-1] >= intervals[i][0] and s[-1][-1] >= intervals[i][0]:
                s[-1] = s[-1]
                i = i + 1
            else:
                s.append(intervals[i])
                i = i + 1
        return(s)
