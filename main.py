from funciones import *

computer = generador()
memoria=[]
game = True
while game:
    usuario = ingresoDeDatos()
    #print ("Numero para adivinar: ",computer)
    vacas=0
    toros=0
    for x in range(len(usuario)):
        for y in range(len(computer)):
            if usuario[x]==computer[y]:
                vacas+=1
                if x==y:
                    toros+=1

    vacas = vacas - toros
    memoria.append("numero: {} => {} TOROS .. {} VACAS".format(usuario,toros,vacas))
    
    for imprimir in memoria:
        print(imprimir)
    
    if toros == 4:
        game = False
    

print("HAZ RAZONADO BIEN")