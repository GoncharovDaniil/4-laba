import math
if __name__ == '__main__':
    a = float(input("a="))
    b = float(input("b="))
    c = float(input("c="))
if a>b:
    a, b = b, a
if b>c:
    b, c = c, b
if a>b:
    a, b = b, a
print(a,b,c)
if a<b:
    a, b = b, a
if b<c:
    b, c = c, b
if a<b:
    a, b = b, a
print(a,b,c)

