class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        def issub(x, y):
            it = iter(y)
            return all(c in it for c in x)
        c=0
        wordsset = set(words)
        for i in wordsset:
            if issub(i,s):
                c = c+words.count(i)
        return c