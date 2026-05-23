class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l = 0
        r = len(people) - 1
        numOfBoat = 0
        while(l < r):
            weight = people[l] + people[r]
            if weight <= limit:
                l += 1
                r -= 1
            else:
                r -= 1
            numOfBoat += 1
        if l == r:
            numOfBoat += 1
        return numOfBoat