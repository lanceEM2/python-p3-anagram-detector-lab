# your code goes here!

class Anagram:
    def __init__(self, word):
        self.word = word.lower()

    def match(self, candidates):
        return [candidate for candidate in candidates if self.is_anagram(candidate)]

    def is_anagram(self, candidate):
        candidate_lower = candidate.lower()
        return candidate_lower != self.word and sorted(candidate_lower) == sorted(self.word)

# Example usage:
listen = Anagram("listen")
result = listen.match(['enlists', 'google', 'inlets', 'banana'])
print(result)
