nums = [4,5,6,7,0,1,2]
target = 1

#print (nums.index(min(nums))) - Binary tree keeping this value to be the index

def rotateSort(nums, target):
    for i in range(1, len(nums)):
        if nums[i] < nums[i-1]:
            index = i
    if target == nums[index]:
        return index
    elif target > nums[0]:
        for i in range(0, index):
            if target == nums[i]:
                return i
    elif target < nums[0]:
        for i in range(index +1, len(nums) +1):
            if target == nums[i]:
                return i

print (rotateSort(nums, target))

