def decor(func):
    def hi():
        print('Hello', end=", ")
        func()
    return hi

@decor
def hello():
    print('Dima')

hello()

