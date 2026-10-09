# Módulo 22 — vi/Vim: edición segura de archivos de texto

Manual Maestro de Linux y Shell Scripting — Edición 2026 · v3 · Vigesimosegunda entrega.

[Índice del manual](README.md) · [← Módulo 21](modulo-21-firewall-nftables-ufw-firewalld.md) · [Arquitectura](00-indice-arquitectura.md) · [Módulo 23 →](modulo-23-primer-script-bash-shebang.md)

## 1. Qué aprenderás

Al terminar este módulo podrás:

- explicar qué son `vi` y Vim;
- distinguir modo normal, inserción y línea de comandos;
- abrir un archivo de práctica;
- desplazarte sin modificar contenido;
- insertar texto;
- guardar cambios;
- salir con y sin guardar;
- deshacer y rehacer;
- buscar texto;
- copiar, pegar y borrar líneas de forma controlada;
- activar números de línea;
- reconocer comandos que descartan cambios;
- evitar editar archivos del sistema con privilegios innecesarios.

Conocimientos previos:
- terminal;
- rutas;
- archivos;
- permisos;
- `cat`, `less`, `head`, `tail`;
- redirecciones.

**Seguridad:** toda la práctica se realiza dentro de `~/linux-lab/modulo-22-vim`. No editaremos `/etc`, `/usr`, `/var` ni otros archivos del sistema. No usaremos `sudo vi` o `sudo vim`. Algunos comandos de Vim pueden borrar texto o descartar cambios; se explican antes de usarlos.

## 2. vi y Vim

`vi` es un editor clásico de Unix.

Vim significa:

```text
Vi IMproved
```

Vim amplía el comportamiento tradicional de vi con muchas funciones adicionales.

En algunos sistemas:

```text
vi
```

puede ser Vim ejecutándose en modo compatible, otro editor compatible con vi o una implementación distinta.

Por eso primero consulta:

```bash
command -v vi
command -v vim
```

Si `vim` no existe pero `vi` sí, puedes practicar con `vi`.

**Nota para instalaciones mínimas (`vim.tiny`):** en Debian y derivados, `vi` puede apuntar a una compilación reducida de Vim. Consulta `readlink -f "$(command -v vi)"` si `readlink` está disponible, y `vi --version` si la implementación lo admite. Algunas funciones avanzadas de Vim pueden faltar. Para desplazarte de forma portable en modo normal usa `h`, `j`, `k`, `l`; no asumas que las flechas se comportan igual en todos los modos.

## 3. Un editor modal

Vim es un editor **modal**.

Eso significa que las teclas hacen cosas distintas según el modo actual.

Tres modos fundamentales:

```text
NORMAL
INSERT
COMMAND-LINE
```

No escribas texto hasta entender en qué modo estás.

## 4. Modo normal

Es el modo principal para:

- moverte;
- borrar;
- copiar;
- pegar;
- deshacer;
- buscar;
- ejecutar comandos de edición.

Cuando abres Vim normalmente comienzas en modo normal.

Para volver a modo normal desde inserción:

```text
Esc
```

Esta es una de las teclas más importantes del módulo.

## 5. Modo inserción

En modo inserción, lo que escribes se introduce como texto.

Una forma básica de entrar:

```text
i
```

`i` significa insertar antes de la posición actual.

Para salir del modo inserción:

```text
Esc
```

Secuencia básica:

```text
i
escribir texto
Esc
```

## 6. Línea de comandos

Desde modo normal, pulsa:

```text
:
```

para entrar en la línea de comandos de Vim.

Ahí se utilizan órdenes como:

```text
:w
:q
:wq
:q!
```

Después pulsas Enter.

## 7. Preparar el laboratorio

Entra a:

```bash
cd ~/linux-lab
pwd
```

Comprueba:

```bash
ls -ld ./modulo-22-vim
```

Si no existe:

```bash
mkdir modulo-22-vim
```

Después:

```bash
cd modulo-22-vim
pwd
ls -la
```

## 8. Crear un archivo de práctica

Comprueba primero que el nombre no exista:

```bash
ls -l practica.txt
```

Si no existe, créalo:

```bash
touch practica.txt
```

Después abre:

