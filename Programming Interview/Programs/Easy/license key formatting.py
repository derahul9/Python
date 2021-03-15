S = "5F-3Z-2e-9-whkgl"
K = 4

class Key:
    def licenseKeyFormatting(self, S, K):
        S = S.replace('-', '')
        S = S.upper()
        left = 0
        arr = []
        while left < len(S):
            arr.append(S[left:left+K])
            left = left + K
        return '-'.join(arr)

z = Key()
print (z.licenseKeyFormatting(S, K))