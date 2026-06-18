class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        l2 = []
        for i in range(len(nums)):
            if nums[i] in l2:
                return True
                break
            else:
                l2.append(nums[i])
        return False