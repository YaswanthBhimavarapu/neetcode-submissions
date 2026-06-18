class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums = sorted(nums)
        curr = 1
        long = 1

        for i in range(len(nums)):

            if nums[i] == nums[i - 1]:
                continue

            elif nums[i] == nums[i-1]+1:
                curr +=1

            else:
                curr = 1

            if curr > long:
                long = curr

        return long        