class WordFilter:

    def __init__(self, words: List[str]):
        
        self.pref_suf = {}
        for k, word in enumerate(words):
            for i in range(len(word)):
                for j in range(len(word)):
                    self.pref_suf[(word[:i+1], word[j:])] = k+1


    def f(self, prefix: str, suffix: str) -> int:
        if self.pref_suf.get((prefix, suffix), False):
            return self.pref_suf[(prefix, suffix)]-1
        return -1


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)