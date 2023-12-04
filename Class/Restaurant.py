class Restaurant:
    def __init__(self, name, cuisine_type) ->None:
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self) -> str:
        return 'Restaurant Name: %s\nCuisine_type: %s'%self.name,self.cuisine_type
    
    def open_restaurant(self) -> str:
        return '{} is opened!'.format(self.name)
    