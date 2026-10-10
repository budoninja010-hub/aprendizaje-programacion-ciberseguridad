# Módulo 7 — Leer archivos con cat, less, head y tail

Manual Maestro de Linux y Shell Scripting — Edición 2026 · v3 · Séptima entrega.

[Índice del manual](README.md) · [← Módulo 6](modulo-06-crear-copiar-mover-borrar-seguro.md) · [Arquitectura](00-indice-arquitectura.md) · [Módulo 8 →](modulo-08-stdin-stdout-stderr-redirecciones.md)

## 1. Qué aprenderás

Al terminar este módulo podrás elegir una herramienta adecuada para leer archivos de texto sin modificarlos:

- `cat` para mostrar o concatenar contenido;
- `less` para navegar por archivos largos de forma interactiva;
- `head` para ver las primeras líneas;
- `tail` para ver las últimas líneas;
- `tail -f` para seguir contenido que va creciendo, entendiendo sus límites.

También aprenderás a distinguir **leer** de **editar**, a reconocer cuándo un archivo es demasiado grande para mostrarlo completo y a evitar copiar información sensible al chat o a un repositorio.

Conocimientos previos:
- navegación con `pwd`, `ls` y `cd`;
- rutas;
- creación de archivos dentro de `~/linux-lab`;
- operaciones básicas con archivos.

**Seguridad:** este módulo se centra en lectura. No modificarás archivos del sistema. No uses `sudo` para abrir contenido que normalmente no puedes leer. Si un archivo contiene información privada, credenciales, tokens, nombres personales o datos de red, no lo pegues completo en el chat ni en GitHub.

## 2. Leer no es editar

Una orden de lectura obtiene contenido sin que su objetivo principal sea modificar el archivo.

Ejemplo:

```bash
cat notas.txt
```

Esto muestra el contenido de `notas.txt`.

No es lo mismo que abrir un editor y cambiar el archivo.

Modelo mental:

```text
leer      = observar contenido
editar    = modificar contenido
borrar    = eliminar contenido u objeto
```

**Error típico:** pensar que cualquier comando que “abre” un archivo puede modificarlo. Aquí las herramientas se usan en modo de lectura.

## 3. cat — mostrar y concatenar

`cat` pertenece a GNU Coreutils en los entornos GNU habituales.

Su nombre proviene de **concatenate**: concatenar.

Ejemplo simple:

```bash
cat notas.txt
```

Si el archivo contiene:

```text
uno
dos
tres
```

la salida esperada será:

```text
uno
dos
tres
```

### ¿Para qué sirve cat?

En este curso lo usaremos inicialmente para:

- mostrar archivos pequeños;
- comprobar rápidamente contenido;
- concatenar varios archivos hacia la salida estándar.

Ejemplo conceptual:

```bash
cat parte1.txt parte2.txt
```

`cat` muestra primero el contenido del primer archivo y luego el del segundo.

**Importante:** en este ejemplo no se crea automáticamente un archivo nuevo. La redirección para guardar salidas se estudiará en el Módulo 8.

Referencia: GNU Coreutils — `cat`.

## 4. Cuándo NO conviene usar cat

Si un archivo tiene miles de líneas, `cat archivo-grande.txt` puede llenar rápidamente la terminal.

No suele dañar el archivo, pero puede hacer difícil revisar el contenido.

En ese caso es mejor un paginador como `less`.

**Regla inicial:**

```text
archivo pequeño  → cat puede ser cómodo
archivo largo    → less suele ser más práctico
```

No necesitas calcular un número exacto de líneas. Elige según la facilidad de lectura.

## 5. less — navegar sin cargar toda la experiencia visual de golpe

`less` es un paginador interactivo. Permite revisar contenido por partes.

Ejemplo:

```bash
less notas.txt
```

Al abrirlo, la terminal entra en una vista interactiva.

Controles iniciales:

- `Space` o Page Down: avanzar;
- `b`: retroceder;
- flechas: desplazamiento;
- `/` seguido de texto: buscar hacia adelante;
- `n`: repetir la búsqueda;
- `q`: salir.

No memorices todos los atajos. Para empezar basta con:

