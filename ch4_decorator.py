#define decorator

def logging_decorator(func):
    def decorator_func(*args, **kargs):
        #custom pre-execute logic
        print("pre handle logic")
        #execute original func logic
        try:
            result = func(*args, **kargs)
            #execute post-executioin logic
            print("post handle logic")
            return result
        except Exception as e:
            print("error logic")
            #execute error logic
            raise e
    return decorator_func

@logging_decorator
def add_int(x, y):
    print("adding", x, y)
    return x + y

print("result = " + str(add_int(1,2)))
print("============Error ?==================")
print("result = " + str(add_int("1",2)))