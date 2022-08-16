class Solution:
    def firstUniqChar(self, s: str) -> int:
        coun = Counter(s)
        for i,j in enumerate(s):
            if coun[j] == 1:
                return i
        return -1