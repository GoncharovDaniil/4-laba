import math
if __name__ == '__main__':
    x = float(input("x="))
if x <= 0:
    y = 2*x*x+math.cos(x)
elif x < 5:
    y=x+1
else:
    y=math.sin(x)-x*x
print("y= {0}".format(y))