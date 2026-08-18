class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        zeros = 0
        max_len = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                zeros += 1
            while zeros > 1:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            max_len = max(max_len,right-left+1)
        return max_len-1




class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        zeros = 0
        max_len = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                zeros += 1
            while zeros > 1:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            max_len = max(max_len,right-left+1)
        return max_len-1





class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def sub_arr(k):
            left = 0
            curr_sum = 0
            count = 0
            for right in range(len(nums)):
                curr_sum += nums[right]
                while curr_sum > k:
                    curr_sum -= nums[left]
                    left += 1
                count += (right-left+1)
            return count
    return

        