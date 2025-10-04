# import math
def productExceptSelf(nums: list[int]) -> list[int]:

    new_nums = [0]*len(nums)
    for i, elm in enumerate(nums):
        mul = 1
        nums[i] = 1
        for j, elm1 in enumerate(nums):
            mul = mul*elm1
        nums[i] = elm

        new_nums[i] = mul
        
    
    return new_nums

print(productExceptSelf([1,2,3,4]))

