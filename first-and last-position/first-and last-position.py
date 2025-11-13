class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def find_left(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return left
        
        def find_right(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1
            return right
        
        left_idx = find_left(nums, target)
        right_idx = find_right(nums, target)
        
        # Check if target was found
        if left_idx <= right_idx and right_idx < len(nums) and nums[left_idx] == target and nums[right_idx] == target:
            return [left_idx, right_idx]
        else:
            return [-1, -1]