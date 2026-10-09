# Módulo 10 — grep, find y locate: buscar texto y archivos

Manual Maestro de Linux y Shell Scripting — Edición 2026 · v3 · Décima entrega.

[Índice del manual](README.md) · [← Módulo 9](modulo-09-pipes-composicion-comandos.md) · [Arquitectura](00-indice-arquitectura.md) · [Módulo 11 →](modulo-11-usuarios-grupos-identidad.md)

## 1. Qué aprenderás

Al terminar este módulo podrás distinguir tres tareas diferentes:

- buscar **texto dentro de contenido** con `grep`;
- buscar **archivos y directorios recorriendo una ruta** con `find`;
- buscar **nombres mediante una base de datos indexada** con una implementación de `locate`, cuando esté disponible.

También aprenderás a:

- usar `grep -i` y `grep -n`;
- combinar `grep` con pipes;
- usar `find` con `-type` y `-name`;
- entender por qué conviene citar patrones como `"*.txt"`;
- reconocer que `locate` puede mostrar resultados desactualizados;
- evitar búsquedas innecesarias sobre todo el sistema.

Conocimientos previos:
- rutas;
- lectura de archivos;
- stdout, stderr y redirecciones;
- tuberías.

**Seguridad:** todas las prácticas se limitan a `~/linux-lab`. No recorreremos `/` como ejercicio de principiante. Buscar sobre todo el sistema puede producir muchas salidas, errores de permisos y exposición innecesaria de rutas privadas. No uses `sudo` para “ver más resultados”.

## 2. Tres preguntas distintas

Antes de elegir una herramienta, identifica qué quieres encontrar.

### Pregunta A — “¿En qué líneas aparece esta palabra?”

Herramienta:

```text
grep
```

### Pregunta B — “¿Dónde está un archivo con este nombre?”

Herramienta:

```text
find
```

### Pregunta C — “¿Existe rápidamente algún nombre parecido en el índice del sistema?”

Posible herramienta:

```text
locate
```

No son sinónimos.

## 3. grep — buscar patrones dentro del texto

`grep` examina texto y selecciona líneas que coinciden con un patrón.

Ejemplo:

```bash
grep 'error' registro.txt
```

Si `registro.txt` contiene:

```text
inicio correcto
error al abrir archivo
proceso completado
```

la salida sería:

```text
error al abrir archivo
```

**Modelo mental:**

```text
texto ──► grep patrón ──► líneas coincidentes
```

Referencia principal: GNU Grep Manual.

## 4. Patrón no significa siempre “texto literal simple”

`grep` trabaja con patrones y, por defecto, interpreta una forma de expresiones regulares.

En este módulo usaremos patrones sencillos como:

```text
error
Linux
usuario
```

No estudiaremos todavía expresiones regulares en profundidad.

**Regla:** si solo quieres aprender búsqueda básica, empieza con texto simple y no agregues símbolos especiales al azar.

## 5. grep -i — ignorar mayúsculas y minúsculas

Ejemplo:

```bash
grep -i 'linux' notas.txt
```

Puede coincidir con:

```text
linux
Linux
LINUX
```

`-i` hace una comparación que ignora diferencias de mayúsculas/minúsculas según el comportamiento y configuración local de la herramienta.

**Error típico:** creer que `grep 'linux'` y `grep -i 'linux'` siempre producen exactamente lo mismo.

## 6. grep -n — mostrar número de línea

Ejemplo:

```bash
grep -n 'error' registro.txt
```

Una salida ilustrativa:

```text
4:error al abrir archivo
```

El número indica la línea donde apareció la coincidencia.

Esto es útil para localizar rápidamente la posición dentro de un archivo.

## 7. Combinar opciones

Puedes combinar:

```bash
grep -in 'linux' notas.txt
```

o escribir opciones separadas:

```bash
grep -i -n 'linux' notas.txt
```

En estos ejemplos ambas formas expresan la misma intención: ignorar mayúsculas/minúsculas y mostrar números de línea.

Para aprender, prioriza claridad sobre abreviar todo.

## 8. grep y stdin

`grep` también puede recibir texto desde stdin.

Ejemplo:

```bash
printf 'rojo\nverde\nazul\n' | grep 'verde'
```

Salida:

```text
verde
```

Aquí no leyó un archivo nombrado: recibió texto mediante el pipe.

Esto conecta directamente con el Módulo 9.

## 9. grep no busca nombres de archivos por defecto

Si escribes:

```bash
grep 'reporte' archivo.txt
```

`grep` busca el patrón dentro del contenido de `archivo.txt`.

No está buscando automáticamente un archivo llamado `reporte`.

Para nombres y rutas usaremos `find`.

## 10. find — recorrer una ruta real

`find` recorre una jerarquía de directorios desde un punto inicial y evalúa criterios.

