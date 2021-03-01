import math
a= float(input())
operacion =str(input())
def solo (u):
    if operacion== "sqrt":
        try:    
            resultado= math.sqrt(a)
            print(resultado)
            b = 0
        except "ValueError":
            print("es un numero negativo")
    elif operacion == "!":
        resultado = math.factorial(a)
        print(resultado)
        b = 0
    elif operacion=="ln":
        resultado = math.log1p(a)
        print (resultado)
        b=0
    elif operacion== "sen" or operacion=="sin":
        resultado = math.sin(a)
        print (resultado)
        b=0
    elif operacion== "cos":
        resultado = math.cos(a)
        print (resultado)
        b=0
    elif operacion== "tan":
        resultado= math.tan(a)
        print (resultado)
        b=0
    elif operacion== "arcos":
        resultado= math.acos(a)
        print (resultado)
        b=0
    elif operacion=="arcsen" or operacion=="arcsin":
        resultado = math.asin(a)
        print (resultado)
        b=0
    elif operacion=="arctan":
        resultado= math.atan(a)
        print (resultado)
        b=0

def op(x,y):
    if operacion== "+":
        resultado = a + b
        print (resultado)
    elif operacion== "-":
        resultado= a-b
        print (resultado)
    elif operacion =="*":
        resultado = a*b
        print (resultado)
    elif operacion=="/":
        resultado= a/b
        print(resultado)
    elif operacion =="**":
        resultado = a**b
        print(resultado)

if operacion== "sqrt" or operacion=="!" or operacion=="ln" or operacion== "sen" or operacion=="sin" or operacion== "cos" or operacion== "tan" or operacion== "arcos" or operacion=="arcsen" or operacion=="arcsin" or  operacion=="arctan":
    solo(a)
else:
    b = float(input())   
    op(a,b)
print ("Desea realizar otra operacion?")
cont = input()
if cont== "si":
    sigue= True
    while sigue == True:
        a= float(input())
        operacion =str(input())
        if operacion == "!":
            resultado= math.factorial(a)
            print (resultado)
            b= 0
        elif operacion== "sqrt":
            try:
                resultado= math.sqrt(a)
                print(resultado)
                b= 0
            except "ValueError":
                print("Es un valor negativo")
        elif operacion=="ln":
            resultado = math.log1p(a)
            print (resultado)
            b=0
        elif operacion== "sen" or operacion=="sin":
            resultado = math.sin(a)
            print (resultado)
            b=0
        elif operacion== "cos":
            resultado = math.cos(a)
            print (resultado)
            b=0
        elif operacion== "tan":
            resultado= math.tan(a)
            print (resultado)
            b=0
        elif operacion== "arcos":
            resultado= math.acos(a)
            print (resultado)
            b=0
        elif operacion=="arcsen" or operacion=="arcsin":
            resultado = math.asin(a)
            print (resultado)
            b=0
        elif operacion=="arctan":
            resultado= math.atan(a)
            print (resultado)
            b=0
        else:
            b=float(input())
            op(a,b)
        print ("Desea realizar otra operacion?")
        cont = input()
        if cont != "si":
            print ("fin del programa")
else:
    sigue = False
    print ("fin del programa")



