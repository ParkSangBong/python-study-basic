# Section08
# 파이썬 모듈과 패키지

# 패키지 예제
# 상대 경로
# .. : 부모 디렉토리
# .  : 현재 디렉토리

# 사용1(클래스)

from pkg.fibonacci import Fibonacci

Fibonacci.fibo(300)

print("ex1 : ", Fibonacci.fibo2(400))
print("ex1 : ", Fibonacci().title)

# 사용2(클래스)
from pkg.fibonacci import *

Fibonacci.fibo(300)

print("ex2 : ", Fibonacci.fibo2(700))
print("ex2 : ", Fibonacci().title)

# 사용3(클래스)
from pkg.fibonacci import Fibonacci as fib

fib.fibo(300)

print("ex3 : ", fib.fibo2(1600))
print("ex3 : ", fib().title)

# 사용4(함수)
import pkg.calculations as c

print("ex4 : ", c.add(10, 100))
print("ex4 : ", c.mul(10, 100))

# 사용5(함수)
from pkg.calculations import div as d

print("ex5 : ", int(d(100,10)))

# 사용6
import pkg.prints as p
import builtins

p.prt1()
p.prt2()
print(dir(builtins))