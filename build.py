import os, textwrap
BASE="https://stimkine.github.io/guillermodiaz"   # con dominio propio: "https://tudominio.cl"
PREFIX="/guillermodiaz"                             # con dominio propio: ""
WA="56989331095"                      # reemplazar: 56 + número sin +
EMAIL="stimkine@gmail.com"
OUT="docs"
os.makedirs(OUT+"/articulos",exist_ok=True)

NAV=[("/","Inicio"),("/sobre-mi/","Sobre mí"),("/experiencia-profesional/","Experiencia"),("/areas-de-rehabilitacion/","Áreas"),("/atencion-en-consulta-y-domicilio/","Consulta y domicilio"),("/mi-enfoque-clinico/","Enfoque clínico"),("/articulos/","Artículos"),("/contacto/","Contacto")]

def fix(h):
    return h.replace('href="/','href="'+PREFIX+'/').replace('src="/','src="'+PREFIX+'/')

def page(path,title,desc,body,schema="",og="website"):
    url=BASE+path
    nav="".join(f'<a href="{h}"{" aria-current=page" if h==path or (h!="/" and path.startswith(h)) else ""}>{t}</a>' for h,t in NAV)
    html=f'''<!doctype html>
<html lang="es-CL"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="{og}"><meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}"><meta property="og:url" content="{url}">
<meta property="og:locale" content="es_CL"><meta property="og:image" content="{BASE}/img/og.jpg">
<meta name="theme-color" content="#fbfaf6">
<link rel="stylesheet" href="/css/style.css">
{schema}
</head><body>
<a class="skip" href="#main">Ir al contenido</a>
<header class="top"><div class="wrap bar">
<a class="brand" href="/">Guillermo Díaz<small>Kinesiólogo y Licenciado en Kinesiología</small></a>
<input type="checkbox" id="mt" class="mt"><label for="mt" class="mb">Menú</label>
<nav aria-label="Principal">{nav}</nav></div></header>
<main id="main">{body}</main>
<footer><div class="wrap fgrid">
<div><strong>Guillermo Díaz Viveros</strong><br>Kinesiólogo y Licenciado en Kinesiología (UDLA)<br>Fundador y Director Clínico de StimKine Movimiento y Salud SpA<br><a href="https://stimkine.github.io/">StimKine Movimiento y Salud</a> · <a href="https://www.instagram.com/StimKine_movimientoysalud/">Instagram</a> · <a href="https://cl.linkedin.com/in/guillermo-diaz-viveros-901a2b8b" target="_blank" rel="noopener noreferrer">LinkedIn</a><br>Consulta y domicilio en San Ramón, San Miguel y La Cisterna · Santiago Sur</div>
<div><a href="/experiencia-profesional/">Experiencia profesional</a><br><a href="/areas-de-rehabilitacion/">Áreas de rehabilitación</a><br><a href="/articulos/">Artículos</a><br><a href="/contacto/">Contacto</a></div>
<p class="fine">La información de este sitio es educativa y no reemplaza una evaluación clínica presencial. No se realizan diagnósticos a distancia.</p>
</div></footer>
<a class="wa" href="https://wa.me/{WA}?text=Hola%20Guillermo%2C%20quisiera%20solicitar%20una%20evaluaci%C3%B3n." rel="noopener">Solicitar evaluación por WhatsApp</a>
</body></html>'''
    d=OUT+path
    os.makedirs(d,exist_ok=True)
    open(d+"index.html","w",encoding="utf-8").write(fix(html))

CTA='<p><a class="btn" href="https://wa.me/'+WA+'?text=Hola%20Guillermo%2C%20quisiera%20solicitar%20una%20evaluaci%C3%B3n.">Solicitar evaluación por WhatsApp</a></p>'

