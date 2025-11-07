a = "ffacebook"
b = "facebook"

def test(a, b):
    x = {}
    for letters in a:
        if letters in x:
            x[letters] += 1
        else:
            x[letters] = 1
    y = dict(sorted(x.items(), key=lambda item: item[1], reverse=True))
    for k,v in y.items():
        if k != "o":
            return v
        else:
            return v // 2

print (test(a,b))


