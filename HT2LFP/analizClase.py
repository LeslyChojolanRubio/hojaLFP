###
# '''
# LISTA = LISTA coma id
#         |id










# INICIO = LISTA          Recomendable crear un estado de inicio

# LISTA = id LISTADOS

# LISTADOS = coma id LISTADOS
#         | Epsilon
# '''
# analizador lexico simulado
listaTokens = []
listaTokens.append({'lexema': 'id1', 'tipo': 'id', 'linea': 1, 'columna': 1})
listaTokens.append({'lexema': ',', 'tipo': 'coma', 'linea': 1, 'columna': 6})
listaTokens.append({'lexema': 'id2', 'tipo': 'id', 'linea': 1, 'columna': 11})
listaTokens.append({'lexema': ',', 'tipo': 'coma', 'linea': 1, 'columna': 16})
listaTokens.append({'lexema': 'id3', 'tipo': 'id', 'linea': 1, 'columna': 21})

for t in listaTokens:
    print(t['lexema'])

#cada no terminal es un estado o una funcion del analizador sintáctico. Algunas funciones son recursivas. Cada vez que necesite reconocer un token coloco un if.

# analizador sintactico /parser   cada función reconoce tokens
tokenActual = 0    #variable global


def listados(indiceToken):
    if indiceToken < len(listaTokens):
        if listaTokens[indiceToken]['tipo'] == 'coma':
            #print('va bien')
            indiceToken += 1
            if listaTokens[indiceToken]['tipo'] == 'id':
                listados(indiceToken+1)
                return True
                #print('ya lee el segundo id ' + listaTokens[indiceToken]['lexema'] )
            else:
                print('Error sintáctico: Se esperaba un identificador y se recibió ' + listaTokens[indiceToken]['tipo'] , listaTokens[indiceToken]['linea'], listaTokens[indiceToken]['columna'] )
                return False
        else:
            print('Error sintáctico: Se esperaba una coma y se recibió ' + listaTokens[indiceToken]['tipo'] , listaTokens[indiceToken]['linea'], listaTokens[indiceToken]['columna'] )
            return False

def lista(indiceToken):         #a cada no terminal le corresponde una funcion
    if listaTokens[indiceToken]['tipo'] == 'id':
        return listados(indiceToken+1)
        #print('El token reconocido es: ',listaTokens[indiceToken]['lexema'])
    else:
        print('Error sintáctico: Se esperaba un identificador y se recibió ' + listaTokens[indiceToken]['tipo'] , listaTokens[indiceToken]['linea'], listaTokens[indiceToken]['columna'] )
        return False

def inicio(indiceToken):
    analisis = lista(indiceToken)
    print('analisis satisfactorio: ', analisis)


print()
print()
print('Analizador sintactico')
print()
print()
inicio(tokenActual)
