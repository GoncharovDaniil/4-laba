import math
if __name__ == '__main__':
    n = float(input("n="))
k=n/7
r=n-7*k
if n % 2 == 0:
    print("n=7*k")
else:
    print("n=7*k+r")