```bash
vim practica.txt
```

o, si Vim no está disponible:

```bash
vi practica.txt
```

## 9. Primera inserción

Dentro de Vim:

1. pulsa `i`;
2. escribe:

```text
Primera línea de práctica.
Segunda línea de práctica.
```

3. pulsa `Esc`.

Ahora estás de nuevo en modo normal.

## 10. Guardar con :w

Desde modo normal:

```text
:w
```

y Enter.

`w` significa **write**.

Guarda los cambios en el archivo actual.

**Importante:** guardar modifica el archivo en disco.

Por eso solo practicamos con archivos creados expresamente para el laboratorio.

## 11. Salir con :q

Si no tienes cambios pendientes:

```text
:q
```

y Enter.

`q` significa **quit**.

Si existen cambios sin guardar, Vim normalmente impedirá salir y mostrará una advertencia.

Eso es una protección útil.

## 12. Guardar y salir con :wq

```text
:wq
```

guarda y sale.

Equivale conceptualmente a:

```text
:w
:q
```

en una sola orden.

## 13. :q! descarta cambios

Este comando necesita una advertencia explícita:

```text
:q!
```

sale descartando cambios no guardados.

El:

```text
!
```

fuerza la acción en este contexto.

**Riesgo:** puedes perder trabajo no guardado.

No uses `:q!` por costumbre.

Úsalo solo cuando estés seguro de que deseas abandonar los cambios.

## 14. :x

```text
:x
```

guarda si existen cambios y luego sale.

No es exactamente idéntico internamente a `:wq` en todas las situaciones, aunque para un principiante suelen parecer equivalentes.

Por claridad inicial usaremos principalmente:

```text
:w
:q
:wq
```

## 15. Movimiento básico

En modo normal:

```text
h → izquierda
j → abajo
k → arriba
l → derecha
```

También pueden funcionar las flechas según la terminal/editor.

Aprender `h j k l` es útil porque funciona dentro del modelo clásico de vi.

## 16. Movimiento por palabras

En modo normal:

```text
w → siguiente palabra
b → palabra anterior
e → final de palabra
```

No necesitas memorizar todos los movimientos hoy.

Primero domina:

```text
h j k l
w b
```

## 17. Inicio y final de línea

```text
0 → inicio físico de línea
^ → primer carácter no blanco
$ → final de línea
```

No confundas:

```text
0
```

con la letra O mayúscula.

## 18. Ir a una línea

Ejemplo:

```text
10G
```

va a la línea 10.

```text
G
```

va al final del archivo.

```text
gg
```

en Vim suele ir al principio.

## 19. Añadir texto con a

En modo normal:

```text
a
```

entra en inserción **después** del carácter actual.

Comparación:

```text
i → insertar antes
a → insertar después
```

Después recuerda:

```text
Esc
```

## 20. Nueva línea con o

En modo normal:

```text
o
```

crea una nueva línea debajo y entra en inserción.

```text
O
```

crea una nueva línea arriba.

Distingue mayúsculas y minúsculas.

## 21. Deshacer con u

En modo normal:

```text
u
```

deshace el último cambio.

Si borraste o modificaste algo accidentalmente, detente y prueba:

```text
u
```

antes de seguir haciendo cambios.

## 22. Rehacer con Ctrl+r

En modo normal:

```text
Ctrl+r
```

rehace un cambio que habías deshecho.

Práctica:

1. modifica una palabra;
2. pulsa `Esc`;
3. pulsa `u`;
4. pulsa `Ctrl+r`.

Observa el cambio.

**Compatibilidad de vi:** en sistemas mínimos, `vi` puede ser una variante reducida o funcionar en modo compatible. Si las flechas insertan caracteres inesperados, vuelve al modo normal con `Esc` y utiliza `h`, `j`, `k`, `l`. Consulta `vi --version` cuando esté disponible; si existe `vim`, puede ofrecer un comportamiento más predecible para las funciones avanzadas. En algunos modos compatibles, pulsar `u` repetidamente alterna deshacer y rehacer, y `Ctrl+r` puede no comportarse como en Vim. Verifica el editor instalado antes de seguir el ejercicio.

## 23. Borrar un carácter con x

