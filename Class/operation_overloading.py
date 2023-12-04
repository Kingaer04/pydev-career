# class Number:
#     def __init__(self, num) -> None:
#         self.num = num

#     def __add__(self, other) -> int:
#         return Number(self.num - other)
    

# x = Number(5)
# Y = x + 2
# print(Y.num)


class SqureOfANumber:
    def __getitem__(self,list):
        return list ** 2
    
    def __repr__(self) -> str:
        return str(self.list)
    

x = SqureOfANumber()
for i in range(1, 9):
    print(x[i], end=',')
