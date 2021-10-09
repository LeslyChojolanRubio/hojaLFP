#Hoja de trabajo 2
#en grupos de 3 como máximo programar la gramática recursiva por la derecha y factorizada del 
#siguiente ejemplo en lenguaje python

'''
A -> A,,,C
    |A..D
    |A.C
    |A,D
    |D
    |F

C -> x
D -> b
F -> m

'''
''' Eliminando recursividad por la izquierda
A -> D A'
    |F A'

A' ->, , , C A'            aqui ya no es recursivo por izquierda, sino por derecha :)
    |. . D A'
    |. C A'
    |, D A'
    | Epsilon

C -> x
D -> b
F -> m

Factorizando


A -> D A'
    |F A'

A' ->, FACTORIZADA1         Con esto se le quita la ambiguedad para que no vaya a varios estados con el mismo símbolo.
    |. FACTORIZADA2
    |Epsilon

FACTORIZADA1 -> , , C A'      
                |D A'

FACTORIZADA2 -> . D A'
                | C A'
    
C -> x
D -> b
F -> m                  cadenas validas: b   b,,,x      b,,,x,,,x..b.x    m    m,,,x    m..b.x   m,b.x,,,x..b
    

'''
#con que una producción sea recursivapor la izquierda, la gramática ya es recursiva por izquierda
