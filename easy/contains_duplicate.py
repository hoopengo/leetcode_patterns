# my solution ------------------------------------
def containsDuplicate(nums):
    # print(sorted(list(set(nums))), sorted(nums))
    return False if sorted(nums) == sorted(list(set(nums))) else True

# print(containsDuplicate([1,5,-2,-4,0]))


# internet solution -------------------------------
def containsDuplicate(nums):
    # print(sorted(list(set(nums))), sorted(nums))
    hash_set = set()
    for num in nums:
        if num not in hash_set:
            hash_set.add(num)
        else:
            return True
    return False

# print(containsDuplicate(test_nums))