```text
Space = avanzar
/     = buscar
q     = salir
```

**Error típico:** creer que quedaste “atrapado” en `less`. Pulsa `q` para salir.

## 6. less no es un editor

Aunque puedes moverte, buscar y examinar texto, el uso básico de `less` en este módulo no está destinado a editar el archivo.

Por eso es útil para inspeccionar:

- documentación;
- archivos de texto largos;
- salidas guardadas;
- ciertos registros, cuando tienes permiso.

No uses `less` como excusa para abrir archivos sensibles que no necesitas revisar.

## 7. head — primeras líneas

`head` muestra el principio de un archivo.

Ejemplo:

```bash
head notas.txt
```

Por defecto, GNU `head` muestra las primeras 10 líneas.

Si quieres una cantidad concreta:

```bash
head -n 5 notas.txt
```

Explicación:

- `head` = muestra el comienzo;
- `-n` = indica que especificarás una cantidad de líneas;
- `5` = número solicitado;
- `notas.txt` = archivo.

**Resultado:** como máximo verás las primeras cinco líneas disponibles.

Referencia: GNU Coreutils — `head`.

## 8. tail — últimas líneas

`tail` muestra el final de un archivo.

Ejemplo:

```bash
tail notas.txt
```

Por defecto, GNU `tail` muestra las últimas 10 líneas.

Para una cantidad concreta:

```bash
tail -n 5 notas.txt
```

Esto muestra las últimas cinco líneas.

**Uso típico:** revisar la parte más reciente de un archivo cuyo contenido se añade al final.

Referencia: GNU Coreutils — `tail`.

## 9. Diferencia entre head y tail

Modelo mental:

```text
head → principio
tail → final
```

Si un archivo tiene:

```text
línea 1
línea 2
línea 3
línea 4
línea 5
```

entonces:

```bash
head -n 2 archivo.txt
```

mostraría:

```text
línea 1
línea 2
```

y:

```bash
tail -n 2 archivo.txt
```

mostraría:

```text
línea 4
línea 5
```

**Ejercicio mental:** sin ejecutar nada, explica qué mostraría `head -n 1` y qué mostraría `tail -n 1`.

## 10. tail -f — seguir un archivo que crece

`tail -f` intenta continuar mostrando contenido nuevo cuando el archivo aumenta.

Ejemplo:

```bash
tail -f actividad.log
```

La terminal puede permanecer esperando cambios.

Para terminar normalmente:

```text
Ctrl + C
```

Esto envía una interrupción al proceso de `tail` que está ejecutándose en primer plano.

### ¿Para qué sirve?

Es útil para observar contenido que una aplicación va añadiendo, por ejemplo en un archivo de registro dentro de un laboratorio propio.

### Límite importante

`tail -f` no significa “monitorizar cualquier cosa automáticamente”. Sigue el archivo según su comportamiento y opciones. Rotación de logs, reemplazos del archivo o permisos pueden cambiar lo que ves.

No lo uses todavía sobre registros sensibles del sistema. Primero practicaremos con un archivo creado por nosotros.

## 11. No confundas salida con contenido almacenado

Cuando ejecutas:

```bash
cat notas.txt
```

el texto aparece en la terminal.

Eso no significa que el archivo haya sido copiado a otro lugar.

Más adelante aprenderás que la salida estándar puede:

- mostrarse en pantalla;
- enviarse a otro comando;
- redirigirse a un archivo.

Ese será el tema de los Módulos 8 y 9.

## 12. Preparar la práctica

Entra al laboratorio:

```bash
cd ~/linux-lab
pwd
ls -la
```

Si `cd` falla, detente.

Comprueba si existe:

```bash
ls -ld ./modulo-07-lectura
```

Si no existe:

```bash
mkdir modulo-07-lectura
```

Después:

```bash
cd ./modulo-07-lectura
pwd
ls -la
```

No borres una práctica anterior si ya existe.

## 13. Crear un archivo de texto para leer

Todavía no hemos enseñado redirecciones formalmente. Para que el módulo sea autocontenido, usaremos una sola vez `printf` con `>` como herramienta controlada para generar texto dentro del laboratorio.

Primero comprueba que el nombre está libre:

