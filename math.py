from sympy import*
x = Symbol('x')
a = Symbol('a')
print('1.'+repr(diff(exp(a*x**2), x)))
print('2.'+repr(diff(tan(x))))
print('3.'+repr(diff(cot(x))))
print('4.'+repr(diff(log(x))))
print('5.'+repr(diff(x**x)))
# Note that ** means ^
