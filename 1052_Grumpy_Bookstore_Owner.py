"""PROBLEM:
Today, the bookstore owner has a store open for customers.length minutes.  Every minute, some number of customers 
(customers[i]) enter the store, and all those customers leave after the end of that minute.

On some minutes, the bookstore owner is grumpy.  If the bookstore owner is grumpy on the i-th minute, grumpy[i] = 1, 
otherwise grumpy[i] = 0.  When the bookstore owner is grumpy, the customers of that minute are not satisfied, 
otherwise they are satisfied.

The bookstore owner knows a secret technique to keep themselves not grumpy for X minutes straight, but can only use it once.

Return the maximum number of customers that can be satisfied throughout the day.

Example 1:

Input: customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], X = 3
Output: 16
Explanation: The bookstore owner keeps themselves not grumpy for the last 3 minutes. 
The maximum number of customers that can be satisfied = 1 + 1 + 1 + 1 + 7 + 5 = 16.

"""

"""SOLUTION: Copied
The way I approached this problem was to split it into 2 smaller problems.

The first involves counting how many customers are already satisfied, i.e. those where the shopkeeper is not grumpy. 
I also set any slots with already satisfied customers to 0, so that we will be left with only the currently unsatisfied
customers in the list.

For the second part, the array now only contains customers who will not be satisfied. We are able to make X adjacent times
“happy”, so we want to find the subarray of length X that has the most customers. We can just keep a rolling sum of the 
last X customers in the array, and then the best solution is the max the rolling sum ever was.

Finally we return the sum of the 2 parts: the customers who were already satisfied, and the maximum number who can be 
made satisfied by stopping the shop keeper from being grumpy for X time.

"""

class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        # Part 1 requires counting how many customers
        # are already satisfied, and removing them
        # from the customer list.
        already_satisfied = 0
        for i in range(len(grumpy)):
            if not grumpy[i]:
                already_satisfied += customers[i]
                customers[i] = 0
        
        # Part 2 requires finding the optimal number
        # of unhappy customers we can make happy.
        max_satisified_customers = 0
        current_satisfied = 0
        
        for i, cust in enumerate(customers):
            current_satisfied += cust
            if i >= X:
                current_satisfied -= customers[i-X]
            max_satisified_customers = max(max_satisified_customers, current_satisfied)
        
        return already_satisfied + max_satisified_customers
        
