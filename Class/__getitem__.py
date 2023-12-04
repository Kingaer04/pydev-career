# class Number:
#     def __init__(self,data):
#         self.data = data
#     def __getitem__(self,index):
#         print('Getitem: ', index)
#         return self.data[index]
    
# x = Number([2,3,4,5,6,0,1])
# print(x[0:4])

class iteration:
    def __getitem__(self,i):
        return self.number[i]
    
    def __repr__(self):
        return str(self.number)
    

x = iteration()
x.number = 'spam'
for i in x:
    print(i, end=' ')

print(x)
