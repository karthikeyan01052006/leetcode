class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        ones = sum(nums)

        if ones <= 1:
            return 0

        curr = sum(nums[:ones])
        maxi = curr

        for i in range(ones, len(nums) + ones):
            curr += nums[i % len(nums)]
            curr -= nums[(i - ones) % len(nums)]

            maxi = max(maxi, curr)

        return ones - maxi