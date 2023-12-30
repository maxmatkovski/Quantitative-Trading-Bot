class MyClass:
    def outer_method(self):
        x = "hello"

        def inner_method():
            print("x " , x)
            print(self)


obj = MyClass()
obj.outer_method()
