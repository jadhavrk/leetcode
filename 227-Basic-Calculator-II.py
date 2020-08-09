class Solution:
    def eval_exp(self, a, b, op):
        if op == '*':
            return a*b
        elif op == '/':
            return a//b
        elif op == '+':
            return a+b
        else:
            return a-b
    def calculate(self, s: str) -> int:
        '''
        [1:00]: We are given a string of expressions. 
        
        The goal would be to extract numbers and operations from the string.
        For each operation, extract two numbers and evaluate them
        
        We also have to do this keeping in mind DMAS priority
        
        Approach 1:
        Use 2 stacks,
        one keeps track of numbers
        second keeps track of operations
        If we encounter a * or /, we take 2 numbers and operate immediately
        else we wait until no operations left.
        
        
        Approach 2:
        Build an expression tree
                      *
                     / \
                    +   2
                   / \
                  3   2
                  
        I'll implement approach 1. O(n) time and O(n) space
        
        
        Edge case:
        Empty string
        [19:00] - Reformatting text
        [33:33] - Wrong logic. Try again
        
        '''

        s = re.split(r'([0-9]+)', s)[1:len(s) + 1]
        for i, ch in enumerate(s):
            if ch.isalnum():
                s[i] = int(ch)
        
        nums, op = [], []
        for i, ch in enumerate(s):
            print(nums, op)
            if type(ch) == int:
                nums.append(ch)
            else:
                if ch == '*' or ch == '/':
                    a = nums.pop()
                    b = nums.pop()
                    nums.append(self.eval_exp(b, a, ch))
                else:
                    op.append(ch)
        while op:
            ch = op.pop()
            a = nums.pop()
            b = nums.pop()
            nums.append(self.eval_exp(b, a, ch))
            
        return nums[0]
            
            
