class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        l=[]
        for i in range(0,n):
            for j in range(i+1,n):
                if nums[i]+nums[j]==target:
                    l.append(i)
                    l.append(j)
                    return l

# alternative and better solution using dict
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         map={}

#         for i, n in enumerate(nums):
#             difference=target-n
#             if difference in map:
#                 return sorted([i,map[difference]])
#             map[n]=i