En modo normal:

```text
x
```

borra el carácter bajo el cursor.

**Riesgo:** modifica el contenido.

Si lo haces por accidente:

```text
u
```

para deshacer.

## 24. Borrar una línea con dd

```text
dd
```

borra la línea actual.

Esto es una operación destructiva sobre el contenido del buffer.

Antes de practicarla:

- usa solo `practica.txt`;
- asegúrate de poder deshacer;
- no guardes si borraste algo que querías conservar.

Puedes recuperar inmediatamente con:

```text
u
```

## 25. Copiar una línea con yy

En modo normal:

```text
yy
```

copia o “yank” la línea actual al registro correspondiente.

No modifica el texto por sí mismo.

## 26. Pegar con p

Después de `yy`:

```text
p
```

pega después de la posición/línea actual según el contenido copiado.

Secuencia:

```text
yy
p
```

duplica una línea en un caso sencillo.

## 27. dd también coloca texto en un registro

Cuando haces:

```text
dd
```

la línea borrada normalmente queda disponible para pegar.

Por eso:

```text
dd
p
```

puede mover una línea.

No necesitas estudiar registros de Vim en profundidad todavía.

## 28. Buscar con /

En modo normal:

```text
/palabra
```

y Enter.

Busca hacia adelante.

Para repetir la búsqueda:

```text
n
```

Para repetir en dirección contraria:

```text
N
```

La búsqueda no modifica el archivo.

## 29. Buscar hacia atrás con ?

```text
?palabra
```

busca hacia atrás.

No necesitas dominar ambas direcciones inmediatamente; `/` y `n` son suficientes al principio.

## 30. Números de línea

Desde modo normal:

```text
:set number
```

activa números de línea.

Para desactivarlos:

```text
:set nonumber
```

Esto cambia la visualización de la sesión actual, no el contenido del archivo.

## 31. Mostrar el número actual

```text
Ctrl+g
```

puede mostrar información como nombre de archivo y posición.

También puedes usar:

```text
:set ruler
```

según configuración.

## 32. Reemplazar un carácter con r

En modo normal:

```text
rX
```

reemplaza el carácter actual por `X`.

No entra permanentemente en modo inserción.

Práctica solo sobre texto desechable.

## 33. Cambiar una palabra con cw

```text
cw
```

cambia desde la posición actual hasta el final de la palabra según las reglas de movimiento.

Después entras en inserción.

Secuencia:

```text
cw
nuevo texto
Esc
```

Si todavía resulta confuso, usa `i` y edición simple.

## 34. Visual mode

Vim tiene modo visual.

Una forma de entrar:

```text
v
```

Permite seleccionar texto visualmente.

No es esencial para dominar vi básico, así que solo lo introducimos.

Pulsa:

```text
Esc
```

para salir de la selección.

## 35. Guardar con otro nombre

Desde Vim:

```text
:w copia.txt
```

guarda el buffer en otro archivo.

**Riesgo:** puede crear o sobrescribir un archivo según el contexto y opciones.

En este módulo solo úsalo con un nombre nuevo dentro de `~/linux-lab/modulo-22-vim`.

Antes verifica desde otra terminal si el nombre está libre, o usa un nombre claramente nuevo.

## 36. Abrir archivo de solo lectura

Si solo quieres inspeccionar:

```bash
view archivo.txt
```

cuando `view` está disponible, suele abrir Vim en modo de solo lectura.

Otra posibilidad:

```bash
vim -R archivo.txt
```

No garantiza protección absoluta contra todas las formas de forzar escritura, pero ayuda a evitar modificaciones accidentales.

Para lectura simple sigue siendo válido usar:

```bash
less archivo.txt
```

## 37. No usar Vim para todo

Herramienta según tarea:

```text
cat   → archivo pequeño, salida completa
less  → lectura navegable
head  → principio
tail  → final
vim   → edición interactiva
```

No abras un archivo enorme en un editor solo para consultar dos líneas si otra herramienta es más apropiada.

## 38. Archivos swap

Vim puede crear archivos temporales/swap para ayudar a recuperar sesiones.

Si al abrir un archivo aparece una advertencia de swap, no elijas opciones al azar.

