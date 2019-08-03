'''
17. Letter Combinations of a Phone Number

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.



Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:

Although the above answer is in lexicographical order, your answer could be in any order you want.



Complexity Analysis

Time complexity : O(3^N * 4^M) where N is the number of digits in the input that maps to 3 letters (e.g. 2, 3, 4, 5, 6, 8) 
and M is the number of digits in the input that maps to 4 letters (e.g. 7, 9), and N+M is the total number digits in the input.

Space complexity : O(3^N * 4^M) solutions.

'''
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        #here index 2 corresponds to 'abc' which fits the picture description 
        mapping = ['0', '1', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        
        result = self.recursiveLetterCombs([], digits, 0, mapping, "")
        
        return result 
    
    #this method is going to return result 
    #digits = number passed in 
    #mapping = helps us decode a digit to corresponding string 
    #current is what we are forming 
    #index is pointing to current position in current 
    def recursiveLetterCombs(self, result, digits, index, mapping, current):
        
        #if digits is an empty str, return an empty array
        if digits == "":
            return []
        
        #base case: 
        #if length of current string we are forming is equal to len(digits)
            #add current to result array 
            #return result aka backtrack 
        
        if len(current) == len(digits): 
            result.append(current)
            return result
        
        #get str mapped to digit char
        map_string = mapping[int(digits[index])]
        
        #for each character in mapped string, get all combinations 
        for i in range(len(map_string)): 
            result = self.recursiveLetterCombs(result, digits, index+1, mapping, current + map_string[i])
            
        return result
