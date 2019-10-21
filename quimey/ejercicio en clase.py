import random
def crearlista():
    lista=[]
    i=0
    numero= random.randint(0,100)
    while numero!=0:
        lista.append(numero)
        numero= random.randint(0,100)
        
        
    return lista

def promedio(a):
    acum=0
    mayor=0
    for i in range (len(lista)):
        acum=acum+lista[i]
        prom=acum//len(lista)
       
    return prom
     
def mostrarMayor(lista,prom):
    mayor=0
    for i in range(len(lista)):
        if prom<lista[i]:
            mayor=lista[i]
            print ("el numero es", mayor, "esta en la posicion", i)
     
    
def impares(a):
   cont=0
   i = len(lista)-1
   while i >=0:
       if lista[i]%2!=0:
           lista.pop(i)
           cont +=1
       i-=1
   return cont
     

        
            
        
    
        
        
    

lista= crearlista()
print(lista)
prom= promedio(lista)
print("el promedio es", prom)
valor= mostrarMayor(lista,prom)
impar= impares(lista)
print(lista)
print("Se eliminaron",impar,"elementos")







