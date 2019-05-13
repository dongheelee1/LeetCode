'''
290. Word Pattern

Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Example 1:

Input: pattern = "abba", str = "dog cat cat dog"
Output: true
Example 2:

Input:pattern = "abba", str = "dog cat cat fish"
Output: false
Example 3:

Input: pattern = "aaaa", str = "dog cat cat dog"
Output: false
Example 4:

Input: pattern = "abba", str = "dog dog dog dog"
Output: false

Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase letters that may be separated by a single space.

bijection:

each element of set A is paired with exactly one element of set B, and each element of the set B is paired with exactly one element of set A. There are no unpaired elements
'''
from collections import Counter


class Solution:

    def wordPattern(self, pattern: str, str: str) -> bool:

        '''
        TIME COMPLEXITY:
        Since there is only one for loop ==> O(n)

        IDEA:
        split the given str on the space and create a words_array of words
        word_freq = frequency of words

        for each character in the pattern:

            populate dictionary with character as key and word in words_array as value:

            if key already exists in dict:

                check that word in words_array == dict[key]

                if above is true:

                    continue

                else if above is not true:

                    return False

            increment counter for words_array

        check to see that word freq actually matches with mapping, if not return False

        return True (able to populate dictionary without problem)
        '''

        words_arr = str.split(" ")

        word_freq = Counter(words_arr)

        if len(words_arr) != len(pattern):
            return False

        mapping = {}

        i = 0

        for char in pattern:

            if char in mapping:

                if mapping[char] != words_arr[i]:
                    return False
            else:

                mapping[char] = words_arr[i]

            i += 1

        if len(mapping) != len(word_freq):
            return False  #ex: word_freq = {'dog': 4}, mapping = {'a': dog, 'b': dog},  str = 'abba', pattern = 'dog dog dog dog'

        return True
