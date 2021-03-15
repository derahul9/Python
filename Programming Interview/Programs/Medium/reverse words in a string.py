s = "the sky is blue"

def reverseWords(s):
    l = s.split(" ")
    m = l[::-1]
    return " ".join(m)

#print (reverseWords(s))

t = ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]

class Words1:
    def reverseWords1(self, t):
        x = []
        a = "".join(t)
        b = a.split(" ")
        c = b[::-1]
        print (c)
        for elements in c:
            x.append(list(elements))
            x.append(" ")
        return x

z = Words1()
print (z.reverseWords1(t))


