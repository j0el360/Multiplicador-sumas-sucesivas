num1=int(input(""))
num2=int(input(""))

resultado=int(0)

def multiplicar(a,b):
    global suma
    resultado=resultado+b
    
    if(a>1):
        multiplicar(a-1,b)
    return resultado;

print(multiplicar(num1,num2))
