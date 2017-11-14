# Formula: (x1 * x2 * ... * xn)^(1/n)

def multiplicacion_recursiva( set_de_datos_a_multiplicar ):
	
	datos_procesados = 0
	cantidad_de_datos = 0
	datos_multiplicados = 1
	multiplicacion_de_30 = []
	
	for x in set_de_datos:

		datos_procesados += 1
		cantidad_de_datos += 1
		datos_multiplicados = float(x) * datos_multiplicados

		if (datos_procesados == 30):

			multiplicacion_de_30.append(datos_multiplicados)
			datos_procesados = 0
			datos_multiplicados = 1

	return multiplicacion_de_30


def potencia_de_nuemeros_multiplicados( set_de_datos_multiplicados ):
	
	numeros_potenciados = []
	potencia = 1/float(30)

	for x in set_de_datos_multiplicados:

		numeros_potenciados.append(x**(potencia))

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

print(multiplicacion_recursiva(set_de_datos))
print(potencia_de_nuemeros_multiplicados(multiplicacion_recursiva(set_de_datos)))
print(sumatoria_final(potencia_de_nuemeros_multiplicados(multiplicacion_recursiva(set_de_datos))))




