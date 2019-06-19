"""PROBLEM:
Given words first and second, consider occurrences in some text of the form "first second third", where second comes
immediately after first, and third comes immediately after second.

For each such occurrence, add "third" to the answer, and return the answer.

Example 1:
Input: text = "alice is a good girl she is a good student", first = "a", second = "good"
Output: ["girl","student"]
"""

class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        words = text.split()
        res = []
        
        for i in range(len(words)-2):
            if words[i] == first and words[i+1] == second:
                res.append(words[i+2])
        
        return res
        
