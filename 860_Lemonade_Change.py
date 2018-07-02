# At a lemonade stand, each lemonade costs $5. 

# Customers are standing in a queue to buy from you, and order one at a time (in the order specified by bills).

# Each customer will only buy one lemonade and pay with either a $5, $10, or $20 bill. 
# You must provide the correct change to each customer, so that the net transaction is that the customer pays $5.

# Note that you don't have any change in hand at first.

# Return true if and only if you can provide every customer with correct change.

## SOLUTION: Greedy approach: For every bill (new customer) keep deducting the change starting from the highest
# denomination. If change at the end is 0 then return True else return False.

class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        if bills == []:
            return True
        
        d = [0]*3
        
        for bill in bills:
            if bill == 5:
                d[0] += 1
            elif bill == 10:
                d[1] += 1
            else:
                d[2] += 1
                
            change = bill - 5
            
            while change > 0:
                while change >= 20 and d[2] > 0:
                    change -= 20
                    d[2] -= 1
                    if change == 0:
                        break
                        
                while change >= 10 and d[1] > 0:
                    change -= 10
                    d[1] -= 1
                    if change == 0:
                        break
                        
                while change >= 5 and d[0] > 0:
                    change -= 5
                    d[0] -= 1
                    if change == 0:
                        break
                
                if change != 0:
                    return False
                
            if change != 0:
                return False
        
        return True
                