Puede significar:

- otra sesión está editando el archivo;
- la sesión anterior terminó de forma inesperada;
- existe una recuperación pendiente;
- el swap es antiguo.

Primero lee la advertencia y verifica si otra sesión está abierta.

## 39. No borrar un swap sin revisar

Eliminar un archivo swap a ciegas puede hacerte perder una oportunidad de recuperación.

Primero identifica:

- archivo original;
- fecha;
- proceso;
- otra sesión;
- si existen cambios recuperables.

La recuperación avanzada se pospone.

## 40. vimtutor

Si está instalado:

```bash
command -v vimtutor
```

puedes ejecutar:

```bash
vimtutor
```

Es un tutorial interactivo de Vim.

No es obligatorio.

Si no existe, no instales paquetes solo para esta práctica.

## 41. Editar archivos del sistema

Una instrucción como:

```text
sudo vim /etc/archivo
```

combina:

- editor poderoso;
- privilegios elevados;
- archivo de configuración del sistema.

Un error puede afectar servicios o arranque.

Por eso no se practica en este módulo.

Primero aprenderás:

- copia de seguridad;
- validación de sintaxis;
- overrides;
- cambios mínimos;
- rollback.

## 42. No usar :w! a ciegas

```text
:w!
```

intenta forzar una escritura en determinados contextos.

No debe convertirse en respuesta automática a:

```text
E45
E212
readonly
permission denied
```

Primero pregunta:

> ¿debo realmente escribir en este archivo?

Un error de permisos puede ser una protección correcta.

## 43. No usar :q! por frustración

Si Vim no te deja salir porque hay cambios:

1. pulsa `Esc`;
2. decide si quieres conservarlos;
3. si sí: `:wq`;
4. si no: `:q!`.

No memorices solo `:q!`.

## 44. Práctica A — abrir, insertar y guardar

```bash
vim practica.txt
```

Dentro:

```text
i
Linux y Vim.
Esc
:w
:q
```

Después verifica:

```bash
cat practica.txt
```

## 45. Práctica B — movimiento

Abre de nuevo:

```bash
vim practica.txt
```

Practica únicamente en modo normal:

```text
h j k l
w b
0 $
```

No cambies texto.

Sal:

```text
:q
```

## 46. Práctica C — deshacer

Dentro del archivo de práctica:

1. pulsa `i`;
2. escribe una palabra de prueba;
3. pulsa `Esc`;
4. pulsa `u`.

Comprueba que el cambio se deshace.

No guardes hasta verificar.

## 47. Práctica D — rehacer

Después de deshacer:

```text
Ctrl+r
```

Comprueba que el cambio reaparece.

Después decide si deseas conservarlo.

## 48. Práctica E — copiar y pegar

Colócate sobre una línea.

Ejecuta:

```text
yy
p
```

Deberías duplicar la línea.

Después:

```text
u
```

si no quieres conservar el duplicado.

## 49. Práctica F — borrar y recuperar

Sobre una línea desechable:

```text
dd
```

Observa que desaparece.

Inmediatamente:

```text
u
```

para recuperarla.

No guardes entre ambos pasos.

## 50. Práctica G — búsqueda

Añade varias líneas y guarda.

Después:

```text
/Linux
```

Enter.

Repite:

```text
n
```

La búsqueda no modifica el archivo.

## 51. Práctica H — números de línea

```text
:set number
```

Observa.

Después:

```text
:set nonumber
```

No cambia el archivo.

## 52. Práctica I — salir correctamente

Escenario 1: no hiciste cambios.

```text
:q
```

Escenario 2: quieres guardar.

```text
:wq
```

Escenario 3: hiciste cambios que deliberadamente quieres descartar.

```text
:q!
```

Explica antes de usar el tercero qué perderás.

## 53. Errores frecuentes

