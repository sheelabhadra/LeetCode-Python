""" In a deck of cards, each card has an integer written on it.

    Return true if and only if you can choose X >= 2 such that it is possible to split the entire deck into 1 or more 
    groups of cards, where:

    Each group has exactly X cards.
    All the cards in each group have the same integer.
"""

""" SOLUTION: Use a dictionary and find GCD.
"""

class Solution(object):
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        def GCD(x, y):
            while(y): 
                x, y = y, x % y 
            return x
        
        d = {}
        for card in deck:
            if card not in d:
                d[card] = 1
            else:
                d[card] += 1
        print d
        count = min(d.values())
        
        for k,v in d.items():
            if v < 2:
                return False
            if GCD(v,count) == 1:
                return False
        return True
        
