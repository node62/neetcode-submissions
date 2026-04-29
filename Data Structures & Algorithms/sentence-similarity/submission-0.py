from collections import defaultdict
class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2):
            return False
        
        cache = defaultdict(list)
        for x, y in similarPairs:
            cache[x].append(y)
            cache[y].append(x)
        
        for a, b in zip(sentence1, sentence2):
            if a!=b and (b not in cache[a]):
                print(a, b)
                return False
        return True