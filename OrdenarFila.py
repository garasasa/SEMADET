import csv

import sys

actualizados = sys.argv[1]
ordenados = sys.argv[2]
 
nuevos_sorted=list()
#lista donde se van a ir imprimiendo los criterios_sorted
with open(actualizados) as csvfile:
	reader = csv.reader(csvfile, delimiter=',')
	for line_number, row in enumerate(reader): 
	#row es lista, cuando me quiero saltar una lista len(lista)==o: continue		
		if len(row)==0:
			continue
		#row es una lista, para leer cada una de las filas de mi lista defino celda que es igual a la lista row en la columna 0
		celda=row[0]
		if celda.strip()=="":
		#si está vacía la celda strippeada, agregar en la lista .append nueva, una lista vacía []
			nuevos_sorted.append([])
			continue
		sectores=celda.split(";")
		#split regres una lista de strings
		#se hace split a sector. Ej: separa en "Ag", "1,2,3,4" el string "Ag:1,2,3,4"en el primer espacio [0] está el nombre del sector, en el segundo espacio [1], están los criterios.
		politicas_ordenadas=list()
		for sector in sectores:
			if sector.strip()=="":
				continue
			print("line_number={} sector='{}'".format(line_number, sector))
			sector_nombre=sector.split(":")[0]
			criterios=sector.split(":")[1]
			print("sector={}" "criterios={}".format(sector_nombre,criterios))
			criterios=criterios.split(",")
			criterios=list(map(str.strip,criterios))
			criterios=list(filter(str.isnumeric, criterios))
			criterios=list(map(int,criterios))
			print("criterios={}".format(criterios))
			criterios_sorted=sorted(criterios)
			print("sorted={}".format(criterios_sorted))
			criterios_sorted=map(str, criterios_sorted)
			string_sorted=",".join(criterios_sorted)
			print("string_sorted={}".format(string_sorted))
			sector_criterios=[sector_nombre, string_sorted]
			sector_criterios=":".join(sector_criterios)
			politicas_ordenadas.append(sector_criterios)
			#nuevos_sorted.append(sector_criterios)
			#.append adds a single item to the existing list. It modifies the original list by adding the item to the end of the list. After executing append the size of the list increases by one.
		juntar_sectores=";".join(politicas_ordenadas)
		nuevos_sorted.append([juntar_sectores])
print("lista nuevos_sorted={}".format(nuevos_sorted))

with open(ordenados, 'w', newline='') as csvfile:
	writer = csv.writer(csvfile, delimiter=',')
	writer.writerows(nuevos_sorted)
	
	
	
	
	
	