schema_home='<script type="application/ld+json">{"@context":"https://schema.org","@type":"Person","name":"Guillermo Díaz Viveros","jobTitle":"Kinesiólogo y Licenciado en Kinesiología","url":"https://stimkine.github.io/guillermodiaz/","email":"mailto:stimkine@gmail.com","telephone":"+56989331095","worksFor":{"@type":"Organization","name":"StimKine Movimiento y Salud SpA","url":"https://stimkine.github.io/"},"sameAs":["https://www.instagram.com/StimKine_movimientoysalud/"]}</script>'

# INICIO
page("/","Guillermo Díaz | Kinesiólogo en San Ramón y Santiago Sur",
"Guillermo Díaz, kinesiólogo: rehabilitación para adolescentes, adultos y personas mayores, en consulta y a domicilio en San Ramón, San Miguel y La Cisterna.",
f'''<section class="hero wrap"><div>
<h1>Guillermo Díaz Viveros</h1><p class="sub">Kinesiólogo y Licenciado en Kinesiología · Fundador y Director Clínico de StimKine Movimiento y Salud SpA</p><h2>Kinesiología en San Ramón y Santiago Sur</h2>
<p class="lead">Atención kinesiológica integral para adolescentes, adultos y personas mayores. Evaluación individualizada y rehabilitación orientada a recuperar el movimiento, la funcionalidad y la calidad de vida.</p>
{CTA}
<p class="sub">Consulta y kinesiología a domicilio en San Ramón, San Miguel y La Cisterna.</p></div>
<figure class="portrait"><img src="{PREFIX}/img/guillermo-diaz-retrato.webp" alt="Guillermo Díaz Viveros, kinesiólogo y licenciado en Kinesiología, en su consulta" width="640" height="850" fetchpriority="high"></figure></section>

<section class="band"><div class="wrap"><h2>Una atención basada en el criterio clínico</h2>
<p class="wide">No aplico máquinas ni técnicas de forma automática. Evalúo tu función, identifico qué te limita, defino objetivos contigo y diseño un plan para ti. Después reevalúo y registro tus avances. <a href="/mi-enfoque-clinico/">Ver cómo trabajo</a>.</p></div></section>

<section class="wrap two"><div><h2>Experiencia clínica diversa</h2>
<p>Clínica Indisa (UPC, unidad coronaria, unidad médico-quirúrgica y traumatología), centros de rehabilitación, ELEAM y la dirección clínica de StimKine.</p>
<p><a href="/experiencia-profesional/">Ver experiencia profesional</a></p></div>
<div><h2>A quién atiendo</h2>
<p>Adolescentes, adultos y personas mayores con dolor, lesiones, recuperación posterior a una cirugía o fractura, y pérdida de fuerza, equilibrio o movilidad. También a familiares que buscan rehabilitación para sus padres.</p>
<p><a href="/areas-de-rehabilitacion/">Ver áreas de rehabilitación</a></p></div></section>

<section class="wrap"><h2>Cómo solicitar una evaluación</h2>
<p class="wide">Escríbeme por WhatsApp contando brevemente qué ocurre y en qué comuna vives. Coordinamos la evaluación en consulta o en tu domicilio. <a href="/atencion-en-consulta-y-domicilio/">Conocer ambas modalidades</a>.</p>{CTA}</section>

<section class="wrap"><h2>Artículos recientes</h2>
<ul class="list"><li><a href="/articulos/que-hacer-frente-al-dolor-lumbar/">¿Qué hacer frente al dolor lumbar?</a></li>
<li><a href="/articulos/dolor-de-rodilla-cuando-consultar-y-que-ejercicio-ayuda/">Dolor de rodilla: cuándo consultar y qué ejercicio ayuda</a></li>
<li><a href="/articulos/como-prevenir-caidas-en-personas-mayores/">¿Cómo prevenir caídas en personas mayores?</a></li></ul></section>''',schema_home)

