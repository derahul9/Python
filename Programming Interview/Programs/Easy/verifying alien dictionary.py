words = ["hello","leetcode"]
order = "hlabcdefgijkmnopqrstuvwxyz"

class Solution:
    def alien(self,  words, order):
            index = {v:i for i, v in enumerate(order)}
            print (index)
            for i in range(len(words) -1):
                word1 = words[i]
                word2 = words[i+1]
                for k in range(min(len(word1),len(word2))):
                    if word1[k] != word2[k]:
                        if index[word1[k]] > index[word2[k]]:
                            return False
                        break
                    else:
                        if len(word1) > len(word2):
                            return False
            return True

z = Solution()
print (z.alien(words, order))

