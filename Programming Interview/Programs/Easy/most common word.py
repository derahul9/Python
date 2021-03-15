#In python, the string data types are immutable. Which means a string value cannot be updated. In C it can mutate.

'''To the question: string data is typically immutable because any object we can’t trust to stay the same, because of some “back door” possibility, adds overhead, in terms of our capacity
to reason about the code. The more mutable an object, the more black boxy and uncertain its contents, from the point of view of the code reader'''

'''Immutable Objects : These are of in-built types like int, float, bool, string, unicode, tuple. In simple words, an immutable object can’t be changed after it is created.'''

paragraph = "Bob hit a ball, the hit ball far far far after it was hit"

banned = ["hit", "bob"]

class Common:
    def mostCommonWord(self, paragraph):
        b = paragraph.lower()
        c = b.replace(".", "")
        d = c.replace(",", "")
        a = d.split(" ")
        counter = 0
        for word in a:
            if word not in banned:
                curr_frequency = a.count(word)
                if curr_frequency > counter:
                    counter = curr_frequency
                    final = word
        return final

z = Common()
print(z.mostCommonWord(paragraph))