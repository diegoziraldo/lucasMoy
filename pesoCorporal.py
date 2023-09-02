 
def calcularIMC(peso, alturaEnMetros):
    imc = peso / (alturaEnMetros * alturaEnMetros)
    return imc

def pedirElIMC():
    peso = float(input('Ingrese su peso'))
    alturaEnCM = int(input('Ingrese su altura en cm'))
    alturaEnMetros = alturaEnCM/100
    imcF = calcularIMC(peso,alturaEnMetros)

    if imcF<20:
        print('Estado de delgadez')
    if imcF>= 20 and imcF <26:
        print('Estado normal')
    if imcF>= 26 and imcF <30:
        print('Estado sobrepeso')
    if imcF>= 30 and imcF <35:
        print('Estado obesidad') 
 

pedirElIMC() 
