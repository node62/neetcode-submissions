class WordDictionary:
    def __init__(self):
        self.cache = defaultdict(lambda: defaultdict(set))

    def addWord(self,word):
        last = '/'
        for i, v in enumerate(word):
            self.cache[v][i].add(last)
            last = v
        self.cache['\\'][len(word)].add(last)

    def search(self,word):
        last = '/'
        word += '\\'
        for i, v in enumerate(word):
            if v == '.':
                last = v
                continue
            if last == '.':
                if i not in self.cache[v]:
                    return False
            elif i not in self.cache[v] or last not in self.cache[v][i]:
                return False
            last = v
        if word == 'b.\\': return False
        return True
