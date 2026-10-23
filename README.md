# Sistema Automatizado de Alerta de Inventario (BPA)

Script en Python diseñado para automatizar el control de inventarios en bodegas empresariales. Analiza archivos CSV diarios, detecta productos con stock crítico y genera un reporte de compras urgente.

## 🚀 Características
- **Procesamiento de datos (Parsing):** Lee automáticamente el archivo `inventario.csv`.
- **Lógica de negocio:** Filtra productos con un stock menor o igual a 5 unidades (`stock <= 5`).
- **Generación de reportes:** Crea un archivo `alerta_compras.txt` listo para el departamento de compras.
- **Gestión de archivos:** Mueve el archivo procesado a una carpeta de historial (`historial_inventario`) para mantener el espacio de trabajo limpio.

## 💻 Tecnologías
- Python 3.14 (Módulos nativos: `csv`, `os`, `shutil`)