class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sitdown(self) -> str:
        return '{} sit! '.format(self.name)
    
    def rollover(self) -> str:
        return '{} roll roll roll, roll {}! roll over boy'.format(self.name, self.name)
    
    def  __repr__(self) -> str:
        return 'Name: {}\nAge: {}'.format(self.name, self.age)
    

if __name__ ==  '__main__':
    dog = Dog('Wisky', 2)
    #print('The name of my dog is {}'.format(dog.name))
    #print('{} is {} years old'.format(dog.name, dog.age))
    #print(dog.rollover())
    print(dog)
