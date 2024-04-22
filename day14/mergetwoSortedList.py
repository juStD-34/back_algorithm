def merge(self, nums1, m, nums2, n):
    index1 = m - 1
    index2 = n - 1
    index = m + n - 1
    while (index1 >= 0 and index2 >= 0):
        if (nums1[index1] < nums2[index2]):
            nums1[index] = nums2[index2]
            index2 -= 1
            index -= 1
        else:
            nums1[index] = nums1[index1]
            index1 -= 1
            index -= 1
    while (index2 >= 0):
        nums1[index] = nums2[index2]
        index -= 1
        index2 -= 1
    return nums1

print(merge(0, [1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3))
