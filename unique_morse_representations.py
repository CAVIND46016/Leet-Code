# https://leetcode.com/problems/unique-morse-code-words/description/
class Solution:
    
    def __init__(self):
        self.wd= [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.",\
                  "--.-",".-.","...", "-","..-","...-",".--","-..-","-.--","--.."]
        
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        a = []
        for i in words:
            mrs = ""
            for j in list(i):
                idx = ord(j)-97
                mrs += self.wd[idx]
            a.append(mrs)
        
        return len(list(set(a)))
