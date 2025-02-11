
x=int(input())
class MyNumbers:
    def __iter__(self):
        self.a=1
        self.b=1
        return self
    
    def __next__(self):
        if self.a<=x**2:
            y=self.a
            self.b+=1
            self.a=self.b
            self.a*=self.a
            return y
        else:
            raise StopIteration
myclass=MyNumbers()
myiter=iter(myclass)

for y in myiter:
    print(y)