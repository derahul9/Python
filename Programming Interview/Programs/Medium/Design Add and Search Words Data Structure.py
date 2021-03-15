class WordDictionary:
    def __init__(self):
        self.a = []

    def addWord(self, word):
        self.a.append(word)

    def search(self, word):
        for data in self.a:
            j = 0
            if len(data) == len(word):
                for i in range(len(word)):
                    if word[i] == data[i] or word[i] == ".":
                        j += 1
                if j == len(data):
                    return True
        return False

obj = WordDictionary()
obj.addWord("bad")
obj.addWord("dad")
obj.addWord("mad")
print (obj.search(".ad"))
print (obj.search("b.."))
print (obj.search("pad"))