import csv
import os
import shutil

# 1. Definir rutas de archivos
archivo_inventario = "inventario.csv"
archivo_alerta = "alerta_compras.txt"
carpeta_historial = "historial_inventario"

# Lista para almacenar los productos críticos y contador
productos_criticos = []
total_productos_revisados = 0

# 2. Leer el archivo CSV y filtrar por stock crítico
print("Analizando inventario en bodega...")

with open(archivo_inventario, mode="r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    
    for row in reader:
        total_productos_revisados += 1
        
        # Convertimos el stock de texto a número entero para poder compararlo
        stock = int(row["stock_actual"])
        
        # Condición de negocio: Si el stock es 5 o menos, entra en alerta
        if stock <= 5:
            productos_criticos.append(row)

# 3. Generar el reporte de alerta urgente
with open(archivo_alerta, mode="w", encoding="utf-8") as report:
    report.write("========================================\n")
    report.write("    REPORTE DE ALERTA DE COMPRAS        \n")
    report.write("========================================\n\n")
    report.write(f"Total de productos analizados: {total_productos_revisados}\n")
    report.write(f"Productos en nivel crítico (<= 5): {len(productos_criticos)}\n\n")
    report.write("LISTA DE PRODUCTOS A REABASTECER:\n")
    report.write("----------------------------------------\n")
    
    for prod in productos_criticos:
        report.write(f"- {prod['nombre_producto']} | Stock actual: {prod['stock_actual']} uds | Precio: ${float(prod['precio_unitario']):,.2f}\n")

# 4. Mover el archivo procesado a la carpeta de historial
if not os.path.exists(carpeta_historial):
    os.makedirs(carpeta_historial)

shutil.move(archivo_inventario, os.path.join(carpeta_historial, archivo_inventario))

print("¡Proceso completado! Se ha generado 'alerta_compras.txt' con éxito.")