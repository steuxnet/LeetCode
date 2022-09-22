class Solution:
    def reverseWords(self, s: str) -> str:
        r_words = [word[::-1] for word in s.split()]
        return " ".join(r_words)