```bash
ls -l lectura.txt
```

Si responde que no existe, crea el archivo:

```bash
printf '%s\n' \
  'línea 1' 'línea 2' 'línea 3' 'línea 4' 'línea 5' 'línea 6' \
  'línea 7' 'línea 8' 'línea 9' 'línea 10' 'línea 11' 'línea 12' \
  > lectura.txt
```

**Importante:** esta orden utiliza una redirección `>`, tema que todavía no se ha explicado formalmente. Aquí se usa solo para preparar el archivo de práctica. No la copies para trabajar con archivos importantes. En el Módulo 8 aprenderás exactamente qué hace y por qué puede sobrescribir.

Después comprueba:

```bash
ls -l lectura.txt
```

No necesitas interpretar todavía todos los campos de `ls -l`.

## 14. Leer con cat

Ejecuta:

```bash
cat lectura.txt
```

Debes ver las doce líneas.

Pregunta:

> ¿`cat` cambió el archivo?

Respuesta esperada: no, en esta práctica solo lo mostró.

## 15. Leer con head

Ejecuta:

```bash
head lectura.txt
```

Después:

```bash
head -n 3 lectura.txt
```

Compara ambas salidas.

Debes poder explicar:
- cuántas líneas muestra la primera por defecto;
- cuántas solicitaste explícitamente en la segunda.

## 16. Leer con tail

Ejecuta:

```bash
tail lectura.txt
```

Después:

```bash
tail -n 3 lectura.txt
```

Compara con `head -n 3`.

**Pregunta:** ¿por qué las líneas son diferentes si ambos reciben el mismo número 3?

## 17. Abrir con less

Ejecuta:

```bash
less lectura.txt
```

Dentro de `less`:

1. desplázate;
2. escribe `/línea 10`;
3. pulsa Enter;
4. observa la coincidencia;
5. pulsa `q` para salir.

Si la búsqueda no funciona como esperabas, sal con `q` y vuelve a intentarlo. No cierres la terminal a la fuerza.

## 18. Práctica controlada de tail -f

Primera terminal:

```bash
cd ~/linux-lab/modulo-07-lectura
ls -l seguimiento.txt
```

Si `seguimiento.txt` no existe, créalo antes de seguirlo:

```bash
touch seguimiento.txt
```

Después, en la misma terminal:

```bash
tail -f seguimiento.txt
```

En una segunda terminal, entra a la misma carpeta y añade una línea con:

```bash
printf 'evento de prueba\n' >> seguimiento.txt
```

La primera terminal debería mostrar la nueva línea.

**Nota:** `>>` también es una redirección y se explicará formalmente en el Módulo 8. Aquí se utiliza solo para demostrar el comportamiento de `tail -f`.

Termina `tail -f` con:

```text
Ctrl + C
```

No cierres el proceso con señales fuertes. La interrupción normal es suficiente.

## 19. Archivos binarios y texto ilegible

No todos los archivos están pensados para mostrarse con `cat` o `less`.

Un ejecutable, imagen o archivo comprimido puede contener bytes que no representan texto legible.

**Regla:** antes de mostrar un archivo desconocido, no asumas que es texto.

Más adelante aprenderás herramientas para identificar tipos de archivo.

En esta práctica solo usamos archivos de texto creados por nosotros.

## 20. Privacidad al leer archivos

Antes de compartir una salida, revisa si contiene:

- nombres de usuario;
- rutas personales;
- nombres de host;
- direcciones IP;
- tokens;
- contraseñas;
- cookies;
- claves;
- datos personales;
- contenido privado de aplicaciones.

No copies archivos completos del sistema al chat “para que los revise” sin inspeccionarlos primero.

Cuando necesites ayuda, comparte el fragmento mínimo relevante y oculta datos sensibles.

## 21. Errores frecuentes

