class WordDictionary:
    def __init__(self):
        self.seen = set()        

    def addWord(self, word: str) -> None:
        self.seen.add(word)     

    def search(self, word: str) -> bool:
        potential = self.seen.copy()
        for i, v in enumerate(word):
            to_remove = set()
            for w in potential:
                if i >= len(w):
                    to_remove.add(w)
                    continue
                if v == '.':
                    continue
                if v != w[i]:
                    to_remove.add(w)
            
            for w in to_remove:
                potential.discard(w)
        
        for w in potential:
            if len(w)== len(word):
                return True
        return False
        
