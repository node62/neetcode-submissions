class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        def will_collide(a, b):
            return a > 0 and b < 0
        fin = []
        for v in asteroids:
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