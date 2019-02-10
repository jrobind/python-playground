# algorithms

# Find maximum number from list of numbers: 
# findMax([34, 45, 3, 6]) // 45 

def findMax(nums):
    current = nums[0]
    for n in nums:
        if (n > current):
            current = n

    return current

print(findMax([34, 45, 3, 6]))

# Return index if specific item exits in list:
# linear_search(['James', 'Joe', 'Kate', 'Lisa', 'Kevin'], 'Kevin') // 4
# linear_search(['James', 'Joe', 'Kate', 'Lisa', 'Kevin'], 'Tony') // -1

def linear_search(l, val):
    for i, item in enumerate(l):
        if (item == val):
            return i
    return -1

print(linear_search(['James', 'Joe', 'Kate', 'Lisa', 'Kevin'], 'Kevin'))
print(linear_search(['James', 'Joe', 'Kate', 'Lisa', 'Kevin'], 'Tony'))

