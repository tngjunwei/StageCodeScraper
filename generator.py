import itertools
import random

class CodeGenerator:
    def __init__(self):
        self.all_words = self._generate_all_words()
        self.PREFIX = "NTU"
        self.word_idx = 0

    def _generate_all_words(self):
        res = []
        for p in itertools.product([chr(i) for i in range(65, 90+1)], repeat=4):
            res.append("".join(p))
        return res
    
    def generate_and_shuffle(self, num):
        self.word_idx = 0
        random.shuffle(self.all_words)
        self.samples = [f"{self.PREFIX}{word}{num}" for word in self.all_words]

    def generate_batch(self, batch=100):
        max_idx = min(batch+self.word_idx, len(self.all_words))
        res = self.all_words[self.word_idx : max_idx]
        self.word_idx = max_idx+1
        return res
    
    def done(self):
        return self.word_idx >= len(self.all_words)