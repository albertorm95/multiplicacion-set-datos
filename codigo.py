# Formula: (x1 * x2 * ... * xn)^(1/n)

import csv

def multiplicacion_recursiva( set_de_datos_a_multiplicar, size_window ):
	
	datos_multiplicados = 1
	multi_30_numeros = []

	i = 0
	
	for x in set_de_datos:

		for y in set_de_datos[i:i+size_window]:

			datos_multiplicados = datos_multiplicados * float(y)
		
		multi_30_numeros.append(datos_multiplicados) # Tiene la multi de los 30 numeros
		datos_multiplicados = 1 # Reinicia datos_multiplicados
		i = i + 1 # suma uno en el contador

	#print(multi_30_numeros)

	return potencia_de_nuemeros_multiplicados( multi_30_numeros, size_window )


def potencia_de_nuemeros_multiplicados( set_de_datos_multiplicados, size_window ):
	
	numeros_potenciados = []
	potencia = 1/float(size_window)

	for x in set_de_datos_multiplicados:

		numeros_potenciados.append(x**(potencia))

	#print(numeros_potenciados)

	return numeros_potenciados


def sumatoria_final( set_de_datos_potenciados ):

	valor_final = 1

	for x in set_de_datos_potenciados:

		valor_final = x + valor_final

	return valor_final


with open('datos.txt') as file:
    set_de_datos = file.readlines()

# you may also want to remove whitespace characters like `\n` at the end of each line
set_de_datos = [x.strip() for x in set_de_datos]

datos = multiplicacion_recursiva(set_de_datos, 30)

#print(multiplicacion_recursiva(set_de_datos, 30))
#print(potencia_de_nuemeros_multiplicados(multiplicacion_recursiva(set_de_datos)))
#print(sumatoria_final(potencia_de_nuemeros_multiplicados(multiplicacion_recursiva(set_de_datos))))


thefile = open('test.txt', 'w')
for item in datos:
  thefile.write("%s\n" % item)
