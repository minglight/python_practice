class Person():
    '''
        1. @property & @name.setter
        2. use hidden property "__xxxx" 
    '''
    def __init__(self,default_name, default_age):
        self.__name = default_name
        self.__age = default_age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, input_name):
        self.__name = input_name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, input_age):
        self.__age = input_age

    def __eq__(self, other_person):
        return self.__age == other_person.age

    def __str__(self):
        return "name : " + self.__name + ", age : " + str(self.__age)

if __name__ == "__main__":
    hank = Person('hank', 20)
    chao = Person('Chao', 20)
    ivan = Person('ivan', 19)

    print(hank == chao)
    print(hank == ivan)

    print(hank)