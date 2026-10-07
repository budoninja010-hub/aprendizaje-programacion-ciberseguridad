# Módulo 4 — Rutas absolutas y relativas; ~, ., .. y nombres con espacios

Manual Maestro de Linux y Shell Scripting — Edición 2026 · v3 · Cuarta entrega.

[Estado actual](README.md) · [Módulo anterior](modulo-03-navegacion-pwd-ls-cd.md) · [Arquitectura](00-indice-arquitectura.md)

## 1. Qué aprenderás

Podrás predecir qué ubicación señala una ruta antes de usarla, distinguir raíz y directorio personal, navegar entre carpetas y conservar como un solo argumento un nombre que contiene espacios.

Antes de empezar, explica para qué sirven `pwd`, `ls` y `cd`. Después indica por qué debes detenerte si falla `cd`. Si necesitas consultar la respuesta, repasa M3; no hace falta memorizar más opciones todavía.

Entorno previsto: Bash sobre Linux, usuario normal y laboratorio `~/linux-lab` preparado. No se supone que tu directorio personal esté necesariamente en `/home/estudiante`.

**Seguridad:** la práctica creará únicamente tres carpetas de ejercicios si sus nombres están disponibles. No borra ni sobrescribe archivos ni modifica permisos. Ejecuta una orden cada vez y revisa su resultado. No uses `sudo` para solucionar errores de esta lección.

## 2. Una ruta indica cómo localizar un objeto

Una ruta es una secuencia de nombres separados por `/`. Puede señalar un archivo o un directorio. La barra separa componentes; no es un carácter que pueda formar parte de un único nombre de archivo en Linux.

Ejemplo conceptual:

```text
/home/estudiante/linux-lab
```

Este ejemplo empieza en la raíz `/`, pasa por `home`, después por `estudiante` y finalmente por `linux-lab`. No lo copies como si fuera tu ruta real.

**Para qué sirve:** muchos comandos necesitan saber qué objeto consultar o modificar. Escribir una ruta no crea automáticamente el objeto que nombra ni demuestra que exista.

**Error típico:** pensar que toda ruta termina en un archivo. La del ejemplo termina en un directorio.

**Ejercicio:** separa los componentes del ejemplo y explica qué representa la primera barra.

## 3. Rutas absolutas: comenzar en la raíz

