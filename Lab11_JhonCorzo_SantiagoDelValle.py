import numpy as np

#Creacion de personaje con Stacks Aleatorios 
#Planteamento General
#Balanceo de estadisticas según el personaje

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

Fisicos_Fisicos= np.random.randint(10,19, size=36).reshape(4,3,3)
Fisicos_Mentales= np.random.randint(1,6, size=36).reshape(4,3,3)
Mentales_Fisicos= np.random.randint(1,6, size=36).reshape(4,3,3)
Mentales_Mentales= np.random.randint(10,19, size=36).reshape(4,3,3)

print(Fisicos_Fisicos)


if n>=1 and n<=8:

    if n==1:
        x=int(input("""Su personaje es un Barbaro, Digite un numero del 1 al 3 para la eleccion automatica de Stacks
        """))
        z=int(input("""Digite un numero dentro del 1 al 3 para un mejor balanceo
        """))
        if x>=1 and x<=3 and z>=1 and z<=3:
            Barbaro_fisico= Fisicos_Fisicos[z-1][x-1]
            Barabaro_Mentales= Fisicos_Mentales[z-1][x-1]
            print("Sus atributos son", Barbaro_fisico,Barabaro_Mentales ,",Estos atributos representan Fuerza, Destreza, Constitución, Inteligencia, Sabiduría y Carisma , respectivamente")
        else:
            print("Por favor haga bien el procedimiento")

    elif n==2:
        x=int(input("""Su personaje es un Bardo, Digite un numero del 1 al 3 para la eleccion automatica de Stacks
        """))
        z=int(input("""Digite un numero dentro del 1 al 3 para un mejor balanceo
        """))
        if x>=1 and x<=3 and z>=1 and z<=3:
            Bardo_fisico= Mentales_Fisicos [z-1][x-1]
            Bardo_Mental= Mentales_Mentales [z-1][x-1]
            print("Sus atributos son",Bardo_fisico,Bardo_Mental , ",Estos atributos representan Fuerza, Destreza, Constitución, Inteligencia, Sabiduría y Carisma , respectivamente")
        else:
            print("Por favor haga bien el procedimiento")

    elif n==3:
        x=int(input("""Su personaje es un clerigo, Digite un numero del 1 al 3 para la eleccion automatica de Stacks
        """))
        z=int(input("""Digite un numero dentro del 1 al 3 para un mejor balanceo
        """))
        if x>=1 and x<=3 and z>=1 and z<=3:
            clerigo_fisico= Mentales_Fisicos [z-1][x-1]
            clerigo_Mental= Mentales_Mentales [z-1][x-1]
            print("Sus atributos son",clerigo_fisico,clerigo_Mental,",Estos atributos representan Fuerza, Destreza, Constitución, Inteligencia, Sabiduría y Carisma , respectivamente")
        else:
            print("Por favor haga bien el procedimiento")

    elif n==4:
        x=int(input("""Su personaje es un Druida, Digite un numero del 1 al 3 para la eleccion automatica de Stacks
        """))
        z=int(input("""Digite un numero dentro del 1 al 3 para un mejor balanceo
        """))
        if x>=1 and x<=3 and z>=1 and z<=3:
            Druida_fisico= Mentales_Fisicos [z-1][x-1]
            Druida_Mental= Mentales_Mentales [z-1][x-1]
            print("Sus atributos son",Druida_fisico,Druida_Mental,",Estos atributos representan Fuerza, Destreza, Constitución, Inteligencia, Sabiduría y Carisma , respectivamente")
        else:
            print("Por favor haga bien el procedimiento")

    elif n==5:
        x=int(input("""Su personaje es un Guerrero, Digite un numero del 1 al 3 para la eleccion automatica de Stacks
        """))
        z=int(input("""Digite un numero dentro del 1 al 3 para un mejor balanceo
        """))
        if x>=1 and x<=3 and z>=1 and z<=3:
            Guerrero_fisico= Fisicos_Fisicos[z-1][x-1]
            Guerrero_mental= Fisicos_Mentales[z-1][x-1]
            print("Sus atributos son",Guerrero_fisico,Guerrero_mental,",Estos atributos representan Fuerza, Destreza, Constitución, Inteligencia, Sabiduría y Carisma , respectivamente")
        else:
            print("Por favor haga bien el procedimiento")            

    elif n==6:
        x=int(input("""Su personaje es un Mago, Digite un numero del 1 al 3 para la eleccion automatica de Stacks
        """))
        z=int(input("""Digite un numero dentro del 1 al 3 para un mejor balanceo
        """))
        if x>=1 and x<=3 and z>=1 and z<=3:
            Mago_fisico= Mentales_Fisicos [z-1][x-1]
            Mago_Mental= Mentales_Mentales [z-1][x-1]
            print("Sus atributos son",Mago_fisico,Mago_Mental,",Estos atributos representan Fuerza, Destreza, Constitución, Inteligencia, Sabiduría y Carisma , respectivamente")
        else:
            print("Por favor haga bien el procedimiento")

    elif n==7:
        x=int(input("""Su personaje es un Paladin, Digite un numero del 1 al 3 para la eleccion automatica de Stacks
        """))
        z=int(input("""Digite un numero dentro del 1 al 3 para un mejor balanceo
        """))
        if x>=1 and x<=3 and z>=1 and z<=3:
            Paladin_fisico= Fisicos_Fisicos[z-1][x-1]
            paladin_mental= Fisicos_Mentales[z-1][x-1]
            print("Sus atributos son",Paladin_fisico,paladin_mental,",Estos atributos representan Fuerza, Destreza, Constitución, Inteligencia, Sabiduría y Carisma , respectivamente")
        else:
            print("Por favor haga bien el procedimiento")

    else:
        x=int(input("""Su personaje es un Picaro, Digite un numero del 1 al 3 para la eleccion automatica de Stacks
        """))
        z=int(input("""Digite un numero dentro del 1 al 3 para un mejor balanceo
        """))
        if x>=1 and x<=3 and z>=1 and z<=3:
            Picaro_fisico= Fisicos_Fisicos[z-1][x-1]
            Picaro_mental= Fisicos_Mentales[z-1][x-1]
            print("Sus atributos son",Picaro_fisico,Picaro_mental,",Estos atributos representan Fuerza, Destreza, Constitución, Inteligencia, Sabiduría y Carisma , respectivamente")
        else:
            print("Por favor haga bien el procedimiento")

else:
    print("Por el momento solo tenemos 8 clases , por favor digite una de las anteriores")