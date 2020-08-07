class WordDictionary:
    '''
    [1:00]: The goal is to efficiently insert a word and lookup the word
    Fast insertion can be done using a hashmap and lookups can also be done with
    a hashmap.
    However, the challenge is to search for words that contain .
    A brute force solution would be to generate a list of all combinations of words
    and store it in the hashmap which would take exponential time to generate but
    guarantees O(1) lookup
    Another solution would be develop a better string matching algorithm where
    insertion into hashmap will be O(1) but string matching might be exponential.
    Therefore we need to find a middle ground with space and time complexity.
    We could  consider using a trie because it's space efficient and also provides fast
    lookups.
    [6:00]
    The challenge would be to figure out how to validate the word when we encounter a 
    wildcard.
    For eg:
            b  d m
           /  / /
          a  a a
         /  / /
        d* d* d*
    We would need to implement a trie and do a dfs. If a wild card is encountered we
    skip the current node and move to the next word.
    We also make sure we can use subwords within the tree to avoid taking up extra space. 
    This can be done using a * to mark the end of a valid word.
    [11:00] Attempting to code it out
    [20:00] Implemented basic trie node
    [26:00] I'm stuck not sure how to implement add word.
    '''
    class TrieNode(self):
        def __init__(self, ch):
            ch = self.ch
            next_trie_node = [None for _ in range(26)]
            
        def add_next(self, trie_node):
            idx = ord(trie_node.ch) - 97
            self.next_trie_node[idx] = trie_node

    def __init__(self):
        """
        Initialize your data structure here.
        Implementing a trie
        """
        root = [None for _ in range(26)]
        
        

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        if not word:
            return None
        ch = word[0]
        idx = ord(ch) - 97 # check if first ch exists in root.
        if not root[idx]:
            trie_node = TrieNode(ch)
            root = trie_node
            #self.
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
