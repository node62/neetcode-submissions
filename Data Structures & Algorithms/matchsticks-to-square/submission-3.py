class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        matchsticks.sort(reverse = True)
        n = len(matchsticks)
        sides = [0] * 4
        if sum(matchsticks) % 4:
            return False
        check = sum(matchsticks) // 4
        def bt(i):
            if i == n:
                if sides[0] == sides[1] == sides[2] == sides[3] == check:
                    return True
                return False
            for j in range(4):
                if sides[j] + matchsticks[i] > check:
                    continue
                sides[j]+=matchsticks[i]
                if bt(i+1):
                    return True
                sides[j]-=matchsticks[i]
            return False
        return bt(0)

