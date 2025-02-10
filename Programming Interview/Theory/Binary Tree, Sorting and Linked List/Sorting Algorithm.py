#https://www.studytonight.com/data-structures

'''
Bublesort
Selectsort
Insertsort
MergeSort
Quicksort
Heapsort
Countsort
'''
n = [5,1,6,2,4,3]

# time complexity of Bubble Sort is O(n2)
# space complexity for Bubble Sort is O(1), because only a single additional memory space is required i.e. for temp variable

class Solution:
    def BubbleSort(self, n):
        for i in range(len(n)):
            for j in range(len(n)-i-1):
                if n[j] > n[j+1]:
                    temp = n[j]
                    n[j] = n[j+1]
                    n[j+1] = temp
            print (n)
        return n

z = Solution()
print (z.BubbleSort(n))

n1 = [11, 17, 18, 26, 23]
#Optimized bubble using a flag
class Solution1:
    def OptimizedBubbleSort(self, n):
        for i in range(len(n)):
            flag = 0
            for j in range(len(n)-i-1):
                if n[j] > n[j+1]:
                    temp = n[j]
                    n[j] = n[j+1]
                    n[j+1] = temp
                    flag = 1
            if flag == 0:
                break
            #print (n)
        return n

z = Solution1()
print (z.OptimizedBubbleSort(n1))

n2 = [3, 6, 1, 8, 4, 5]
#Selection Sort
#Average Time Complexity [Big-theta]: O(n2)
#Space Complexity: O(1)
class Solution2:
    def SelectionSort(self, n):
        for i in range(len(n)-1):
            for j in range(i+1, len(n)):
                if n[i] > n[j]:
                    temp = n[i]
                    n[i] = n[j]
                    n[j] = temp
            #print (n)
        return n

z = Solution2()
print (z.SelectionSort(n2))

n3 = [12, 11, 13, 5, 6]
#Insertion Sort
#Average Time Complexity: O(n2)
#Space Complexity: O(1)
class Solution3:
    def insertionSort(self, n):
        for i in range(1, len(n)):
            key = n[i]
            j = i - 1
            while j >= 0 and key < n[j]:
                n[j + 1] = n[j]
                j -= 1
            n[j + 1] = key
        return n

z = Solution3()
print (z.insertionSort(n3))

n4 = [12, 11, 13, 5, 6]
#Merge Sort
#Time complexity of Merge Sort is O(n*Log n) in all the 3 cases (worst, average and best) as merge sort always divides the array in two halves and takes linear time to
#merge two halves.
#It requires equal amount of additional space as the unsorted array. Hence its not at all recommended for searching large unsorted arrays.
class Solution4:
    def mergeSort(self, arr):
        if len(arr) > 1:
            mid = len(arr) // 2
            L = arr[:mid]
            R = arr[mid:]
            self.mergeSort(L)
            self.mergeSort(R)
            i = j = k = 0
            while i < len(L) and j < len(R):
                if L[i] < R[j]:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
                k += 1
            while i < len(L):
                arr[k] = L[i]
                i += 1
                k += 1
            while j < len(R):
                arr[k] = R[j]
                j += 1
                k += 1
        return arr

z = Solution4()
print (z.mergeSort(n4))

n5 = [5, 4, 3, 2, 1]
#Quick Sort
#For an array, in which partitioning leads to unbalanced subarrays, to an extent where on the left side there are no elements, with all the elements greater than the pivot,
#hence on the right side.
#And if keep on getting unbalanced subarrays, then the running time is the worst case, which is O(n2)
#Where as if partitioning leads to almost equal subarrays, then the running time is the best, with time complexity as O(n*log n).
#Worst Case Time Complexity [ Big-O ]: O(n2)
#Best Case Time Complexity [Big-omega]: O(n*log n)
#Average Time Complexity [Big-theta]: O(n*log n)
#Space Complexity: O(n*log n)

class Solution5:
    def partition(self, array, start, end):
        pivot = array[start]
        low = start + 1
        high = end
        while True:
            while low <= high and array[high] >= pivot:
                high = high - 1
            while low <= high and array[low] <= pivot:
                low = low + 1
            if low <= high:
                array[low], array[high] = array[high], array[low]
            else:
                break
        array[start], array[high] = array[high], array[start]
        return high

    def quickSort(self, array, start, end):
        if start >= end:
            return
        p = self.partition(array, start, end)
        self.quickSort(array, start, p - 1)
        self.quickSort(array, p + 1, end)
        return array

z = Solution5()
print (z.quickSort(n5, 0, len(n5) - 1))

#Heap Sort
'''
Heap is a special tree-based data structure, that satisfies the following special heap properties:
Shape Property: Heap data structure is always a Complete Binary Tree, which means all levels of the tree are fully filled
Heap is a special tree-based data structure, that satisfies the following special heap properties:
Shape Property: Heap data structure is always a Complete Binary Tree, which means all levels of the tree are fully

How Heap Sort Works?
Heap sort algorithm is divided into two basic parts:

Creating a Heap of the unsorted list/array.
Then a sorted array is created by repeatedly removing the largest/smallest element from the heap, and inserting it into the array. 
The heap is reconstructed after each removal.
Initially on receiving an unsorted list, the first step in heap sort is to create a Heap data structure(Max-Heap or Min-Heap). Once heap is built, 
the first element of the Heap is either largest or smallest(depending upon Max-Heap or Min-Heap), so we put the first element of the heap in our array. 
Then we again make heap using the remaining elements, to again pick the first element of the heap and put it into the array. We keep on doing the same repeatedly 
untill we have the complete sorted list in our array.

Complexity Analysis of Heap Sort
Worst Case Time Complexity: O(n*log n)
Best Case Time Complexity: O(n*log n)
Average Time Complexity: O(n*log n)
Space Complexity : O(1)
'''

#Count Sort
'''
Counts the frequency and sorts
Advantages of Counting Sort:
It is quite fast
It is a stable algorithm
Note: For a sorting algorithm to be stable, the order of elements with equal keys (values) in the sorted array should be the same as that of the input array.

Disadvantages of Counting Sort:
It is not suitable for sorting large data sets
It is not suitable for sorting string values
'''





