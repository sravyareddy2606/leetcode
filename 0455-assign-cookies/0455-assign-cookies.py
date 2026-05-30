class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        l = 0
        m = 0
        glen = len(g)
        slen = len(s)
        while l < glen and m < slen:
            if s[m] >= g[l]:
                l += 1
            m += 1
        return l