import numpy as np

#Creacion de personaje con Stacks Aleatorios 
#Planteamento General

n=int(input("""Bienvenido a Dungeons And Dragons , para poder escoger su personaje será de la siguiente manera:
1= Barbaro 
2= Bardo
3= Clérigo
4= Druida
5= Guerrero
6= Mago
7= Paladín 
8= Pícaro
"""))

atributos= np.random.randint(10,19, size=144).reshape(8,3,6)

if n>=1 and n<=8:

    if n==1:
        x=int(input("""Su personaje es un Barbaro, Digite un numero del 1 al 3 para la eleccion automatica de Stacks
        """))
        if x>=1 and x<=3:
            Barbaro= atributos[n-1][x-1]
            print("Sus atributos son", Barbaro ,",Estos atributos representan Fuerza, Destreza, Constitución, Inteligencia, Sabiduría y Carisma , respectivamente")
        else:
            print("Por favor haga bien el procedimiento")

    elif n==2:
        x=int(input("Su personaje es un Bardo, Digite un numero del 1 al 3 para la eleccion automatica de Stacks"))
        if x>=1 and x<=3:
            Bardo= atributos[n-1][x-1]
            print("Sus atributos son",Bardo , ",Estos atributos representan Fuerza, Destreza, Constitución, Inteligencia, Sabiduría y Carisma , respectivamente")
        else:
            print("Por favor haga bien el procedimiento")

    elif n==3:
        x=int(input("Su personaje es un clerigo, Digite un numero del 1 al 3 para la eleccion automatica de Stacks"))
        if x>=1 and x<=3:
            clerigo= atributos[n-1][x-1]
            print("Sus atributos son",clerigo,",Estos atributos representan Fuerza, Destreza, Constitución, Inteligencia, Sabiduría y Carisma , respectivamente")
        else:
            print("Por favor haga bien el procedimiento")

    elif n==4:
        x=int(input("Su personaje es un Druida, Digite un numero del 1 al 3 para la eleccion automatica de Stacks"))
        if x>=1 and x<=3:
            Druida= atributos[n-1][x-1]
            print("Sus atributos son",Druida,",Estos atributos representan Fuerza, Destreza, Constitución, Inteligencia, Sabiduría y Carisma , respectivamente")
        else:
            print("Por favor haga bien el procedimiento")

    elif n==5:
        x=int(input("Su personaje es un Guerrero, Digite un numero del 1 al 3 para la eleccion automatica de Stacks"))
        if x>=1 and x<=3:
            Guerrero= atributos[n-1][x-1]
            print("Sus atributos son",Guerrero,",Estos atributos representan Fuerza, Destreza, Constitución, Inteligencia, Sabiduría y Carisma , respectivamente")
        else:
            print("Por favor haga bien el procedimiento")            

    elif n==6:
        x=int(input("Su personaje es un Mago, Digite un numero del 1 al 3 para la eleccion automatica de Stacks"))
        if x>=1 and x<=3:
            Mago= atributos[n-1][x-1]
            print("Sus atributos son",Mago,",Estos atributos representan Fuerza, Destreza, Constitución, Inteligencia, Sabiduría y Carisma , respectivamente")
        else:
            print("Por favor haga bien el procedimiento")

    elif n==7:
        x=int(input("Su personaje es un Paladin, Digite un numero del 1 al 3 para la eleccion automatica de Stacks"))
        if x>=1 and x<=3:
            Paladin= atributos[n-1][x-1]
            print("Sus atributos son",Paladin,",Estos atributos representan Fuerza, Destreza, Constitución, Inteligencia, Sabiduría y Carisma , respectivamente")
        else:
            print("Por favor haga bien el procedimiento")

    else:
        x=int(input("Su personaje es un Picaro, Digite un numero del 1 al 3 para la eleccion automatica de Stacks"))
        if x>=1 and x<=3:
            Picaro= atributos[n-1][x-1]
            print("Sus atributos son",Picaro,",Estos atributos representan Fuerza, Destreza, Constitución, Inteligencia, Sabiduría y Carisma , respectivamente")
        else:
            print("Por favor haga bien el procedimiento")

else:
    print("Por el momento solo tenemos 8 clases , por favor digite una de las anteriores")
