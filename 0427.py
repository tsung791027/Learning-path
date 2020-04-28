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
