class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1,nums2=nums2,nums1
        tot=len(nums1)+len(nums2)
        half=(tot+1)//2
        low=0
        high=len(nums1)
        while low<=high:
            pa1=(low+high)//2
            pa2=half-pa1
            if pa1==0:
                L1=float("-inf")
            else:
                L1=nums1[pa1-1]
            if pa1==len(nums1):
                R1=float("inf")
            else:
                R1=nums1[pa1]
            if pa2==0:
                L2=float("-inf")
            else:
                L2=nums2[pa2-1]
            if pa2==len(nums2):
                R2=float("inf")
            else:
                R2=nums2[pa2]
            if L1<=R2 and L2<=R1:
                if tot%2==0:
                    return float((max(L1,L2)+min(R1,R2))/2)
                else:
                    return float(max(L1,L2))
            elif L1>R2:
                high=pa1-1
            else:
                low=pa1+1