Una ruta absoluta empieza por `/`. Su interpretación parte de la raíz del entorno de archivos del proceso, no de la carpeta de trabajo actual. [Linux: resolución de rutas](https://man7.org/linux/man-pages/man7/path_resolution.7.html).

Ejemplo de consulta ya visto:

```bash
ls /etc
```

`ls` lista y `/etc` identifica el directorio consultado. Esta orden no te cambia de carpeta ni modifica la configuración de `/etc`. En esta lección no necesitas ejecutarla: sirve para reconocer la forma de una ruta absoluta.

**Error típico:** llamar «absoluta» a una ruta solo porque es larga. La diferencia es dónde empieza a resolverse, no su longitud.

**Ejercicio:** ¿`/tmp` es absoluta? ¿Y `carpeta/subcarpeta/archivo.txt`? Justifica la respuesta sin contar caracteres.

Una ruta absoluta tampoco garantiza seguridad: puede apuntar fuera del laboratorio. En un contenedor o entorno aislado, `/` puede representar una vista distinta de la del sistema anfitrión.

## 4. Rutas relativas: comenzar desde una base

Para las consultas ordinarias de esta lección, una ruta relativa se interpreta desde tu directorio de trabajo. Por eso necesitas conocer primero la salida de `pwd`.

Ejemplo conceptual: si estás en `/home/estudiante`, `linux-lab` se refiere a una carpeta dentro de esa ubicación. Si ya estás en `/home/estudiante/linux-lab`, el mismo texto buscaría otra carpeta llamada `linux-lab` dentro de ella.

```text
Ubicación actual: /home/estudiante
Ruta relativa:   linux-lab
Destino:         /home/estudiante/linux-lab
```

Esto es un razonamiento sobre una estructura sencilla sin enlaces; no una salida de tu equipo.

**Para qué sirve:** permite trabajar con carpetas cercanas sin repetir toda la ruta. **Error típico:** reutilizar una ruta relativa después de cambiar de ubicación y asumir que conserva el destino.

**Ejercicio:** si estás en el laboratorio y escribes `ls apuntes`, ¿en qué carpeta se buscará `apuntes`?

Nota de precisión: Bash puede tener configurada una búsqueda especial para `cd` mediante `CDPATH`. Usaremos `./nombre` cuando queramos dejar explícito que el destino empieza en la carpeta actual. No cambies tu configuración para hacer esta práctica. [GNU Bash: cd](https://www.gnu.org/software/bash/manual/html_node/Bourne-Shell-Builtins.html).

## 5. Punto y doble punto

Dentro de una ruta, `.` representa el directorio actual y `..` el padre. Para este primer recorrido se usan directorios normales sin enlaces simbólicos.

```bash
ls .
```

`ls` consulta y `.` señala la carpeta actual. Es una forma explícita de indicar el lugar que ya se listaba con `ls` sin ruta.

```bash
cd ./apuntes
```

`cd` cambia de carpeta; `./apuntes` empieza en la ubicación actual y busca un directorio llamado `apuntes`. Solo ejecútalo cuando esa carpeta exista en la práctica.

```bash
cd ..
```

En el recorrido normal, sube al padre. No equivale a `cd -`, que vuelve al directorio anterior registrado. Tampoco hay que cambiarlo por tres puntos: `...` no es una abreviatura especial para subir dos niveles.

**Ejercicio:** partiendo de una carpeta `apuntes` que está dentro del laboratorio, explica qué señalarían `.` y `..`.

No simplifiques automáticamente toda ruta como si fuera una suma: con enlaces simbólicos, navegación lógica y física pueden producir diferencias. En M5 se introducirá su interpretación. Si el recorrido real no coincide con lo esperado, pausa y revisa.

## 6. Tilde: el directorio personal

En los ejemplos de Bash, un `~` inicial sin citar se expande al directorio personal. Así, `~/linux-lab` llega a tu laboratorio aunque estés trabajando en otra carpeta.

No confundas estos tres elementos:

| Escritura | Significado en estos ejemplos |
|---|---|
| `/` | Raíz del árbol de archivos |
| `~` | Abreviatura que Bash expande al directorio personal |
| `.` | Directorio de trabajo actual |

`~/linux-lab` es una expresión de la shell: después de su expansión habitual resulta una ruta absoluta. No es una ruta relativa ordinaria por el mero hecho de no empezar visualmente con `/`. Otras aplicaciones no tienen por qué expandir `~`. [GNU Bash: expansión de tilde](https://www.gnu.org/s/bash/manual/html_node/Tilde-Expansion.html).

**Error típico:** escribir `cd "~/linux-lab"` esperando que Bash expanda la tilde. Al estar citada, se conserva literalmente. En nuestros ejemplos se usa `cd ~/linux-lab`.

**Ejercicio:** explica por qué `/`, `~` y `.` pueden señalar lugares diferentes en una misma sesión.

## 7. Nombres con espacios: agrupar un argumento

Un espacio sin proteger separa palabras de la orden. Si un nombre es `mis notas`, debes indicar que sus dos palabras forman un solo argumento.

Ejemplo de consulta, para cuando exista esa carpeta:

```bash
ls "mis notas"
```

- `ls` es la orden.
- `"mis notas"` se transmite como un argumento con un espacio interno.
- Las comillas de agrupación no se convierten en parte del nombre.

Para este nombre literal sencillo también sirve `ls 'mis notas'`. Las comillas simples y dobles no son equivalentes en todos los contextos: las dobles permiten ciertas expansiones que las simples impiden. Hoy usa nombres literales sencillos; la regla completa se estudiará en M24. [GNU Bash: comillas](https://www.gnu.org/software/bash/manual/html_node/Quoting.html) y [comillas dobles](https://www.gnu.org/s/bash/manual/html_node/Double-Quotes.html).

### Combinar tilde y espacios

```bash
ls ~/linux-lab/modulo-04-rutas/"mis notas"
```

La tilde inicial queda sin citar y se expande. El segmento con espacios queda entre comillas. Como no hay separadores sin proteger entre los segmentos, Bash construye un único argumento de ruta.

**Error típico:** `ls mis notas` consulta dos nombres, `mis` y `notas`; no equivale al nombre `mis notas`. Que la orden no falle no demuestra que haya consultado el destino que querías.

**Ejercicio:** explica cuántos argumentos de ruta recibe `ls` en cada una de las dos escrituras anteriores. No necesitas ejecutar el ejemplo incorrecto.

## 8. Preparación guiada del recorrido

Esta sección crea carpetas; lee el efecto antes de ejecutar. No se crearán archivos dentro de ellas. Si un nombre ya está ocupado, no elimines ni renombres lo existente para continuar.

### Paso A. Entrar y comprobar

Ejecuta una línea cada vez:

```bash
cd ~/linux-lab
pwd
ls -la
```

La primera entra al laboratorio; si falla, detente. La segunda comprueba la ubicación. La tercera permite inspeccionar también entradas ocultas. Reutiliza los conocimientos de M3 y confirma que el laboratorio es el directorio normal previsto.

### Paso B. Crear un directorio nuevo de práctica

Si no aparece una entrada llamada `modulo-04-rutas`, ejecuta:

```bash
mkdir modulo-04-rutas
```

`mkdir`, presentado en M1, crea una carpeta; aquí el nombre es relativo a la ubicación comprobada. No usamos `-p`: si el nombre ya existe, queremos revisar la situación. Un fallo no autoriza a borrar lo que lo ocupa.

Si ya existía, inspecciónalo con `ls -ld ./modulo-04-rutas`. Si no es un directorio normal, pausa. Si lo es, revisa su contenido con `ls -la ./modulo-04-rutas` y conserva todo: puedes reutilizarlo solo después de entender qué contiene.

### Paso C. Entrar y preparar dos destinos

```bash
cd ./modulo-04-rutas
pwd
ls -la
```

Cada línea sirve para entrar, confirmar e inspeccionar. Si los siguientes nombres están disponibles, créalos por separado:

```bash
mkdir apuntes
mkdir "mis notas"
```

La primera crea `apuntes`; la segunda crea una sola carpeta cuyo nombre contiene un espacio. Si alguna ya existe, inspecciónala antes de decidir reutilizarla. Ante enlaces, archivos ordinarios o dudas, detente. No se exige que las carpetas estén vacías.

Árbol esperado, si acabas de crearlas:

```text
linux-lab/
└── modulo-04-rutas/
    ├── apuntes/
    └── mis notas/
```

## 9. Navegación: anticipar el destino

Empieza dentro de `modulo-04-rutas`, comprobado con `pwd`. Realiza una orden por vez; si falla, no continúes.

| Paso | Orden | Qué debes explicar |
|---|---|---|
| 1 | `cd ./apuntes` | Entrar en un hijo del directorio actual |
| 2 | `pwd` | Confirmar el destino real |
| 3 | `ls ..` | Listar el padre sin cambiar de ubicación |
| 4 | `cd ../"mis notas"` | Subir al padre y entrar en el otro directorio |
| 5 | `pwd` | Ver una ruta cuyo nombre final contiene un espacio |
| 6 | `cd .` | Permanecer en la ubicación actual |
| 7 | `pwd` | Comprobar que no se cambió de lugar |
| 8 | `cd ~/linux-lab` | Volver al laboratorio mediante la abreviatura del directorio personal |
| 9 | `pwd` | Confirmar dónde terminó el recorrido |

Ahora compara una ruta relativa y una absoluta al mismo destino. Dentro de `modulo-04-rutas`, `ls ./apuntes` consulta el hijo. Para escribir la alternativa absoluta, toma la ruta real mostrada allí por `pwd`, añade `/apuntes` y encierra **toda esa ruta real** entre comillas dobles si contiene espacios. No uses literalmente la palabra «ruta» ni la dirección ilustrativa de otra persona.

Si no estás seguro de haberla construido bien, muéstrala al tutor con los datos personales sustituidos y deja la consulta pendiente. El propósito es entender el recorrido, no acertar por ensayo y error.

Al terminar, deja las carpetas creadas tal como están. No hay un paso de limpieza con borrado.

## 10. Errores y corrección mínima

| Problema | Causa posible | Corrección |
|---|---|---|
| `cd "~/linux-lab"` no llega al laboratorio | La tilde citada no se expande | Usar la forma del ejemplo con `~` sin citar |
| `cd mis notas` falla | Se han entregado palabras separadas | Agrupar el nombre: `cd "mis notas"`, desde el padre correcto |
| Una ruta relativa encuentra otro destino | Cambió el directorio de trabajo | Consultar `pwd` y reconstruir la ruta |
| Se utilizó `/linux-lab` por `~/linux-lab` | Raíz y directorio personal se confundieron | Revisar el punto de partida; no crear carpetas en `/` |
| `mkdir` informa que existe una entrada | El nombre está ocupado | Inspeccionar y conservar; no borrar para repetir la práctica |
| Aparece «Permission denied» | Falta acceso al destino | Detenerse y revisar ubicación, sin `sudo` ni cambios de permisos |

Un mensaje de error no implica por sí solo que debas reinstalar herramientas. Tampoco una orden exitosa demuestra que la ruta elegida era la correcta: comprueba intención y resultado.

## 11. Práctica independiente y evaluación

Sin copiar la tabla, parte del laboratorio, entra a `apuntes`, consulta el padre y navega a `mis notas`. Regresa al laboratorio y explica qué parte del recorrido fue relativa y cuál utilizó expansión de tilde. Comprueba cada cambio con `pwd`.

Responde después:

1. ¿Qué diferencia fundamental existe entre una ruta absoluta y una relativa?
2. Si estás en `modulo-04-rutas/apuntes`, ¿qué señala `../"mis notas"` en nuestro árbol?
3. ¿Por qué escribir comillas no crea un nombre diferente en el ejemplo correcto?
4. ¿Es `~` una abreviatura del directorio actual o del personal?
5. ¿Por qué no puedes sustituir `cd ..` por `cd -` en todos los casos?
6. ¿Qué harías si el nombre de práctica estuviera ocupado por un archivo?

Pista si te bloqueas: dibuja el árbol, marca dónde estás y recorre los componentes de izquierda a derecha. No se considera dominado por un único intento. En otra sesión repite con un punto de partida diferente, explica el razonamiento y detecta un error por tu cuenta.

## 12. Registro y revisión

Puedes enviar una respuesta breve al chat: qué entendiste de las rutas, un ejemplo explicado, un error reconocido y qué necesitas repetir. No pegues rutas personales o nombres privados sin revisarlos. La ficha del estudiante se conservará cuando exista y haya sido revisada; no se inventan respuestas ni avances.

Revisión documental: sintaxis de ejemplos, separación de argumentos, expansión de tilde, destinos del árbol y coherencia con M1–M3. Las referencias GNU se consultaron mediante documentación oficial indexada; la resolución de rutas se contrastó con Linux man-pages. La práctica en el Linux del estudiante sigue pendiente. No se afirma validación de ejecuciones reales.

Siguiente módulo por redactar: **Módulo 5 — Árbol de archivos y FHS; /etc, /usr, /var, /tmp, /proc, /sys y enlaces**.
