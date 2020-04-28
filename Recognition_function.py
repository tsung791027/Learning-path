#ch11-6 help()
def greeting(name):
    """Python 函數需傳遞名字name"""
    print("hi", name, "Good Morning!")
#greeting('Nelson')

#help(greeting)
#print(greeting.__doc__)

#ch11-6-2
def upperstr(text):
    print(text.upper())
#upperstr('deep')

#upperLetter = upperstr

#upperLetter('deep')

def total(data):
    return sum(data)

x = (1,5,10)
'''mylist = [min, max, sum, total]'''
'''for f in mylist:
    print(f, f(x))
'''
#ch 11-6-5 *args
def mysum(*args):
    return sum(args)
def run_with_multiple_args(func, *agrs):
    return func(*agrs)

print(run_with_multiple_args(mysum, 1, 2, 3, 4, 5))
print(run_with_multiple_args(mysum, 6, 7, 8, 9))

#ch 11-6 closure
def outer():
    b = 10
    def innter(y):
        return 5 * y + b
    return innter
b = 2
f = outer()
print(f(b))

def dist(x1,y1,x2,y2):
    def mysqrt(z):
        return z** 0.5
    dx = (x1 - x2) ** 2
    dy = (y1 - y2) ** 2
    return mysqrt(dx + dy)

print(dist(0,0,1,1))

#lambda funtion
#ch11_32
square = lambda x: x ** 2
print(square)

#lambda 使用時機
def mycar(cars,func):
    for car in cars:
        print(func(car))
dreamcars = ['porsche', 'rolls royce', 'maserati']
mycar(dreamcars, lambda carbrand:"My dream car is " + carbrand.title())

#filter()
#filter(func, iterable)
#iterable 可以重複執行
def oddfn(x):
    return x if (x % 2 == 1) else None

mylist = [5, 10, 15, 20, 25, 30]
filter_object = filter(oddfn, mylist)

print("奇數串列: ",[item for item in filter_object])

#ch11-36 使用匿名函數簡化程式
oddlist = list(filter(lambda x: (x % 2 == 1), mylist))
print(oddlist)

