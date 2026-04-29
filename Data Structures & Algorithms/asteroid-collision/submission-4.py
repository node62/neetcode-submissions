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
                if abs(fin[-1])==abs(v):
                    fin.pop()
                    des = True
                    break
                elif abs(fin[-1])>=abs(v):
                    des = True
                    break
                fin.pop()

            if not des:
                fin.append(v)
        return fin


        