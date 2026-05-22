import math, cmath
#calculates roots of a3x^3+a1x+a0 (reduced poly)
def calculate_rootsr(a1, a0):
    D=(a0**2+4*a1**3/27)
    x1_comp=100000
    x2_comp=200000
    x3_comp=300000
    if a0.imag == 0 and D.imag == 0:
        if D.real >= 0.0:
            #test set:
            #x1=1+2j
            #x2=1-2j
            h = (-a0+D**(1/2))/2
            g = (-a0-D**(1/2))/2
            G=cuberoot(abs(g), 3*phase(g))
            H=cuberoot(abs(h), 3*phase(h))
            x1_comp=G+H
            x2_comp=G*cmath.exp(-1j*2*math.pi/3)+H*cmath.exp(1j*2*math.pi/3)
            x3_comp=G*cmath.exp(1j*2*math.pi/3)+H*cmath.exp(-1j*2*math.pi/3)
        if D.real < 0.0:
            #test set
            #x1=2
            #x2=1
            h = (-a0+abs(D)**(1/2)*cmath.exp(1j*(math.pi+0*2*math.pi)/2))/2
            g = (-a0+abs(D)**(1/2)*cmath.exp(1j*(math.pi+1*2*math.pi)/2))/2
            mod=(-a1/3)**(1/2)
            phi=(phase(h))
            x1_comp = 2*mod*math.cos(phi/3)
            x2_comp = 2*mod*math.cos(phi/3-2*math.pi/3)
            x3_comp = 2*mod*math.cos(phi/3-4*math.pi/3)
    else:
        h = ( -a0+ abs(D)**(1/2)*cmath.exp(1j*(math.atan2(D.imag, D.real)+0*2*math.pi)/2)   )/2
        g = ( -a0+ abs(D)**(1/2)*cmath.exp(1j*(math.atan2(D.imag, D.real)+1*2*math.pi)/2)   )/2
        ng=0
        nh=(3*(phase(a1)+math.pi)-phase(h)-phase(g))/(2*math.pi)-ng
        H=cuberoot(abs(h), phase(h)+nh*2*math.pi) 
        G=cuberoot(abs(g), phase(g)+ng*2*math.pi)
        x1_comp=G+H
        x2_comp=G*cmath.exp(-1j*2*math.pi/3)+H*cmath.exp(1j*2*math.pi/3)
        x3_comp=G*cmath.exp(1j*2*math.pi/3)+H*cmath.exp(-1j*2*math.pi/3)
    return x1_comp, x2_comp, x3_comp

def phase(c):
    if c.real == 0:
        if c.imag == 0:
            raise ValueError("Phase is not defined for a zero")
        else:
            if c.imag>0:
                return math.pi/2
            if c.imag<0:
                return 3*math.pi/2
    else:
        if c.real>0:
            return math.atan(c.imag/c.real)
        if c.real<0:
            return math.atan(c.imag/c.real)+math.pi

def cuberoot(module, phase):
    if module.imag>0:
        raise ValueError("module must be a real number")
    if module.real < 0:
        raise ValueError("module must be greater or equal than zero")
    return module**(1/3)*cmath.exp(1j*phase/3)
    
def polyr(r):
    return r**3+a1*r+a0

if __name__ == "__main__":
    # x1=1+1j
    # x2=1-1j
    x1=3
    x2=2
    # x1=4+2j
    # x2=-1+3j
    x3=-(x1+x2)
    a1=x1*x2+x2*x3+x3*x1
    a0=-x1*x2*x3
    roots=calculate_rootsr(a1, a0)
    testxr1=polyr(roots[0])
    testxr2=polyr(roots[1])
    testxr3=polyr(roots[2])
    print(f"tests={testxr1, testxr2, testxr3} (reduced poly)")
    print(f"x={roots} (reduced poly)")
