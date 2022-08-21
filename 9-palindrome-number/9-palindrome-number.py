class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
    
        'Get left side'
        x = str(x);
        left = []
        
        for element in x:
            'print(element);'
            left.append(element);
            
        'Get right side'
        right = [];
        
        'reverse hash function'
        for elem in x[ : : -1]: 
            'print(elem);'
            right.append(elem);
            
        'Compare arrays left and right'
        if (left == right):
            return True;
        else:
            return False;