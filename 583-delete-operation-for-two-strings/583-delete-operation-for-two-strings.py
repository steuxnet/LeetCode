class Solution:
    def minDistance(self, w1: str, w2: str) -> int:
        
        b , s  = (w1, w2) if len(w1) >= len(w2) else (w2, w1)
        p = defaultdict(list)
        
        for i, c in enumerate(s):
            p[c].append(i)

        l = [0] * (len(s) + 1)
        for c in b:
            for i in reversed(p[c]):
                l[i+1] = max(l[:i+1]) + 1

        same = max(l[1:])
        return len(b) + len(s) - 2 * same