| Situación | Qué ocurrió | Corrección |
|---|---|---|
| `cat` llena la terminal con muchas líneas | Archivo demasiado largo para una lectura cómoda | Usa `less` o selecciona una parte con `head`/`tail` |
| No sabes salir de `less` | Estás dentro del paginador | Pulsa `q` |
| `head -n 5` muestra menos de 5 líneas | El archivo tiene menos contenido | No es un error |
| `tail -f` parece “quedarse detenido” | Está esperando contenido nuevo | Usa `Ctrl+C` cuando termines |
| “Permission denied” | No tienes acceso | No añadas `sudo`; revisa si realmente necesitas ese archivo |
| Pegaste un log completo | Puede contener información privada | Comparte solo el fragmento necesario |
| Usas `cat` sobre un archivo binario | No era texto legible | Detente y usa herramientas apropiadas más adelante |

## 22. Práctica independiente

Dentro de una nueva carpeta de práctica:

1. crea un archivo de al menos 15 líneas;
2. muestra el archivo completo;
3. muestra solo las primeras 4 líneas;
4. muestra solo las últimas 4;
5. ábrelo con un paginador;
6. busca una palabra dentro del paginador;
7. sal correctamente;
8. explica qué herramienta elegirías si el archivo tuviera 20 000 líneas.

No copies la secuencia guiada. Escribe las órdenes basándote en lo aprendido.

## 23. Mini evaluación

1. ¿Qué herramienta es apropiada para mostrar rápidamente un archivo pequeño?
   - A) `cat`
   - B) `mkdir`
   - C) `rm`
   - D) `chmod`

2. ¿Qué herramienta permite navegar por un archivo largo de forma interactiva?
   - A) `tail`
   - B) `less`
   - C) `touch`
   - D) `mv`

3. ¿Qué muestra `head -n 3 archivo.txt`?
   - A) Las últimas tres líneas.
   - B) Las primeras tres líneas.
   - C) Tres archivos.
   - D) Tres directorios.

4. ¿Qué muestra `tail -n 3 archivo.txt`?
   - A) Las últimas tres líneas.
   - B) Las primeras tres.
   - C) Los permisos.
   - D) El propietario.

5. ¿Cómo sales normalmente de `less`?
   - A) `q`
   - B) `rm`
   - C) `sudo`
   - D) `exit --force`

6. ¿Cómo terminas normalmente una ejecución interactiva de `tail -f` en primer plano?
   - A) `Ctrl+C`
   - B) `rm -rf`
   - C) Reiniciando el equipo.
   - D) Borrando el archivo.

7. ¿Debes pegar un archivo completo del sistema al chat sin revisar su contenido?
   - A) Sí.
   - B) No.

## 24. Registro de aprendizaje

Puedes responder:

```text
cat sirve para:
less sirve para:
head sirve para:
tail sirve para:
Para salir de less uso:
Para detener tail -f normalmente uso:
Si un archivo es muy largo elegiría:
Un error que ya sé reconocer:
Algo que todavía confundo:
Estado: EN APRENDIZAJE / PRACTICADO
```

Una ejecución correcta no basta para marcar el tema como dominado. En otra sesión debes elegir la herramienta adecuada sin que se te indique cuál usar.

## 25. Fuentes y límites

Clasificación y estado de los enlaces de esta sección: [catálogo de fuentes](06-catalogo-fuentes.md) (jerarquía E04, comprobación del 9 de octubre de 2026).

Fuentes principales:

- GNU Coreutils — `cat`: https://www.gnu.org/software/coreutils/manual/html_node/cat-invocation.html
- GNU Coreutils — `head`: https://www.gnu.org/software/coreutils/manual/html_node/head-invocation.html
- GNU Coreutils — `tail`: https://www.gnu.org/software/coreutils/manual/html_node/tail-invocation.html
- Documentación de `less`: https://www.greenwoodsoftware.com/less/

Esta lección usa las funciones básicas necesarias para principiantes. No cubre todavía:
- numeración avanzada;
- seguimiento por nombre frente a descriptor;
- rotación de logs;
- combinaciones de `tail` con múltiples archivos;
- opciones avanzadas de `less`;
- lectura de archivos binarios.

**Estado de la lección:** redactada y revisada documentalmente. La práctica real del estudiante sigue pendiente.

---

**Siguiente:** [Módulo 8 — stdin, stdout, stderr y redirecciones](modulo-08-stdin-stdout-stderr-redirecciones.md) · [Volver al índice](README.md)
