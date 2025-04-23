#!/bin/bash

# Archivo de salida
OUTPUT="contenidoDirectorio.txt"

# Limpiar contenido previo si existe
> "$OUTPUT"

# Listar contenido de cada directorio
find /home/devasc -type d | while read dir; do
    echo "Contenido de $dir:" >> "$OUTPUT"
    ls -l "$dir" >> "$OUTPUT" 2>/dev/null
    echo "" >> "$OUTPUT"
done

# Contar archivos y directorios por separado
TOTAL_ARCHIVOS=$(find /home/devasc -type f | wc -l)
TOTAL_DIRECTORIOS=$(find /home/devasc -type d | wc -l)

# Agregar totales al final del archivo
echo "----------------------------------------" >> "$OUTPUT"
echo "Total de archivos: $TOTAL_ARCHIVOS" >> "$OUTPUT"
echo "Total de directorios: $TOTAL_DIRECTORIOS" >> "$OUTPUT"