| Error | Qué ocurrió | Corrección |
|---|---|---|
| Escribes y aparecen comandos extraños | Estás en modo normal | Pulsa `i` para insertar |
| Teclas `hjkl` aparecen como texto | Estás en inserción | Pulsa `Esc` |
| No puedes salir | Hay cambios pendientes o sigues en otro modo | `Esc`, luego decide `:wq` o `:q!` |
| Usas `:q!` por costumbre | Pierdes cambios | Decide antes |
| Borras línea con `dd` | Comando normal de borrado | Usa `u` si fue accidental |
| Guardas archivo incorrecto | No verificaste nombre/ruta | Consulta nombre y `pwd` |
| Abres archivo del sistema con sudo | Riesgo elevado | Practica en linux-lab |
| Usas `:w!` ante error de permisos | Intentas forzar sin diagnosticar | Revisa propiedad/ruta/necesidad |
| Borras swap sin leer aviso | Puedes perder recuperación | Investiga primero |
| Editas cuando solo querías leer | Riesgo innecesario | Usa `less` o `vim -R` |

## 54. Método seguro antes de editar

1. ejecuta `pwd`;
2. confirma el nombre del archivo;
3. comprueba permisos con `ls -l`;
4. decide si necesitas editar o solo leer;
5. si es importante, asegúrate de tener respaldo o control de versiones;
6. abre sin `sudo`;
7. realiza un cambio pequeño;
8. revisa;
9. guarda;
10. valida el resultado.

## 55. Práctica independiente

Dentro de una nueva carpeta del laboratorio:

1. crea un archivo vacío;
2. ábrelo con Vim/vi;
3. inserta tres líneas;
4. guarda;
5. busca una palabra;
6. activa números de línea;
7. duplica una línea con `yy` y `p`;
8. deshaz el duplicado;
9. borra una línea y recupérala;
10. guarda y sal;
11. verifica con `cat`.

No uses `sudo`.

## 56. Mini evaluación

1. ¿en qué modo puedes usar `dd`?
   - A) Normal.
   - B) Inserción.

2. ¿qué tecla suele volver a modo normal?
   - A) Esc.
   - B) Enter.

3. ¿qué hace `:w`?
   - A) Guarda.
   - B) Borra.

4. ¿qué hace `:q`?
   - A) Sale si es posible.
   - B) Guarda siempre.

5. ¿qué hace `:q!`?
   - A) Sale descartando cambios no guardados.
   - B) Crea una copia.

6. ¿qué hace `u` en modo normal?
   - A) Deshacer.
   - B) Guardar.

7. ¿qué hace `yy`?
   - A) Copia una línea.
   - B) La elimina permanentemente.

8. ¿qué hace `dd`?
   - A) Borra/corta una línea.
   - B) Activa números.

9. ¿`:set number` modifica el contenido del archivo?
   - A) Sí.
   - B) No.

10. ¿debes practicar con `sudo vim /etc/... `?
   - A) Sí.
   - B) No.

## 57. Registro de aprendizaje

Puedes responder:

```text
Modo normal sirve para:
Modo inserción sirve para:
Esc sirve para:
i hace:
:w hace:
:q hace:
:wq hace:
:q! hace:
u hace:
Ctrl+r hace:
yy hace:
dd hace:
p hace:
/texto sirve para:
¿Por qué no uso sudo vim para practicar?:
Algo que todavía confundo:
Estado: EN APRENDIZAJE / PRACTICADO
```

## 58. Fuentes y límites

Clasificación y estado de los enlaces de esta sección: [catálogo de fuentes](06-catalogo-fuentes.md) (jerarquía E04, comprobación del 9 de octubre de 2026).

Fuentes principales:

- Vim documentation:
  https://vimhelp.org/
- Vim user manual:
  https://vimhelp.org/usr_toc.txt.html
- Vim reference manual:
  https://vimhelp.org/#reference_toc
- Vim project:
  https://www.vim.org/

Se posponen:

- macros;
- registros avanzados;
- sustituciones complejas;
- regex de Vim;
- buffers;
- ventanas;
- tabs;
- plugins;
- configuración avanzada de `.vimrc`;
- edición de archivos del sistema;
- recuperación avanzada de swap;
- diff;
- scripting de Vim.

**Estado de la lección:** redactada y revisada documentalmente. Las prácticas se limitan a archivos propios del laboratorio.

---

**Siguiente:** [Módulo 23 — Primer script Bash y shebang](modulo-23-primer-script-bash-shebang.md) · [Volver al índice](README.md)
