import random

def test (cadena):
    print(cadena)

def randomUno():
    return random.randint(1,9)

def randomx():
    return random.randint(0,9)

def sonDistintos (lista,al):
    contador = 0
    for elemento in lista:
        if elemento == al: 
            contador+=1
            
    return contador

def generador():
    contador = 0
    lista = []
    lista.append(randomUno())
    while contador<3:
        al = randomx()
        if sonDistintos(lista,al) == 0:
            lista.append(al)
            contador +=1
    return lista

def ingresoDeDatos():
    ingreso=0
    salir = False
    while not salir:
            try:
                entrada = input ("Ingrese su numero: ")
                x = list(entrada)
                for elemento in range(len(x)):
                    x[elemento]=int(x[elemento])
                if len(x)!=4:
                    print("El dato debe tener 4 dígitos")

                if len(x)==4:
                    if x[0]!=0:
                        a = x.count(x[0])
                        b = x.count(x[1])
                        c = x.count(x[2])
                        if a !=1 or b !=1 or c!=1:
                            print("No se preocupe, sólo tiene que cambiar los números que se repiten")
                            print("para el juego no puede repetir los numeros")
                            
                        else: 
                            salir = True
                    else:
                        print("No puede tener CERO el primer digito")
                
            except:  
                print("¡Lo sentimos!")
                print("Posiblemente se ha ingresado un caracter que no es número")
                print("intentelo de nuevo por favor!")
            
            
    return x


