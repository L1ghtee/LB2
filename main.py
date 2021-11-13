import math

def getX1():
    while type:
        getX = input('Введіть X: ')
        try:
            getX = float(getX)
        except ValueError:
            print('"' + getX + '"' + ' - не  є числом!!! Повторіть спробу!')
        else:
            break
    return getX


def getY1():
    while type:
        getY = input('Введіть Y: ')
        try:
            getY = float(getY)
        except ValueError:
            print('"' + getY + '"' + ' - не  є числом!!! Повторіть спробу!')
        else:
            break
    return getY

def getZ1():
    while type:
        getZ = input('Введіть Z: ')
        try:
            getZ = float(getZ)
        except ValueError:
            print('"' + getZ + '"' + ' - не  є числом!!! Повторіть спробу!')
        else:
            break
    return getZ

x = getX1()
y = getY1()
z = getZ1()
s = math.pow(2, math.pow(y,x) )+ math.pow(math.pow(3 ,x ), y)-(y*(math.atan(z)-(1/3))/(math.fabs(x)+(1/(math.pow(y,2) +1))) )


print("Результат розрахунку:", round(s,3))