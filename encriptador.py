'''
archivo = open('texto.txt', 'a')
archivo.write('Prueba de guardado')
archivo.close()

archivo = open('texto.txt', 'r')
print(archivo.read())
'''


def encriptar(texto):
    print(f'Texto para encriptar {texto}')
    textoFinal = ''
    for letra in texto:
        textoFinal += letra + 'x'
    print(textoFinal)

#Esta funcion agregara una letra x despues de cada letra
#El texto se enviara en los parametros
#encriptar('123ddf456')


def desencriptar(texto):
    print(f'Texto para desencriptar {texto}')
    textoFinal = ''
    contador = 0
    for letra in texto:
        if contador % 2 == 0:
            textoFinal += letra
        contador +=1
    print(f'Texto desencriptado es: {textoFinal}')
        
#Lo que hace esta funcion es despues de cada letra par no agregarle una letra al textoFinal
#entonces como cada letra par tiene una x este no se va a agregar.
#desencriptar('prueba de texto')



 
 
    