# SOBRE MI
page("/sobre-mi/","Sobre Guillermo Díaz Viveros | Kinesiólogo, Licenciado en Kinesiología UDLA",
"Quién es Guillermo Díaz Viveros, kinesiólogo y Director Clínico de StimKine: formación, enfoque de trabajo y herramientas de evaluación como EvalKine.",
f'''<div class="wrap prose"><h1>Sobre mí</h1>
<figure class="ph sm" role="img" aria-label="Guillermo Díaz en su consulta"><span>Fotografía en consulta (img/guillermo-consulta.jpg)</span></figure>
<p>Soy Guillermo Díaz Viveros, kinesiólogo y Licenciado en Kinesiología de la Universidad de Las Américas (UDLA). He trabajado en unidades de paciente crítico, traumatología, centros de rehabilitación y residencias de personas mayores. Hoy soy Director Clínico de StimKine Movimiento y Salud SpA y atiendo directamente a mis pacientes.</p>
<h2>Lo que me importa en una atención</h2>
<p>Recuperar la funcionalidad: que puedas caminar con seguridad, volver a tu trabajo o a tus actividades, o mantener tu independencia. Para lograrlo parto de una evaluación clínica y funcional, no de una técnica. Lo explico en <a href="/mi-enfoque-clinico/">mi enfoque clínico</a>.</p>
<h2>Evaluación objetiva y tecnología</h2>
<p>Desarrollé EvalKine, una herramienta de evaluación y seguimiento clínico que uso para organizar evaluaciones, registrar avances y comparar resultados en el tiempo.</p>
<p>Mi trayectoria completa está en <a href="/experiencia-profesional/">experiencia profesional</a>.</p>
{CTA}</div>''')

# EXPERIENCIA
page("/experiencia-profesional/","Áreas de experiencia clínica | Guillermo Díaz Viveros, Kinesiólogo",
"Áreas de experiencia clínica de Guillermo Díaz Viveros: atención en unidades de paciente crítico, cardiovascular, traumatológica, musculoesquelética y geriátrica.",
f'''<div class="wrap prose"><h1>Áreas de experiencia clínica</h1>
<p>Experiencia en distintos contextos de atención y rehabilitación, con adolescentes, adultos y personas mayores.</p>
<ul><li>Atención y rehabilitación en unidades de paciente crítico (UPC).</li><li>Área cardiovascular y unidad coronaria.</li><li>Rehabilitación traumatológica y musculoesquelética.</li><li>Rehabilitación geriátrica y funcional.</li><li>Evaluación y recuperación de la movilidad.</li><li>Atención y rehabilitación de personas mayores en contextos institucionales y domiciliarios.</li></ul>
<p>Actualmente soy fundador y Director Clínico de StimKine Movimiento y Salud SpA, donde participo en la evaluación y atención de pacientes en consulta y a domicilio.</p>
{CTA}</div>''')

