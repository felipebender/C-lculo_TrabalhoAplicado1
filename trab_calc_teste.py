import math

print ("\nEquação: e^-1 = 2x²-4\n")

def f(x):
    return (math.e)**(-x)
def g(x):
    return 2*x**2-4

def aprox(x1,x2):
    while abs(x1-x2)>=0.1:
        m = (x1+x2)/2
        if (f(x1) <= g(x1) and f(m) >= g(m)) or (f(x1) >= g(x1) and f(m) <= g(m)):
            x2=m
        elif (f(x2) <= g(x2) and f(m) >= g(m)) or (f(x2) >= g(x2) and f(m) <= g(m)):
            x1=m
    print(f"intervalo de comprimento menor que 0.1: {x1} <= x <= {x2}")

t=0
while t==0:
    x1= float(input("Digite o menor valor do intervalo para x: "))
    x2= float(input("Digite o maior valor do intervalo para x: "))

    if (f(x1) <= g(x1) and f(x2) >= g(x2)) or (f(x1) >= g(x1) and f(x2) <= g(x2)):
        t=1
        print('\nA equação tem pelo menos uma solução neste intervalo' )
        aprox(x1,x2)
    else:
        print('\nNão é possível afirmar que existe solução neste intervalo, tente outros dois números\n' )


     

