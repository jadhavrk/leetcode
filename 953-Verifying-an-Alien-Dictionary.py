class Solution:
    def compare(self,w1, w2, h):
        i, j = 0, 0
        while (w1[i] and w2[j]):
            #print(w1[i], h[w1[i]], w2[j], h[w2[j]])
            if h[w1[i]] < h[w2[j]]:
                #print("Enter 1")
                return True
            elif h[w1[i]] > h[w2[j]]:
                #print("Enter 2")
                return False
            else:
                #end of the word
                if i + 1 < len(w1) and j + 1 < len(w2):
                    #print("enter 3-A")
                    i += 1
                    j += 1
                elif not i + 1 < len(w1) and j + 1 < len(w2):
                    #print("enter 3-B")
                    return True
                else:
                    #print("enter 3-C")
                    return False
        return True
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        '''
        [2:00]: This looks like a sorting problem where 
        a custom ordering is provided and we have to figure out whether
        the words in the list are sorted according to this order.
        
        Algorithm
        We need a function (say compare(w1, w2))that compares takes two words and checks if 
        w1 < w2.
        
        We need to perform this every word
        
        #edge cases:
        same words
        words of different length
        [20:00]: done w/ code. Wrong answer
        Stuck on implemeting comparator function
        [25:00]: Working solution bug free
        '''
        
        # Edge cases
        if not words:
            return True
        
        if len(words) == 1:
            return True
        
        #create hasmap of order
        h = {}
        for i, ch in enumerate(order):
            h[ch] = i
        
        for i, word in enumerate(words[1:],1):
            if not self.compare(words[i - 1], word, h):
                return False
            
        return True
        
