"""
Given an array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
"""

from collections import Counter

class Solution:
    # 14/15 test cases passed
    def singleNumber_method1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.num = []
        for i in nums:
            if(i not in self.num):
                self.num.append(i)
            else:
                self.num.remove(i);
                
        return self.num.pop()
        
    # 15/15 test cases passed    
    def singleNumber_method2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c = Counter(nums)
        return sorted(c.items(), key=lambda i: i[1])[0][0]
        

input = [2, 1, 2, 3, 3, 4, 5, 4, 6, 5, 1]; 
  
s = Solution();

print(s.singleNumber_method1(input))
print(s.singleNumber_method2(input))
