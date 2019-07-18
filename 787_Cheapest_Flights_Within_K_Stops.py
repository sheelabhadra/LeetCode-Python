"""PROBLEM:
There are n cities connected by m flights. Each fight starts from city u and arrives at v with a price w.

Now given all the cities and flights, together with starting city src and the destination dst, your task is to find the
cheapest price from src to dst with up to k stops. If there is no such route, output -1.

"""

"""SOLUTION:
We fisrt create the adjacency list. Then using a min heap we keep track of the cost.

"""

import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        # Create the graph
        flight_cost = {}
        for flight in flights:
            start, end, price = flight
            if start in flight_cost:
                flight_cost[start].append((end, price))
            else:
                flight_cost[start] = [(end, price)]
        
        heap = []
        heapq.heappush(heap, (0, -1, src))
        
        while heap:
            curr_price, stops, city = heapq.heappop(heap)
            if stops > K:
                continue
            
            if city == dst:
                return curr_price # since min heap ensures this
            
            if city in flight_cost:
                for end, price in flight_cost[city]:
                    heapq.heappush(heap, (curr_price + price, stops+1, end))
        
        return -1
        
