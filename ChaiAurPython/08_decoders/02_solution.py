# Create a decorator to print the function name and the values of its arguments every time the function is called.



def debug(func):#decorators
    def wrapper(*args,**kwargs):
        args_value=','.join(str(arg) for arg in args)
        kwargs_value=','.join(f"{k}={v}" for k,v in kwargs.items())
        print(f"calling :{func.__name__} with args {args_value} and kwargs {kwargs_value}")

        return func(*args,**kwargs)
    return wrapper

#[i*2 for i in []]

@debug
def hello():
    print("Hello")


@debug
def greet(name,greeting="hello"):
    print(f"{greeting},{name}")


greet("sonu",greeting="Good morning")