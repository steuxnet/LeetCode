class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
                        
        queue = collections.deque([])        
        window = set()
        result = 0
        
        for c in s:            
            if c in window:
                while queue:
                    prev = queue.popleft()
                    window.remove(prev)
                    if prev == c:
                        break
                            
            queue.append(c)
            window.add(c)
            result = max(result, len(window))
            
        return result