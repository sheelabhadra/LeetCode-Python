"""PROBLEM:
You are driving a vehicle that has capacity empty seats initially available for passengers.  The vehicle only drives east
(ie. it cannot turn around and drive west.)

Given a list of trips, trip[i] = [num_passengers, start_location, end_location] contains information about the i-th trip:
the number of passengers that must be picked up, and the locations to pick them up and drop them off.  
The locations are given as the number of kilometers due east from your vehicle's initial location.

Return true if and only if it is possible to pick up and drop off all passengers for all the given trips. 

Input: trips = [[3,2,7],[3,7,9],[8,3,9]], capacity = 11
Output: true

"""

"""SOLUTION:
Similar to minimum number of stations/meeting rooms. Sort all the start and end times together in a single array. Also keep
track of the passengers boarding/departing at each time stamp. Then for each time stamp if it is a start time then increase
the number of passengers or else decrease it. If number of passengers > capacity at any point, return false. Make sure to
remove passengers before adding in case of ties in start and end timestamps (IMPORTANT).

"""

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        if len(trips) == 0:
            return True
        
        time_stamps = []
        for trip in trips:
            time_stamps.append((trip[1], 'start', trip[0]))
            time_stamps.append((trip[2], 'end', trip[0]))
        
        time_stamps = sorted(time_stamps)
        
        num_passengers = 0
        for t in time_stamps:
            if t[1] == "start":
                num_passengers += t[2]
                if num_passengers > capacity:
                    return False
            else:
                num_passengers -= t[2]
        
        return True
        
