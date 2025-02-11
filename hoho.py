
x=int(input())
class MyNumbers:
    def __iter__(self):
        self.a=1
        self.b=1
        return self
    
    def __next__(self):
        if self.a<=x:
            y=self.a
            self.a+=1
            return y
        else:
            raise StopIteration
myclass=MyNumbers()
myiter=iter(myclass)
b=list
for y in myiter:
    if y%2==0:
        print(y,end=",")
         