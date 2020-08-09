class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        '''
        Given a list of names where the first element is the name
        and the following elements are email id's we are 
        supposed to merge them.
        
        I think a hashmap where the key is a string and value is an array
        would be a useful datastructure to use in this problem.
        
        Since a hashmap provides quick lookup the appropriate bucket and place
        elements in it.
        Runtime would be O(N) and space would be O(N)
        
        Alternatively, we know that the length of accounts will be in 
        range 1 - 10, so we can use bucket sort.
        
        [10:00]Misunderstood question
        
        Naive approach
        Go through list,
        if same name and intersection in email -> merge
        
        
        [
            ["John", "johnsmith@mail.com", "john00@mail.com"], 
            ["John", "johnnybravo@mail.com"], 
            ["John", "johnsmith@mail.com", "john_newyork@mail.com"], 
            ["Mary", "mary@mail.com"]]
            
        [22:00]: Stuck. Saw solution
        Graph or Union Find
        '''
        # get unique names
        names = set()
        for acc in accounts:
            names.add(acc[0])
        print(names)
        
        def get_lists_with_name(name):
            res = []
            for acc in accounts:
                if acc[0] == name:
                    res.append(acc[1:])
                    
            return res
        
        #get filtered list by names
        # if intersection between list1 and list2
        # merge
        for name in names:
            emails_filtered_by_name = get_lists_with_name(name)
            
            for i in range(len(emails_filtered_by_name)):
                for j in range(1, len(emails_filtered_by_name)):
                    if 0 <= j <= len(emails_filtered_by_name):
                        s1 = emails_filtered_by_name[i]
                        s2 = emails_filtered_by_name[j]
                        if s1.intersection(s2):
                            merge(s1, s2)

                        
        