# AREAS
areas=[("Rehabilitación musculoesquelética","musculoesqueletica",["Dolor lumbar","Dolor cervical","Dolor de hombro","Dolor de rodilla","Lesiones musculares","Lesiones articulares","Alteraciones de movilidad"],"Evalúo el origen del dolor y de la limitación, y trabajo para que vuelvas a moverte con menos dolor y más confianza.","<a href=\"/articulos/que-hacer-frente-al-dolor-lumbar/\">Dolor lumbar</a> · <a href=\"/articulos/dolor-de-rodilla-cuando-consultar-y-que-ejercicio-ayuda/\">Dolor de rodilla</a>"),
("Rehabilitación traumatológica y postoperatoria","traumatologica-postoperatoria",["Recuperación posterior a cirugías","Recuperación de fracturas","Recuperación de fuerza","Recuperación de movilidad","Reeducación funcional"],"Acompaño la recuperación después de una cirugía o fractura, respetando las indicaciones de tu equipo médico.",""),
("Rehabilitación geriátrica","geriatrica",["Prevención de caídas","Alteraciones del equilibrio","Entrenamiento de marcha","Pérdida de fuerza","Deterioro de movilidad","Recuperación y mantención de autonomía"],"El objetivo es que la persona mayor conserve su independencia y se sienta segura en su vida diaria.","<a href=\"/articulos/como-prevenir-caidas-en-personas-mayores/\">Prevención de caídas</a> · <a href=\"/articulos/fuerza-y-movilidad-en-personas-mayores/\">Fuerza y movilidad</a>"),
("Rehabilitación funcional","funcional",["Entrenamiento terapéutico","Fuerza y resistencia","Movilidad y coordinación","Recuperación de capacidades físicas","Retorno progresivo a actividades cotidianas"],"Programas progresivos para volver a hacer lo que cada persona necesita o quiere hacer.","")]
b='<div class="wrap prose"><h1>Áreas de rehabilitación</h1><p>Atiendo a adolescentes, adultos y personas mayores. Las técnicas y el ejercicio se eligen según la evaluación y las necesidades de cada paciente.</p>'
IMG={"musculoesqueletica":("lumbar-electroterapia",1000,1000,"Paciente en camilla durante una sesión de rehabilitación lumbar con electroterapia"),
"traumatologica-postoperatoria":("escalon-barra-postoperatoria",1000,1000,"Paciente realizando ejercicio de subir un escalón con apoyo en una barra, en la consulta"),
"geriatrica":("marcha-andador",1000,782,"Persona mayor realizando entrenamiento de marcha con andador"),
"funcional":("plancha-funcional",1000,1000,"Paciente realizando un ejercicio de estabilidad de tronco sobre una colchoneta")}
def fig(k):
    f,w,h,a=IMG[k]; return f'<figure class="photo"><img src="/img/{f}.jpg" width="{w}" height="{h}" loading="lazy" alt="{a}"></figure>'
for n,sid,l,t,links in areas:
    b+=f'<section id="{sid}"><h2>{n}</h2><p>{t}</p>'+fig(sid)+'<ul>'+"".join(f"<li>{x}</li>" for x in l)+"</ul>"+(f'<p>Para leer: {links}</p>' if links else "")+"</section>"
b+=CTA+"</div>"
page("/areas-de-rehabilitacion/","Áreas de rehabilitación | Kinesiólogo Guillermo Díaz",
"Rehabilitación musculoesquelética, traumatológica y postoperatoria, geriátrica y funcional: dolor lumbar, rodilla, fracturas, caídas. Santiago Sur.",b)

# MODALIDADES
page("/atencion-en-consulta-y-domicilio/","Kinesiólogo a domicilio y en consulta | San Ramón, San Miguel, La Cisterna",
"Kinesiólogo a domicilio en San Ramón, San Miguel y La Cisterna, y atención en consulta. Kinesiología a domicilio en Santiago Sur.",
f'''<div class="wrap prose"><h1>Atención en consulta y a domicilio</h1>
<h2>Atención en consulta</h2><figure class="photo"><img src="/img/consulta-equipada.jpg" width="1000" height="1000" loading="lazy" alt="Sala de consulta con camilla, barra de apoyo, escalón y láminas anatómicas"></figure><p>Un espacio equipado para la evaluación y la rehabilitación: trabajo de movilidad, fuerza, equilibrio y reeducación funcional.</p>
<h2>Kinesiología a domicilio</h2><p>Visitas a tu casa para personas que necesitan rehabilitarse en su entorno habitual o que tienen dificultades para trasladarse, por ejemplo después de una cirugía o en personas mayores. Permite además trabajar sobre las condiciones reales del hogar.</p>
<h2>Cobertura inicial en Santiago Sur</h2>
<h3>San Ramón</h3><p>Kinesiólogo en San Ramón, en consulta y a domicilio.</p>
<h3>San Miguel</h3><p>Atención kinesiológica en San Miguel.</p>
<h3>La Cisterna</h3><p>Atención kinesiológica en La Cisterna.</p>
<p>Si vives en otra comuna, escríbeme y te confirmo si es posible coordinar la atención.</p>
{CTA}</div>''')

