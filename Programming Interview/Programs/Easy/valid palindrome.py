str = "A man, a plan, a canal: Panama"
str1 = "Eva, Can I Stab Bats In A Cave"
str2 = "Dammit, I'm Mad!"
str3 = "abca"

class Palindrome():
    def isPalindrome(self, str):
        a = list(str)
        b = []
        for elements in a:
            if elements.isalnum():
                b.append(elements.lower())
        c = len(b)
        for i in range(c):
            n = c - 1 - i
            if b[i] != b[n]:
                return False
        return True


z = Palindrome()
print (z.isPalindrome(str))

