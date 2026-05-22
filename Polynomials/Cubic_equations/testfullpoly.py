import math, cmath
from testredpoly import calculate_rootsr
# Calculates roots of b3x^3+b2x^2+b1_x+b0 (full poly)
# b0 = complex(input("b0="))
# b1 = complex(input("b1="))
# b2 = complex(input("b2="))
# b3 = complex(input("b3="))
b0=4+2j
b1=3+7j
b2=-4+1j
b3=5+3j
def poly(r):
    return b3*r**3+b2*r**2+b1*r+b0 

p=-b2/(3*b3)
a1=(-b2**2/(3*b3)+b1)/b3
a0=(2*b2**3/(27*b3**2)-b1*b2/(3*b3)+b0)/b3
roots=calculate_rootsr(a1, a0)
xp_comp=[]
test=[]
for r in roots:
    R=r+p
    xp_comp.append(R)
    test.append(poly(R))

print(f"x={xp_comp} (full poly)")
print(f"test={test} (full poly)")

