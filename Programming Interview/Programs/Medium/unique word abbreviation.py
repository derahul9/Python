class ValidWordAbbr:

    def __init__(self, dictionary):
        self.b = []
        c = []
        self.dictionary = dictionary
        for word in dictionary:
            x = len(word) - 2
            c.append(word[0])
            c.append(str(x))
            c.append(word[len(word) - 1])
            abb1 = "".join(c)
            self.b.append(abb1)
            c = []
            self.j = {i:v for i,v in enumerate(self.b)}
        print (self.j)

    def isUnique(self, word):
        a = []
        if len(word) < 3:
            abb = word
        else:
            x = len(word) -2
            a.append(word[0])
            a.append(str(x))
            a.append(word[len(word)-1])
            abb = "".join(a)
            a = []
        if abb not in self.b:
            return True
        for i, v in self.j.items():
            if abb == v:
                if word == self.dictionary[i]:
                    return True
        return False

validWordAbbr = (ValidWordAbbr(["deer", "door", "cake", "card"]))
print (validWordAbbr.isUnique("dear"))
print (validWordAbbr.isUnique("cart"))
print (validWordAbbr.isUnique("cane"))
print (validWordAbbr.isUnique("make"))
