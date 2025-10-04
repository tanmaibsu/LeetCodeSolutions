def threeSum(nums: list[int]) -> list[list[int]]:

    sum = 0
    i = 0
    for num1 in range(0, len(nums) - 1):
        j = i + 1
        for nums2 in range(j, len(nums) - 1):
            print((i, j))
            j = j + 1
        
        i += 1


print(threeSum([-1,0,1,2,-1,-4]))
