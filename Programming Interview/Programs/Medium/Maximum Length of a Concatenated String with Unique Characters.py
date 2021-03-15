arr = ["abcdefghijklmnopqrstuvwxyz"]
arr1 = ["cha","r","act","ers"]
arr2 = ["un","iq","ue"]
arr3 = ["a", "abc", "d", "de", "def"]

class Solution:
    def con(self, arr):
        maximum = 0
        string = ""
        for index, string1 in enumerate(arr):
            if len(string) == len(set(string)):
                for index2, string2 in enumerate(arr):
                    if index != index2:
                        if len(string1 + string2) == len(set(string1 + string2)):
                            print (string1, string2)
                            string = string1 + string2
                    maximum = max(len(string), maximum)
                    string = ""
        return maximum

z = Solution()
print (z.con(arr3))