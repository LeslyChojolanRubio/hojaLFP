# INICIO = A
#  A = D A'
#     |F A'

# A' = , FACTORIZADA1         Con esto se le quita la ambiguedad para que no vaya a varios estados con el mismo símbolo.
#     |. FACTORIZADA2
#     |Epsilon

# FACTORIZADA1 = , , C A'      
#                 |D A'         al parecer si hay recursividad con A' pero está implicita, no se ve a simple vista.

# FACTORIZADA2 = . D A'
#                 | C A'
    
# C = x
# D = b
# F = m                  cadenas validas: b   b,,,x      b,,,x,,,x..b.x    m    m,,,x    m..b.x   m,b.x,,,x..b
    



#con que una producción sea recursivapor la izquierda, la gramática ya es recursiva por izquierda
#analizador lexico simulado    imagina que cada letra es una palabra. Como lo de ordenar sintacticamente un if.
listaTokens = []   # m,,,x
listaTokens.append({'lexema': 'm', 'tipo': 'tk_m', 'linea': 1, 'columna': 1})
listaTokens.append({'lexema': ',', 'tipo': 'tk_coma', 'linea': 1, 'columna': 2})
listaTokens.append({'lexema': ',', 'tipo': 'tk_coma', 'linea': 1, 'columna': 22})
listaTokens.append({'lexema': ',', 'tipo': 'tk_coma', 'linea': 1, 'columna': 3})
listaTokens.append({'lexema': ',', 'tipo': 'tk_coma', 'linea': 1, 'columna': 4})
listaTokens.append({'lexema': 'x', 'tipo': 'tk_x', 'linea': 1, 'columna': 5})

#no estoy viendo si una cadena es valida o no eso es un hecho estoy viendo si la lista de tokens está en el orden correcto sintacticamente
#m,b.x,,,x..b
# tk_m    tk_b   tk_x  tk_coma  tk_punto
# F         D     C      ,       .

for t in listaTokens:
    print(t['lexema'])

#cada no terminal es un estado o una funcion del analizador sintáctico. Algunas funciones son recursivas. Cada vez que necesite reconocer un token coloco un if.

# analizador sintactico /parser   cada función reconoce tokens
tokenActual = 0    #variable global

def FACTORIZADA1(indiceToken):         #a cada no terminal le corresponde una funcion
    if listaTokens[indiceToken]['tipo'] == 'tk_coma':
        #print('va bien')
        indiceToken += 1
        if listaTokens[indiceToken]['tipo'] == 'tk_coma':
            indiceToken += 1
            if listaTokens[indiceToken]['tipo'] == 'tk_x':
                A_prima(indiceToken+1)
                #return True
            #print('ya lee el segundo id ' + listaTokens[indiceToken]['lexema'] )
            else:
                print('Error sintáctico: Se esperaba un token x y se recibió ' + listaTokens[indiceToken]['tipo'] , listaTokens[indiceToken]['linea'], listaTokens[indiceToken]['columna'] )
                #return False
        else:
            print('Error sintáctico: Se esperaba un token coma y se recibió ' + listaTokens[indiceToken]['tipo'] , listaTokens[indiceToken]['linea'], listaTokens[indiceToken]['columna'] )
    
    elif listaTokens[indiceToken]['tipo'] == 'tk_b':
        A_prima(indiceToken+1)
                #return True
    else:
        print('Error sintáctico: Se esperaba un token coma o token b pero se recibió ' + listaTokens[indiceToken]['tipo'] , listaTokens[indiceToken]['linea'], listaTokens[indiceToken]['columna'] )
        #return False



def FACTORIZADA2(indiceToken):         #a cada no terminal le corresponde una funcion
    if listaTokens[indiceToken]['tipo'] == 'tk_punto':
        #print('va bien')
        indiceToken += 1    
        if listaTokens[indiceToken]['tipo'] == 'tk_b':
            A_prima(indiceToken+1)
            #return True
        #print('ya lee el segundo id ' + listaTokens[indiceToken]['lexema'] )
        else:
            print('Error sintáctico: Se esperaba un token b y se recibió ' + listaTokens[indiceToken]['tipo'] , listaTokens[indiceToken]['linea'], listaTokens[indiceToken]['columna'] )
            #return False
    elif listaTokens[indiceToken]['tipo'] == 'tk_x':
        A_prima(indiceToken+1)
                #return True
    else:
        print('Error sintáctico: Se esperaba un token punto o token x pero se recibió ' + listaTokens[indiceToken]['tipo'] , listaTokens[indiceToken]['linea'], listaTokens[indiceToken]['columna'] )
        #return False



def A_prima(indiceToken):
    if indiceToken < len(listaTokens):
        if listaTokens[indiceToken]['tipo'] == 'tk_coma':
            #print('va bien')
            #indiceToken += 1
            FACTORIZADA1(indiceToken+1)
            return True
            
            #print('ya lee el segundo id ' + listaTokens[indiceToken]['lexema'] )
        elif listaTokens[indiceToken]['tipo'] == 'tk_punto':
                #indiceToken += 1
                FACTORIZADA2(indiceToken+1)
                return True
                
        else:
            print('Error sintáctico: Se esperaba un token coma o punto y se recibió ' + listaTokens[indiceToken]['tipo'] , listaTokens[indiceToken]['linea'], listaTokens[indiceToken]['columna'] )
            return False

    else:
        return True #se recibió epsilon

def A(indiceToken):         #a cada no terminal le corresponde una funcion
    if listaTokens[indiceToken]['tipo'] == 'tk_b':
        return A_prima(indiceToken+1)
        #print('El token reconocido es: ',listaTokens[indiceToken]['lexema'])
    elif listaTokens[indiceToken]['tipo'] == 'tk_m':
        return A_prima(indiceToken+1)
        #print('El token reconocido es: ',listaTokens[indiceToken]['lexema'])
    else:
        print('Error sintáctico: Se esperaba un token b o m y se recibió ' + listaTokens[indiceToken]['tipo'] , listaTokens[indiceToken]['linea'], listaTokens[indiceToken]['columna'] )
        return False

def inicio(indiceToken):
    analisis = A(indiceToken)
    print('analisis satisfactorio: ', analisis)


print()
print()
print('Analizador sintactico')
print()
print()
inicio(tokenActual)