Ejemplo:

```bash
find ~/linux-lab -type f
```

Explicación:

- `find` = herramienta;
- `~/linux-lab` = ruta inicial;
- `-type f` = selecciona archivos ordinarios.

Puede mostrar muchas rutas si tu laboratorio ya tiene varias prácticas.

Referencia principal: GNU Findutils Manual.

## 11. Buscar solo directorios

```bash
find ~/linux-lab -type d
```

`-type d` selecciona directorios.

Comparación:

```text
-type f = archivos ordinarios
-type d = directorios
```

No necesitas memorizar todavía todos los tipos posibles.

## 12. find -name — buscar por nombre

Ejemplo:

```bash
find ~/linux-lab -type f -name "*.txt"
```

Esto recorre el laboratorio y selecciona archivos ordinarios cuyo nombre coincide con el patrón `*.txt`.

### ¿Por qué usamos comillas?

Porque queremos que el patrón:

```text
*.txt
```

llegue a `find` para que **find** lo interprete.

Si lo dejas sin citar, la shell podría expandirlo antes dependiendo de los nombres presentes en tu directorio actual.

Regla de este módulo:

```bash
-name "*.txt"
```

es preferible para que el patrón llegue completo a `find`.

## 13. El asterisco en -name

Dentro del patrón de `find`:

```text
*
```

puede representar una secuencia de caracteres en el nombre.

Ejemplo:

```text
*.txt
```

puede coincidir con:

```text
notas.txt
reporte.txt
a.txt
```

No significa “buscar dentro del contenido”.

## 14. find es sensible a la ruta inicial

Compara:

```bash
find .
```

con:

```bash
find ~/linux-lab
```

`.` significa “desde aquí”.

`~/linux-lab` fija explícitamente el laboratorio.

Para principiantes, la segunda forma suele ser más clara cuando queremos limitar el alcance.

## 15. Evitar find /

Esta orden:

```text
find /
```

inicia desde la raíz del sistema.

Puede:

- recorrer una cantidad enorme de rutas;
- producir errores de permisos;
- mostrar rutas privadas;
- tardar mucho;
- consumir recursos innecesariamente.

No la necesitamos para aprender `find`.

**Regla:** practica con una ruta concreta y pequeña.

## 16. find y errores de permisos

Aunque una búsqueda sea de lectura, puede intentar entrar en lugares para los que tu usuario no tiene acceso.

Si aparece:

```text
Permission denied
```

no añadas `sudo` automáticamente.

Pregunta primero:

> ¿Necesito realmente buscar en esa ruta?

En nuestras prácticas, la respuesta será normalmente no.

## 17. Buscar por nombre exacto

Ejemplo:

```bash
find ~/linux-lab -type f -name "notas.txt"
```

Esto busca archivos ordinarios llamados exactamente `notas.txt` según el patrón proporcionado.

No examina el contenido de esos archivos.

## 18. Buscar texto dentro de varios archivos encontrados

Más adelante aprenderás formas robustas de combinar `find` con otras herramientas.

Por ahora no construiremos pipelines complejas con nombres de archivo, porque los nombres pueden contener:

- espacios;
- saltos de línea;
- guiones iniciales;
- otros caracteres especiales.

No uses como regla general:

```text
for archivo in $(find ...)
```

Ese patrón puede romper nombres válidos.

En este nivel, primero aprende a obtener rutas correctamente.

## 19. locate — búsqueda por índice

Una herramienta tipo `locate` puede buscar nombres usando una base de datos previamente construida.

Ejemplo conceptual:

```bash
locate ejemplo.txt
```

La ventaja principal suele ser velocidad: no necesita recorrer todas las rutas en tiempo real en cada búsqueda.

Pero existe una diferencia fundamental:

```text
find   = recorre rutas actuales
locate = consulta un índice
```

## 20. locate puede no estar instalado

No todas las distribuciones instalan una herramienta `locate` por defecto.

Además, la implementación puede variar.

En sistemas actuales podrías encontrar, por ejemplo, una implementación como `plocate`, que normalmente proporciona el comando `locate`.

No instales nada solo para completar este módulo.

Comprueba primero:

```bash
command -v locate
```

Si no produce una ruta, registra:

```text
locate no disponible en mi entorno
```

y continúa con `grep` y `find`.

## 21. La base de datos puede estar desactualizada

Si acabas de crear:

```text
~/linux-lab/archivo-nuevo.txt
```

`find` puede localizarlo inmediatamente porque recorre la jerarquía actual.

`locate` puede no mostrarlo todavía si su índice no se ha actualizado.

Esa es una de las diferencias más importantes del módulo.

## 22. updatedb: concepto, no práctica administrativa

