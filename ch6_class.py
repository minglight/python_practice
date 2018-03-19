class Person():
    obj_prop1 = 1
    obj_prop2 = 2

    def method_1(self, num1, num2):
        print(self.obj_prop1, self.obj_prop2)
        self.obj_prop1 = num1
        self.obj_prop2 = num2
        print(self.obj_prop1, self.obj_prop2)
        print("===========================")

    @classmethod
    def method_2(cls, num1, num2):
        print(cls.obj_prop1, cls.obj_prop2)
        cls.obj_prop1 = num1
        cls.obj_prop2 = num2
        print(cls.obj_prop1, cls.obj_prop2)
        print("===========================")


    def print_prop(self):
        print(self.obj_prop1, self.obj_prop2)
        print("===========================")


person = Person()
person.method_1(3,4)

# using class method will change the objects afterword
Person.method_2(5,6)
# the original 
person.print_prop()
person2 = Person()
person2.print_prop()

#conclusion 
'''
    Person 本來有兩個class屬性 obj_prop1,obj_prop2
    當使用Person()的時候, 他就會把class屬性轉為object屬性, 所以 obj_prop1, obj_prop1會變成 obj的屬性, 這時候cls 跟 obj的兩個屬性已經分開了

    但是當你使用method改到cls的屬性時, 之後再使用Person()的obj屬性初始值會變成改過之後的
'''


