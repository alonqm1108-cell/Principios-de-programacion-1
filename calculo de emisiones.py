cantidad_estudiantes = int(input("Ingrese la cantidad de estudiantes: "))
distancia_recorrida = float(input("Ingrese la distancia recorrida en kilómetros: "))
factor_emision = 0.21  # Factor de emisión en kg CO2 por km
emisiones_totales = cantidad_estudiantes * distancia_recorrida * factor_emision

print("----CALCULO DE LAS EMISIONES DE CO2----")
print(f"Las emisiones totales de CO2 son: {emisiones_totales} kg")
print(f"las emiciones esperadas son de: {emisiones_totales:.2f} kg de CO2")

