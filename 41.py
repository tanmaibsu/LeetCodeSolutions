def firstMissingPositive(nums: list[int]) -> int:

    nums = list(set(nums))
    nums = [n for n in nums if n >= 0]
    if len(nums) == 0:
        return 1
    nums.sort()

    if nums[0] > 1:
        return 1

    l = len(nums)

    for i in range(l):
        n = nums[i]
        if i == l - 1:
            return n + 1
        elif n + 1 > 0 and n + 1 != nums[i+1]:
            return n + 1

print(firstMissingPositive([1,2,0]))