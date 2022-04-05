# my solutions -----------------------------------------------

# first
def missingNumber(nums):
    min_num = min(nums)
    max_num = max(nums)
    range_nums = [i for i in range(min_num, max_num+1)]
    nums = set(nums)
    for j in range_nums:
        if j not in nums:
            return j
    if min_num > 0:
        return min_num-1
    return max_num+1

# print(missingNumber([0,1,2,3,5]))

# second
def missingNumber(nums):
    min_n, max_n = min(nums), max(nums)
    set_range = set(range(min_n, max_n+1))
    nums = set(nums)
    try:
        return list(set_range - nums)[0]
    except:
        return 0 if min_n > 0 else max_n+1

# print(missingNumber([9,6,4,2,3,5,7,0,1]))
# print(missingNumber([1,2,3,5]))

# threesome :0 (not mine)
def missingNumber(nums):
    return sum(range(0, len(nums)+1)) - sum(nums)

# print(missingNumber([0,1]))

# internet solutions ----------------------------------------
def missingNumber(nums):
    res = len(nums)

    for i in range(len(nums)):
        res += (i - nums[i])

    return res

# the best solution
def missingNumber(nums):
    n = len(nums)
    s = int(n*(n+1)/2)

    for i in nums:
        s -= i
    
    return s

# can i just die?

# print(missingNumber([0,1,2,3,5]))

# Мои решения работают даже когда нет нуля, будь то хоть - [23,24,26], оно будет работать. СОСАААААТЬ!!!!)))