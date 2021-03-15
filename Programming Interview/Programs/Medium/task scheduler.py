tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"]
n = 2

class Solution:
    def task(self, tasks, n):
        if n == 0:
            return len(tasks)
        a = []
        for data in tasks:
            if data not in a:
                a.append(data)
        b = []
        print(a)
        for elem in a:
            b.append(tasks.count(elem))
        b.sort(reverse=1)
        print(b)
        idle = (b[0] -1)*n
        print (idle)
        for i in range(1,len(b)):
            idle -= min((b[0] -1), b[i])
        return idle + len(tasks)

z = Solution()
print (z.task(tasks, n))


