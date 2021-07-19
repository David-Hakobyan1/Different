def hello():
    print("hello my friend")

def decorator_func(hello):
    def wraper():
        print("barev")
        print("sksum enq {}".format(hello))
        hello()
        print("avart")
    wraper()
#decorator_func(hello)

@decorator_func
def hello_world():
    print("hello world")