Las implementaciones de `locate` suelen disponer de un mecanismo para actualizar la base de datos, tradicionalmente mediante una herramienta llamada `updatedb`.

Actualizar una base del sistema puede depender de:

- distribución;
- implementación;
- permisos;
- servicios o temporizadores configurados.

No ejecutaremos `sudo updatedb` como receta universal.

Para este módulo basta entender por qué un índice puede no reflejar cambios recientes.

## 23. locate no sustituye find

Usa `find` cuando necesites:

- controlar exactamente la ruta recorrida;
- buscar el estado actual;
- filtrar por tipo;
- construir criterios sobre la jerarquía real.

Usa `locate`, cuando esté disponible, para una búsqueda rápida basada en nombres indexados.

## 24. Preparar el laboratorio

Entra:

```bash
cd ~/linux-lab
pwd
ls -la
```

Comprueba:

```bash
ls -ld ./modulo-10-busquedas
```

Si no existe:

```bash
mkdir modulo-10-busquedas
```

Después:

```bash
cd ./modulo-10-busquedas
pwd
ls -la
```

No borres una práctica anterior.

## 25. Crear datos de práctica

Primero comprueba cada nombre en el laboratorio con `ls -ld documentos`, `ls -ld registros` y `ls -ld notas`. Si alguno ya existe, **detente y revisa su contenido**; no sobrescribas prácticas anteriores.

Solo si los tres nombres están libres, crea los subdirectorios:

```bash
mkdir documentos
mkdir registros
mkdir notas
```

Verifica con `ls -ld documentos registros notas` antes de crear archivos.

Crea archivos:

```bash
printf 'Linux es el núcleo\nBash es una shell\n' > documentos/conceptos.txt
printf 'inicio correcto\nERROR de prueba\nfin correcto\n' > registros/app.log
printf 'aprender grep\naprender find\naprender pipes\n' > notas/tareas.txt
```

Estas redirecciones reemplazan los archivos destino si ya existen.

Por eso ejecútalas solo si acabas de crear esta práctica o ya verificaste que el contenido puede reemplazarse.

## 26. Práctica A — grep simple

Ejecuta:

```bash
grep 'Bash' documentos/conceptos.txt
```

Predice la línea antes de mirar.

Después prueba:

```bash
grep 'bash' documentos/conceptos.txt
```

Compara el resultado.

## 27. Práctica B — grep -i

```bash
grep -i 'bash' documentos/conceptos.txt
```

Explica por qué ahora puede coincidir aunque el archivo tenga `Bash` con mayúscula.

## 28. Práctica C — grep -n

```bash
grep -n 'ERROR' registros/app.log
```

Debes poder identificar:

- número de línea;
- contenido coincidente.

No memorices el formato como una regla universal para todas las opciones; interpreta esta salida concreta.

## 29. Práctica D — grep mediante pipe

```bash
cat notas/tareas.txt | grep 'find'
```

Después usa la forma más directa:

```bash
grep 'find' notas/tareas.txt
```

Explica por qué la segunda es más simple para este caso.

## 30. Práctica E — find por tipo

Desde `modulo-10-busquedas`:

```bash
find . -type f
```

Después:

```bash
find . -type d
```

Identifica qué resultados corresponden a archivos y cuáles a directorios.

## 31. Práctica F — find por extensión

```bash
find . -type f -name "*.txt"
```

Debe encontrar los archivos `.txt` de la práctica, pero no necesariamente `app.log`.

Explica por qué las comillas alrededor de `*.txt` son importantes.

## 32. Práctica G — nombre exacto

```bash
find . -type f -name "tareas.txt"
```

El resultado debe incluir la ruta relativa a `notas/tareas.txt`.

Ahora explica la diferencia entre:

```bash
grep 'tareas' archivo.txt
```

y:

```bash
find . -name "tareas.txt"
```

## 33. Práctica H — comprobar locate

```bash
command -v locate
```

Si muestra una ruta, puedes probar dentro de tu propio laboratorio:

```bash
locate modulo-10-busquedas
```

Si no muestra resultados, no significa necesariamente que la carpeta no exista. El índice puede no estar actualizado o puede aplicar reglas de visibilidad.

Si `locate` no está instalado, no hagas nada más.

## 34. grep recursivo: introducción limitada

GNU `grep` puede buscar recursivamente con opciones como:

```bash
grep -r 'aprender' .
```

Dentro de nuestra pequeña carpeta de práctica, esto puede ser útil.

Pero no uses:

```text
grep -r palabra /
```

como ejercicio: recorrer todo el sistema genera ruido, errores de permisos y posibles exposiciones.

En módulos posteriores veremos filtros y estrategias más precisas.

## 35. grep y archivos binarios

Una búsqueda recursiva puede encontrar archivos que no son texto.

`grep` tiene comportamientos y opciones para esos casos, pero no los estudiaremos todavía.

