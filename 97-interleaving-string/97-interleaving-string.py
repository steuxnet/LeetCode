class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        memo = {}
        return self.helper(s1, s2, s3, 0, 0, 0, '', {})
        
    
    def helper(self, s1, s2, s3, index1, index2, index3, current, memo):
        if current == s3 and index1 == len(s1) and index2 == len(s2):
            return True
        if current and current[-1] != s3[index3 - 1]:
            return False
        ans = False
        if (index1, index2) in memo:
            return memo[(index1, index2)]
        if index1 < len(s1):
            ans = ans or self.helper(s1, s2, s3, index1 + 1, index2, index3 + 1, current + s1[index1], memo)
        if index2 < len(s2):
            ans = ans or self.helper(s1, s2, s3, index1, index2 + 1, index3 + 1, current + s2[index2], memo)
        
        memo[(index1, index2)] = ans
        return ans