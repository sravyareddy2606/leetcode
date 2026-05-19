class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = "".join(s.split("-")).upper()
        ss = []
        c = 0
        for i in range(len(s) - 1, -1, -1):
            ss.append(s[i])
            c += 1
            if c % k == 0:
                ss.append("-")
        if ss and ss[-1] == "-":
            ss.pop()
        return "".join(ss[::-1])
    