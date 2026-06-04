class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        total, n = sum(machines), len(machines)
        if total % n: return -1
        avg, t, tp, ans = total//n, 0, 0, 0
        for num in machines:
            t += num-avg
            T = tp+t if tp >= 0 and t >= 0 else max(abs(tp), abs(t))
            if T > ans: ans = T
            tp = -t
        return ans