# ENFOQUE
steps=["Evaluación clínica y funcional","Identificación de problemas y limitaciones","Definición de objetivos terapéuticos","Diseño de un plan individualizado","Intervención basada en las necesidades del paciente","Seguimiento y reevaluación","Registro y análisis de resultados"]
page("/mi-enfoque-clinico/","Mi enfoque clínico | Guillermo Díaz, Kinesiólogo",
"Cómo trabajo: evaluación clínica y funcional, objetivos, plan individualizado, seguimiento y registro de resultados con EvalKine.",
'<div class="wrap prose"><h1>Mi enfoque clínico</h1><p>La rehabilitación no consiste en aplicar máquinas o técnicas de manera automática, sino en comprender el problema y trabajar para recuperar la funcionalidad y la calidad de vida.</p><h2>Cómo es una atención</h2><ol class="steps">'+"".join(f"<li>{s}</li>" for s in steps)+'''</ol>
<h2>Registro de avances con EvalKine</h2>
<p>EvalKine es una herramienta de evaluación y seguimiento clínico que desarrollé para organizar evaluaciones, registrar avances y comparar resultados en el tiempo. Es una herramienta de apoyo a mi trabajo; no es un producto médico certificado.</p>'''+CTA+"</div>")

# ARTICULOS
arts=[
("que-hacer-frente-al-dolor-lumbar","¿Qué hacer frente al dolor lumbar?",
"Qué recomienda la evidencia para el dolor lumbar: mantenerse activo, ejercicio, señales de alarma y cuándo consultar a un kinesiólogo.",
'''<p>El dolor lumbar es una de las causas más frecuentes de consulta y de limitación en la vida diaria. En la mayoría de los casos no se debe a una lesión grave y mejora con el tiempo.</p>
<h2>Qué recomienda la evidencia</h2><ul><li><strong>Mantenerse activo:</strong> se recomienda evitar el reposo prolongado y retomar progresivamente las actividades (Foster et al., 2018).</li>
<li><strong>Ejercicio y educación:</strong> son la base del tratamiento y ayudan a prevenir recaídas.</li>
<li><strong>Calor local y analgésicos:</strong> pueden aliviar a corto plazo; los medicamentos deben ser indicados por un médico.</li></ul>
<h2>Cuándo consultar pronto a un médico</h2><p>Si el dolor aparece después de un golpe fuerte, si hay fiebre, pérdida de fuerza en las piernas, adormecimiento en la zona genital o pérdida del control de la orina o las deposiciones.</p>
<h2>Cuándo consultar a un kinesiólogo</h2><p>Si el dolor no mejora en algunas semanas, se repite o limita tu trabajo o tus actividades. La evaluación identifica qué movimientos te limitan y cómo recuperar fuerza y movilidad.</p>
<h2>Referencias</h2><ul class="refs"><li>Foster NE, Anema JR, Cherkin D, et al. Prevention and treatment of low back pain: evidence, challenges, and promising directions. <em>The Lancet</em>. 2018;391(10137):2368-2383.</li></ul>'''),
("dolor-de-rodilla-cuando-consultar-y-que-ejercicio-ayuda","Dolor de rodilla: cuándo consultar y qué ejercicio ayuda",
"Cuándo el dolor de rodilla necesita evaluación y qué dice la evidencia sobre el ejercicio terapéutico en la artrosis de rodilla.",
'''<p>El dolor de rodilla puede aparecer por una lesión, por sobrecarga o por desgaste articular (artrosis). Entender cuál es tu caso orienta el tratamiento.</p>
<h2>Señales para consultar pronto</h2><ul><li>Dolor después de una caída o un golpe.</li><li>Hinchazón marcada, enrojecimiento o calor.</li><li>No poder apoyar el pie o sensación de bloqueo.</li><li>Fiebre junto con el dolor.</li></ul>
<h2>Qué dice la evidencia sobre el ejercicio</h2><p>Una revisión Cochrane concluyó que el ejercicio terapéutico en personas con artrosis de rodilla reduce el dolor y mejora la función física (Fransen et al., 2015). Por eso el ejercicio, ajustado a cada persona, es parte central de la rehabilitación.</p>
<h2>Cuándo consultar a un kinesiólogo</h2><p>Si el dolor limita caminar, subir escaleras o levantarte de una silla, o si persiste más de unas semanas. La evaluación define qué ejercicio es adecuado y cómo progresarlo.</p>
<h2>Referencias</h2><ul class="refs"><li>Fransen M, McConnell S, Harmer AR, et al. Exercise for osteoarthritis of the knee. <em>Cochrane Database of Systematic Reviews</em>. 2015;1:CD004376.</li></ul>'''),
("como-prevenir-caidas-en-personas-mayores","¿Cómo prevenir caídas en personas mayores?",
"Qué factores aumentan el riesgo de caídas en personas mayores y qué dice la evidencia sobre el ejercicio para prevenirlas.",
'''<p>Las caídas son frecuentes en personas mayores y pueden cambiar la vida de una persona: una fractura, el miedo a volver a caer o la pérdida de independencia. Gran parte del riesgo se puede reducir.</p>
<h2>Por qué aumenta el riesgo</h2><p>Con los años pueden disminuir la fuerza de las piernas, el equilibrio y la velocidad de reacción. A eso se suman algunos medicamentos, la visión, el calzado, el entorno del hogar y la inactividad.</p>
<h2>Qué ayuda</h2><ul><li><strong>Ejercicio específico:</strong> una revisión Cochrane concluyó que los programas de ejercicio reducen la tasa de caídas en personas mayores que viven en la comunidad, y que los que desafían el equilibrio son los más efectivos (Sherrington et al., 2019).</li>
<li><strong>Fuerza de piernas y marcha:</strong> se trabajan de forma progresiva y adaptada.</li>
<li><strong>Revisar el hogar:</strong> iluminación, alfombras sueltas, escalones y baño.</li>
<li><strong>Consultar al médico</strong> por medicamentos, visión y mareos.</li></ul>
<h2>Cuándo consultar a un kinesiólogo</h2><p>Si hubo una caída, hay inseguridad al caminar, se apoya en los muebles o se evita salir por miedo a caer. Más sobre <a href="/areas-de-rehabilitacion/#geriatrica">rehabilitación geriátrica</a>.</p>
<h2>Referencias</h2><ul class="refs"><li>Sherrington C, Fairhall NJ, Wallbank GK, et al. Exercise for preventing falls in older people living in the community. <em>Cochrane Database of Systematic Reviews</em>. 2019;1:CD012424.</li></ul>'''),
("fuerza-y-movilidad-en-personas-mayores","Fuerza y movilidad en personas mayores: por qué importan",
"Por qué mantener la fuerza muscular y el equilibrio ayuda a conservar la autonomía, según las recomendaciones de la OMS.",
'''<p>La fuerza de las piernas y el equilibrio influyen en cosas cotidianas: levantarse de una silla, subir escaleras, salir a caminar. Mantenerlas ayuda a conservar la autonomía.</p>
<h2>Qué recomienda la OMS</h2><p>Las guías de la OMS recomiendan que las personas de 65 años o más hagan actividad física variada, con énfasis en el equilibrio funcional y el entrenamiento de fuerza de intensidad moderada o mayor, tres o más días a la semana, además de actividad aeróbica regular (Bull et al., 2020).</p>
<h2>Cómo empezar de forma segura</h2><ul><li>Parte con ejercicios simples y progresa gradualmente.</li><li>Si hay dolor, mareos, antecedentes de caídas o una cirugía reciente, consulta antes.</li><li>Pide una evaluación para que el programa se ajuste a tu condición.</li></ul>
<h2>Referencias</h2><ul class="refs"><li>Bull FC, Al-Ansari SS, Biddle S, et al. World Health Organization 2020 guidelines on physical activity and sedentary behaviour. <em>British Journal of Sports Medicine</em>. 2020;54(24):1451-1462.</li></ul>''')]
for slug,t,d,body in arts:
    sch=f'<script type="application/ld+json">{{"@context":"https://schema.org","@type":"Article","headline":"{t}","author":{{"@type":"Person","name":"Guillermo Díaz Viveros"}},"inLanguage":"es-CL","mainEntityOfPage":"{BASE}/articulos/{slug}/"}}</script>'
    page(f"/articulos/{slug}/",f"{t} | Guillermo Díaz Kinesiólogo",d,
    f'<article class="wrap prose"><h1>{t}</h1>{body}<hr><p>Este artículo es educativo y no reemplaza una evaluación. ¿Quieres una evaluación personalizada?</p>{CTA}</article>',sch,"article")
