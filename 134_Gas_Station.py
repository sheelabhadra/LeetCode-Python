#There are N gas stations along a circular route, where the amount of gas at station i is gas[i].

#You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1).
#You begin the journey with an empty tank at one of the gas stations.

#Return the starting gas station's index if you can travel around the circuit once, otherwise return -1.

#### SOLUTION ####

class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        sumGas, sumCost, start, tank = 0, 0, 0, 0
        for i in range(len(gas)):
            sumGas += gas[i]
            sumCost += cost[i]
            tank += gas[i] - cost[i]
            if tank < 0:
                tank = 0
                start = i+1
        
        if sumGas < sumCost:
            return -1
        else:
            return start
            
