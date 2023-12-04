'''
Learning how to implement classs and object
by creating an incrementing app
'''

class CountBy:
    '''Will increment the value'''
    def __init__(self,v:int=0,i:int=1) -> None:
        self.value = v
        self.increment = i

    def increase(self) -> None:
        self.value += self.increment

    def __repr__(self) -> str:
        return str(self.value)
    

if __name__ == "__main__":
    a = CountBy(10)
    a.increase()
    a.increase()
    print(a)
