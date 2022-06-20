class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        words = list(set(words))
        Trie  = lambda: collections.defaultdict(Trie)
        trie  = Trie()
        # For each word put A REFEENCE to her reversed trie traversal in list
        nodes = []
        for word in words:
            current_trie = trie
            for c in reversed(word):
                current_trie = current_trie[c]                
            nodes.append(current_trie)
        #Add word to the answer if it's node has no neighbors
        return sum(len(word) + 1
                   for i, word in enumerate(words)
                   if not nodes[i])