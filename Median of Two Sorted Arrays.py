"""There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

Example 1:
nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:
nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5"""




class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        nums3 = nums1 + nums2
        nums3 = sorted(nums3)
        l = len(nums3)
        b = l/2
        print b
        if l % 2 == 0:
            total = float(nums3[b-1] + nums3[b])
            median = float(total)/2
            return median
        else:
            median = nums3[b]
            return median
