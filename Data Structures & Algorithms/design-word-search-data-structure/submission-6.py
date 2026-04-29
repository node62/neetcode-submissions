class WordDictionary:
    def __init__(self):
        self.cache = defaultdict(lambda: defaultdict(set))

    def addWord(self,word):
        word += '\\'
        last = '/'
        for i, v in enumerate(word, start=1):
            self.cache[v][i].add(last)
            last += v

    def search(self,word):
        word += '\\'
        lastc = '/'
        lasti = 0
        for i, v in enumerate(word, start=1):
            if v == '.':
                continue
            
            if i in self.cache[v]:
                toggle = False
                for w in self.cache[v][i]:
                    if lastc == w[lasti]:
                        toggle = True
                        break
                if not toggle:
                    return False
            
            else: return False
            
            lastc = v
            lasti = i
        
        return True