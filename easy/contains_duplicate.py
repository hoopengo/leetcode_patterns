# https://leetcode.com/problems/contains-duplicate/
# my solution
def containsDuplicate(nums):
    return False if sorted(nums) == sorted(list(set(nums))) else True


# internet solution
def containsDuplicate(nums):
    hash_set = set()
    for num in nums:
        if num not in hash_set:
            hash_set.add(num)
        else:
            return True
    return False