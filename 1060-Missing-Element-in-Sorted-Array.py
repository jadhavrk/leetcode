class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        '''
        [2:00] We are given a sorted array of unique numbers and
        we need to find the Kth missing array where
        1 <= K <= 1e7.
        
        We can use binary search but it needs a target.
        In eg 1, 
        We know the left most number = 4
        rightmost number = 10
        so answer should be between 4 and 10
        
        4, five, six, 7, eight, 9, 10
        0   1     2   3    4    5   6
        
        
        [6:00] Side tracking to Naive solution
        - generate missing numbers in new array, G
        - return G[k - 1]
        [8:00] Implementing naive solution
        [11:00] TLE on Naive
        [12:00]: Looked at solution
        - "To find the kth missing element is actually to find the 
        ith element in array that kth is in nums[i, i+1]."
        i < k < i + 1?
        
        - we need to figure out how many elements are missing at any given point
        In eg 1 if the entire array is given,
        missing_count + actual_count = total_count 
        missing_count = total_count - actual count
        total_count = 10 - 4 = 6
        actual_count = 4
        missing_count = 6 - 4 + 1 = 3 (since idx start at 0)
        
        At any ith index missing_count = nums[end] - nums[start] - (end - start) + 1 
        '''
        start, end = nums[0], nums[-1]
        G = []
        for i in range(start, end + k):
            if i not in nums:
                G.append(i)
        return G[k - 1]
