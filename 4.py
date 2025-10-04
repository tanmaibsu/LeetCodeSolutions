def findMedianSortedArrays(nums1, nums2) -> float:
    sorted_arr = sorted(nums1 + nums2)
    arr_len = len(sorted_arr)

    if(arr_len % 2 ) != 0:
        return float(sorted_arr[arr_len // 2])
    else:
        return (sorted_arr[arr_len // 2] + sorted_arr[(arr_len // 2) - 1]) / 2


print(findMedianSortedArrays([1,3], [2]))