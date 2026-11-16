# Guillermo Díaz — Kinesiólogo (sitio web personal)

Sitio estático (HTML + CSS, sin dependencias). Se genera con `build.py`.

## Pasos pendientes antes de publicar
1. `./configurar.sh https://TU-DOMINIO 569XXXXXXXX tu@correo.cl` (dominio, WhatsApp, correo).
2. Agregar fotos reales en `docs/img/` (`guillermo-portada.jpg`, `guillermo-consulta.jpg`, `og.jpg`) y reemplazar los marcadores `.ph` por `<img>` con texto alternativo.
3. Verificar las referencias bibliográficas de los artículos antes de publicar.
4. Subir a GitHub, Settings → Pages → Branch `main`, carpeta `/docs`. Si usas dominio propio, agregar `docs/CNAME`.
5. Search Console: verificar dominio y enviar `sitemap.xml`. Crear Google Business Profile.

## Agregar un artículo
Añadir una entrada a la lista `arts` en `build.py` y ejecutar `python3 build.py`. El sitemap se actualiza solo.
