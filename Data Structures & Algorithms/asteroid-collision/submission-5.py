class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        def will_collide(a, b):
            return a > 0 and b < 0

        n = len(asteroids)
        fin = [asteroids[0]]
        for i in range(1, n):
            v = asteroids[i]

            des = False
            while fin and will_collide(fin[-1], v):
                last = fin[-1]
                if abs(last) <= abs(v):
                    fin.pop()
                if abs(last) >= abs(v):
                    des = True
                    break

            if not des:
                fin.append(v)
        return fin