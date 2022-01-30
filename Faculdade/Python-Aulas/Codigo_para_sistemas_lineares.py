from sympy import *
import  numpy as np

VariavelConhecida = 5
x = symbols('x') 
y = symbols('y') 
eq1 = Eq(5*x +7*y -8,0) 
eq2 = Eq(6*x +10*y -2,0)

sol = solve((eq1,eq2),(x,y))
print(sol)
x =sol[x]
y =sol[y]  
print(x)
print(y)

print(np.sin(np.radians(30)))