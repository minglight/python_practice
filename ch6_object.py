## hidden property
## @property & @name.setter
class Person():
    '''
        1. @property & @name.setter
        2. use hidden property "__xxxx" 
    '''
    def __init__(self,default_name):
        self.__name = default_name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, input_name):
        self.__name = input_name


#inherit and super()

class Employee(Person):
    
    def __init__(self, default_name, salary):
        super().__init__(default_name)
        self.__salary = salary

    @property
    def salary(self):
        return self.__salary



   # Using salary.setter , not name.setter
    @salary.setter
    def salary(self, salary):
        self.__salary = salary

    




if __name__ == "__main__":
    
    hank = Person('hank')
    #call getter
    print(hank.name)
    #call setter
    hank.name = 'hank hsieh'
    print(hank.name)


    emp_hank = Employee('hank', 10000)
    print(emp_hank.name)
    print(emp_hank.salary)

    emp_hank.salary += 100
    print(emp_hank.salary)



