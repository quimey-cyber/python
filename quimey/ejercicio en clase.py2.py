def socio():
    listaUrgencia=[]
    listaTurnos=[]
    num=int(input("ingrese numero de socio:"))
    while num!=-1:
        while num<1000 or num>9999:
            num=int(input("ingrese numero de socio:"))
        casos=int(input("urgencia = 1, turno = 2:"))
        if casos==1:
            listaUrgencia.append(num)
        if casos==2:
            listaTurnos.append(num)
        num=int(input("ingrese numero de socio:"))
    return listaUrgencia, listaTurnos

def busquedanumero(a,b,c):
    cont=0
    cont1=0
    for i in range(0,len(a)):
        if a[i]==c:
            cont+=1
    for i in range(0,len(b)):
        if b[i]==c:
            cont1+=1
    return cont, cont1
    
paciente1, paciente2 = socio()
print(paciente1)
print(paciente2)
numeropedido=int(input("ingrese numero de socio que desea buscar:"))
busqueda1,busqueda2= busquedanumero(paciente1,paciente2,numeropedido)
print(busqueda1)
print(busqueda2)
        
        
        
        
        
    