Por ahora limita la práctica a archivos de texto creados por nosotros.

## 36. Errores frecuentes

| Error | Problema | Corrección |
|---|---|---|
| Usas `grep` para localizar un nombre de archivo | `grep` busca texto/patrones | Usa `find` para rutas/nombres |
| Usas `find` esperando buscar contenido | `find` evalúa objetos y rutas | Usa `grep` para contenido |
| `locate` no encuentra un archivo recién creado | Índice desactualizado o no disponible | Usa `find` para el estado actual |
| Escribes `-name *.txt` sin comillas | La shell puede expandir el patrón antes | Usa `-name "*.txt"` |
| Ejecutas `find /` y aparecen cientos de errores | Alcance demasiado amplio | Limita la ruta |
| Añades `sudo` por errores de permisos | Estás ampliando acceso sin necesidad | Revisa si debes buscar ahí |
| `grep` no coincide por mayúsculas | La búsqueda normal distingue caso | Usa `-i` si esa es la intención |

## 37. Método para elegir herramienta

Hazte estas preguntas:

1. ¿Busco texto dentro de contenido?
   - `grep`.

2. ¿Busco un objeto por ruta, nombre o tipo?
   - `find`.

3. ¿Quiero una búsqueda rápida por índice y acepto que pueda estar desactualizada?
   - `locate`, si existe.

Esta decisión es más importante que memorizar muchas opciones.

## 38. Práctica independiente

Sin copiar la secuencia exacta:

1. crea dos carpetas;
2. crea al menos cuatro archivos de texto;
3. incluye una palabra común en dos de ellos;
4. usa `grep` para encontrar las líneas;
5. repite ignorando mayúsculas/minúsculas;
6. usa `find` para listar solo archivos `.txt`;
7. usa `find` para localizar un nombre exacto;
8. explica qué pasaría si `locate` no muestra un archivo recién creado;
9. no busques desde `/` y no uses `sudo`.

## 39. Mini evaluación

1. ¿Qué herramienta busca patrones dentro del texto?
   - A) `grep`
   - B) `find`
   - C) `cd`

2. ¿Qué herramienta recorre rutas y puede filtrar por nombre o tipo?
   - A) `grep`
   - B) `find`
   - C) `cat`

3. ¿Qué significa `grep -i`?
   - A) Ignorar diferencias de mayúsculas/minúsculas.
   - B) Instalar grep.
   - C) Buscar solo directorios.

4. ¿Qué aporta `grep -n`?
   - A) Número de línea.
   - B) Nombre del usuario.
   - C) Tamaño del disco.

5. En `find . -type f -name "*.txt"`, ¿por qué citamos `*.txt`?
   - A) Para que el patrón llegue a `find` sin expansión prematura de la shell.
   - B) Porque `find` exige comillas en todos los argumentos.
   - C) Para usar `sudo`.

6. ¿`locate` consulta necesariamente el sistema de archivos en tiempo real?
   - A) Sí.
   - B) No.

7. Si acabas de crear un archivo y necesitas encontrarlo con certeza dentro de una ruta, ¿qué elegirías primero?
   - A) `find`
   - B) `locate`

8. ¿Debes ejecutar `find /` con `sudo` como práctica básica?
   - A) Sí.
   - B) No.

## 40. Registro de aprendizaje

Puedes responder:

```text
grep sirve para:
find sirve para:
locate sirve para:
grep -i significa:
grep -n significa:
-type f significa:
-type d significa:
¿Por qué cito "*.txt"?:
Si locate no encuentra algo recién creado:
Un error que ya sé identificar:
Algo que todavía confundo:
Estado: EN APRENDIZAJE / PRACTICADO
```

No se marca como dominado con una sola búsqueda correcta. Debes poder escoger la herramienta sin que el tutor te diga cuál corresponde.

## 41. Fuentes y límites

Fuentes principales:

- GNU Grep Manual:
  https://www.gnu.org/software/grep/manual/grep.html
- GNU Findutils Manual:
  https://www.gnu.org/software/findutils/manual/html_mono/find.html
- plocate:
  https://plocate.sesse.net/

Se posponen:

- expresiones regulares detalladas;
- `grep -E`, `grep -F`, contexto y colores;
- `find -exec`;
- `-print0` y procesamiento NUL;
- criterios por permisos, fechas y tamaños;
- diferencias detalladas entre `locate`, `mlocate` y `plocate`;
- búsquedas administrativas del sistema.

**Estado de la lección:** redactada y revisada documentalmente. La práctica real del estudiante sigue pendiente.

---

**Siguiente:** [Módulo 11 — Usuarios y grupos: whoami, id, UID, GID e identidad](modulo-11-usuarios-grupos-identidad.md) · [Volver al índice](README.md)
