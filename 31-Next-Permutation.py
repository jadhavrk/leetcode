class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        '''
        Understanding: The next number that is generated in the permutation if
        it was generated using backtracking or recursion.
        
        If it's the greatest, then return the lowest possible order
        Eg. 3, 2, 1 -> 1, 2, 3
        
        Possible solution:
        - Use backtracking like approach where 
        we first search for the first "dip"/smallest number from the end
        say i
        swap(nums[i], nums[i + 1])
        Eg 1, 2, 3 -> 1 is the first smallest num since nums[2] > nums[3]. So swap(nums[2], nums[3])
        1, 2, 3, 4 -> 1, 2, 4, 3
        
        If i == 0, then return sorted array in ascending order
        
        Only works if edge there are atleast 2 numbers. Account for edge case. Ask interviewer for input len?
        [12:00]
        
        Coded solution at 16:00
        
        Test cases:
        [] -> []
        [1] -> [1]
        [1, 2]
        i = 1, nums[1] > nums[0]: True -> nums = [2, 1]
        [1, 1, 5]
        i = 2, nums[2] > nums[1]: True -> nums[1, 5, 1]
        
        Ran code at 18:00
        Failed at [1, 3, 2] -> [2, 1, 3]
        Wrong algo, need to come up with better strategy
        Find the next biggest digit and swap with i - 1 ? Not sure.
        
        
        '''
        #Edge case
        if not nums:
            return []
        if len(nums) == 1:
            return nums
        
        i = len(nums) - 1
        
        #check from back for dip
        while i > 0:
            if nums[i] > nums[i - 1]:
                nums[i], nums[i-1] = nums[i - 1], nums[i]
                return nums
            i -= 1
        
        # largest possible element
        nums.sort()
        
        return nums
            
