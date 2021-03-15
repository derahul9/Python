S = "ab#c"
T = "ab#c#c"

class Space:
    def backSpace(self, S, T):
        S = list(S)
        T = list(T)
        a = []
        b = []
        for i in range(0, (len(S))):
            if S[i] != "#":
                a.append(S[i])
            if S[i] == "#":
                a.remove(S[i-1])
        for j in range(0, (len(T))):
            if T[j] != "#":
                b.append(T[j])
            if T[j] == "#":
                b.remove(T[j-1])
        return a == b

z = Space()
print (z.backSpace(S, T))

class Space:
    def backSpace(self, S, T):
        def helper(A):
            x = []
            for i in range(0, (len(A))):
                if A[i] != "#":
                    x.append(A[i])
                if x:
                    x.pop()
            return x
        return helper(S) == helper(T)

z = Space()
print (z.backSpace(S, T))

