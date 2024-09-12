class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        f = [0] * (n+1)
        for first, last, seats in bookings:
            f[first-1] += seats
            f[last] -= seats
        for i in range(1,len(f)):
            f[i] = f[i] + f[i-1]
        return f[:-1]
