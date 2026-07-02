class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trustsSomeone = [0] * (n + 1)
        trustedBySomeone = [0] * (n+1)

        for a,b in trust:
            trustsSomeone[a] = 1
            trustedBySomeone[b] += 1

        for person in range(1, n+1):
            if trustsSomeone[person] == 0 and trustedBySomeone[person] == n-1:
                return person

        return -1

            