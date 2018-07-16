# https://leetcode.com/problems/add-digits/description/
# This solution is also posted on the Discussions tab - 
# https://leetcode.com/problems/add-digits/discuss/150025/A-solution-involving-no-recursion-no-loops.

import time
import random

class Solution:
    def add_digits_recursive(self, num):
        """
        :type num: int
        :rtype: int
        """
        l = sum(list(map(int, str(num))))
        if l < 10:
            return l
        
        return self.add_digits_recursive(l)
    
    # https://en.wikipedia.org/wiki/Digital_root    
    def add_digits_modulo(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num == 0:
            return 0
        
        n = num%9
        if n == 0:
            return 9
        else:
            return n
        
s = Solution()

# A huge number consisting of 3,15,652 or 3,15,653 digits.
num = random.getrandbits(1024*1024)

t = time.time()
sol1 = s.add_digits_recursive(num)
e = time.time()
print('Method 1 - Recursion\nOutput: {} ({} secs)'.format(sol1, e-t))

t = time.time()
sol2 = s.add_digits_modulo(num)
e = time.time()
print('Method 2 - Modulo_9\nOutput: {} ({} secs)'.format(sol2, e-t))

assert sol1 == sol2

""" 
OUTPUT:

Method 1 - Recursion
Output: 4 (8.737640619277954 secs)
Method 2 - Modulo_9
Output: 4 (0.000997304916381836 secs)
"""