page("/articulos/","Artículos de kinesiología y rehabilitación | Guillermo Díaz",
"Artículos sobre dolor lumbar, dolor de rodilla, caídas y fuerza en personas mayores, escritos por el kinesiólogo Guillermo Díaz.",
'<div class="wrap prose"><h1>Artículos y educación</h1><p>Información clara y fundamentada para entender mejor tu recuperación.</p><ul class="list">'+"".join(f'<li><a href="/articulos/{s}/">{t}</a><br><span>{d}</span></li>' for s,t,d,_ in arts)+"</ul></div>")

# CONTACTO
page("/contacto/","Contacto | Guillermo Díaz, Kinesiólogo",
"Solicita una evaluación kinesiológica con Guillermo Díaz por WhatsApp o correo. Consulta y domicilio en San Ramón, San Miguel y La Cisterna.",
f'''<div class="wrap prose"><h1>Contacto</h1>
{CTA}
<p>Correo: <a href="mailto:{EMAIL}">{EMAIL}</a></p>
<p>Consulta y domicilio en San Ramón, San Miguel y La Cisterna. <a href="/atencion-en-consulta-y-domicilio/">Ver modalidades</a>.</p>
<h2>Envíame un mensaje</h2>
<form id="f"><label>Nombre<input name="n" required></label>
<label>Comuna<input name="c" required></label>
<label>¿Qué te ocurre?<textarea name="m" rows="4" required></textarea></label>
<button class="btn" type="submit">Enviar por WhatsApp</button></form>
<script>document.getElementById('f').addEventListener('submit',function(e){{e.preventDefault();var d=new FormData(this);var t='Hola Guillermo, soy '+d.get('n')+' ('+d.get('c')+'). '+d.get('m');location.href='https://wa.me/{WA}?text='+encodeURIComponent(t);}});</script>
</div>''')

open(OUT+"/404.html","w",encoding="utf-8").write(fix('<!doctype html><html lang="es-CL"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Página no encontrada</title><link rel="stylesheet" href="/css/style.css"><div class="wrap prose"><h1>Página no encontrada</h1><p><a href="/">Volver al inicio</a></p></div></html>'))
urls=["/","/sobre-mi/","/experiencia-profesional/","/areas-de-rehabilitacion/","/atencion-en-consulta-y-domicilio/","/mi-enfoque-clinico/","/articulos/","/contacto/"]+[f"/articulos/{s}/" for s,*_ in arts]
open(OUT+"/sitemap.xml","w").write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+"\n".join(f"<url><loc>{BASE}{u}</loc></url>" for u in urls)+"\n</urlset>\n")
open(OUT+"/robots.txt","w").write(f"User-agent: *\nAllow: /\nSitemap: {BASE}/sitemap.xml\n")
