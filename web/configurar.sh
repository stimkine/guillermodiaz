#!/bin/sh
# Uso: ./configurar.sh https://tudominio.cl 569XXXXXXXX correo@tudominio.cl
sed -i "s#https://DOMINIO_AQUI#$1#g; s#56900000000#$2#; s#contacto@DOMINIO_AQUI#$3#" build.py
rm -rf docs/*.html docs/articulos docs/*/index.html 2>/dev/null; python3 build.py && echo "Listo. Sube la carpeta docs/"
