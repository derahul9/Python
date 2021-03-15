Input = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]

class Email:
    def uniqueEmail(self, Input):
        x = []
        for elements in Input:
            name, email = elements.split("@")
            if "+" in name:
                name = (name.split("+")[0])
            if "." in name:
                name1 = name.replace(".", "")
            name2 = name1 + '@' + email
            x.append(name2)
            y = set(x)
        return len(y)

z = Email()
print (z.uniqueEmail(Input))