class Solution:
    def longestValidParentheses(self, s: str) -> int:
        '''
        [1:22]: Goal is to find the longest valid paranthesis
        Questions to ask interviewer
        - Should it be continous or a subsequence?
            - I'm assuming it's continous
        - Is empty string considered a valid substring? If so, should I return 0?
            - I'm assuming this is the case
        - Can I assume valid inputs. ie no weird charecters?
        
        [3:00] Possible Solutions
        - From solving similar problems I know that a stack is used 
          to verify if a given sequence of string is valid or not
        - So to count the longest valid sequence we would have to validate every substring
        - However this means there are multiple repeated calls to validate the same substring
        - Therefore, we can use memoization or dp techniques to remember the values of substring.
        
        [6:00] Implementation
        - For each substring check if the substring is isValidParanthesis.
        - Store it's value in the longest contigous substring
        - Use previous value to validate future values
        
        [12:00] Wrote pseudo code
        - not sure how to implement dp
        - Probably need to combine sliding window technique with dp
        
        [16:00] Implemented isValidParanthesis
        - still not sure how to implement dp
        - maybe a 2d matrix?
        - Looking up sliding window
           ( ( )
        (  
        (
        )
        [26]: stuck
        '''
        
        def isValidParentheses(substr):
            tot_sum = 0 # this must sum to zero for string to be valid
            for ch in substr:
                if ch == "(":
                    tot_sum += 1
                else:
                    tot_sum -= 1
            return not tot_sum
        
        dp = [0 for i in range(len(s))]
        dp[0] = 0
        for i in range(1, len(s)):
            substr = s[:i]
            if isValidParentheses(substr):
                dp[i] = dp[i - 1] + 1    
                
        print(dp)
