class number:
    def _init_(self,n):
        self.n = n
    
    def _add_(self, num):
        return self.n + num.n

n = number(1)
m = number(2)

print(n + m)