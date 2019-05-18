class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('a new pet?')

    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def __str__(self):
        return 'this pet\'s name is '+(self.name)