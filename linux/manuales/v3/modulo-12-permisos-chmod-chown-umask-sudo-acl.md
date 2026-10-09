# Módulo 12 — Permisos, propietarios, chmod, chown, umask, sudo y ACL básica

Manual Maestro de Linux y Shell Scripting — Edición 2026 · v3 · Duodécima entrega.

[Índice del manual](README.md) · [← Módulo 11](modulo-11-usuarios-grupos-identidad.md) · [Arquitectura](00-indice-arquitectura.md) · [Módulo 13 →](modulo-13-procesos-ps-top-htop.md)

## 1. Qué aprenderás

Al terminar este módulo podrás:

- interpretar los permisos básicos mostrados por `ls -l`;
- distinguir propietario, grupo y otros;
- explicar qué significan `r`, `w` y `x` en archivos y directorios;
- cambiar permisos de un archivo propio con `chmod`;
- interpretar los modos numéricos básicos como 600, 640, 644, 700, 750 y 755;
- explicar qué hace `chown` y por qué no debe usarse sin necesidad;
- explicar `umask` sin confundirlo con una resta decimal;
- comprender qué problema resuelven las ACL;
- explicar para qué sirve `sudo` y por qué no debe anteponerse automáticamente a una orden que falla.

Conocimientos previos:
- usuarios, UID, grupos y GID;
- `ls -l`;
- creación de archivos y directorios;
- navegación segura en `~/linux-lab`.

**Seguridad:** modificar permisos puede impedir el acceso a archivos o exponerlos a otros usuarios. Todas las prácticas de escritura se realizan solo sobre objetos creados expresamente dentro de `~/linux-lab/modulo-12-permisos`. No cambiamos permisos del sistema. No usamos `sudo chmod`, `sudo chown` ni `chmod -R` en este módulo.

## 2. Leer la primera columna de ls -l

Ejecuta sobre un archivo propio:

```bash
ls -l archivo.txt
```

Una salida ilustrativa podría empezar así:

```text
-rw-r-----
```

Los primeros diez caracteres se interpretan así:

```text
- rw- r-- ---
│ │   │   │
│ │   │   └─ otros
│ │   └───── grupo
│ └───────── propietario
└─────────── tipo de objeto
```

El primer carácter no es un permiso. Indica el tipo de entrada.

Ejemplos frecuentes:

```text
- = archivo ordinario
d = directorio
l = enlace simbólico
```

Los nueve caracteres restantes se dividen en tres grupos de tres.

## 3. Las tres clases de permisos

Las tres clases básicas son:

```text
u = user  = propietario
g = group = grupo
o = others = otros
```

También existe:

```text
a = all
```

que se refiere a todas las clases cuando se usa en expresiones simbólicas de `chmod`.

No confundas:

- **propietario** con “cualquier usuario”;
- **grupo** con todos los grupos del usuario;
- **otros** con un grupo llamado `others`.

## 4. r, w y x en un archivo

Para un archivo ordinario:

```text
r = read    = leer contenido
w = write   = modificar contenido
x = execute = intentar ejecutarlo como programa/script
```

Ejemplo:

```text
rw-
```

significa lectura y escritura, sin ejecución.

**Importante:** tener `x` no garantiza que el contenido sea un programa válido. Solo es una condición de permisos para determinadas formas de ejecución.

## 5. r, w y x en un directorio

En un directorio, las letras tienen efectos distintos:

- `r`: permite leer/listar nombres de entradas, sujeto a otras condiciones;
- `w`: permite modificar entradas del directorio, como crear, borrar o renombrar, sujeto a otras reglas;
- `x`: permite atravesar el directorio y acceder a entradas conocidas, si los demás permisos lo permiten.

Por eso:

> El significado práctico de `x` depende de si el objeto es un archivo o un directorio.

No estudiaremos todavía todos los casos con sticky bit, ACL, montajes y políticas adicionales.

## 6. Propietario y grupo

Una salida larga puede verse conceptualmente así:

```text
-rw-r----- 1 alumno proyecto ... informe.txt
```

Aquí:

- `alumno` sería el propietario;
- `proyecto` sería el grupo asociado.

Los nombres son ilustrativos.

Para consultar un archivo real propio:

```bash
ls -l archivo.txt
```

No necesitas cambiar propietario para aprender a leer esta información.

## 7. chmod — cambiar bits de modo

`chmod` cambia permisos o, más precisamente, bits del modo del archivo según las reglas y opciones aplicables.

Hay dos formas principales que aprenderemos:

1. simbólica;
2. numérica u octal.

Primero usaremos la simbólica porque muestra con claridad qué clase cambia.

Referencia principal: GNU Coreutils — `chmod`.

## 8. chmod simbólico

Ejemplo:

```bash
chmod u+x script.sh
```

Se lee:

- `u`: propietario;
- `+`: añadir;
- `x`: permiso de ejecución.

Otro ejemplo:

```bash
chmod g-w archivo.txt
```

Se lee:

- grupo;
- quitar;
- escritura.

Y:

```bash
chmod o-r archivo.txt
```

quita lectura a otros.

## 9. Operadores +, - y =

En modo simbólico:

```text
+ = añadir permisos indicados
- = quitar permisos indicados
= = establecer exactamente los permisos indicados para esa clase
```

Ejemplo:

```bash
chmod u=rw archivo.txt
```

establece para el propietario lectura y escritura, sin ejecución.

**Cuidado:** `=` reemplaza los permisos de esa clase por los indicados.

## 10. Notación numérica: r=4, w=2, x=1

Cada clase puede representarse mediante la suma de:

```text
r = 4
w = 2
x = 1
```

Ejemplos:

```text
7 = 4 + 2 + 1 = rwx
6 = 4 + 2     = rw-
5 = 4 + 1     = r-x
4 = 4         = r--
0 = 0         = ---
```

Tres dígitos representan:

```text
propietario | grupo | otros
```

## 11. Modos numéricos frecuentes

Ejemplos:

```text
600 = rw------- 
640 = rw-r-----
644 = rw-r--r--
700 = rwx------
750 = rwxr-x---
755 = rwxr-xr-x
```

No memorices números sin traducirlos a letras.

### Ejemplo

```bash
chmod 640 informe.txt
```

significa:

- propietario: `rw-`;
- grupo: `r--`;
- otros: `---`.

## 12. Por qué no usamos chmod 777 como solución universal

```text
777 = rwxrwxrwx
```

Concede lectura, escritura y ejecución a propietario, grupo y otros.

Eso suele ser **mucho más acceso del necesario**.

Usar `chmod 777` para “hacer que funcione” puede ocultar el problema real y ampliar innecesariamente el acceso.

**Regla:** aplica el mínimo permiso necesario.

## 13. chmod recursivo aumenta el alcance

Una opción como:

```text
chmod -R ...
```

puede cambiar permisos de un árbol completo.

No se practica en este módulo.

Un error en la ruta podría afectar muchos archivos y directorios.

Aprende primero a modificar un solo objeto creado expresamente para la práctica.

## 14. chown — cambiar propietario y/o grupo

`chown` puede cambiar el propietario y, según la sintaxis, el grupo.

Ejemplo conceptual:

```text
chown usuario archivo
chown usuario:grupo archivo
```

Cambiar propietario normalmente requiere privilegios adecuados.

**En este módulo no ejecutaremos `chown`**.

¿Por qué?

- no necesitamos cambiar propietario para aprender permisos;
- un cambio equivocado puede dejar archivos inaccesibles para la cuenta esperada;
- practicarlo con `sudo` enseñaría a elevar privilegios antes de comprender el impacto.

Referencia: GNU Coreutils — `chown`.

## 15. chgrp

Existe también `chgrp` para cambiar el grupo de un archivo.

Un usuario puede tener ciertas posibilidades de cambio de grupo según sus pertenencias y las reglas del sistema.

No lo practicaremos todavía.

Primero aprenderemos a interpretar correctamente propietario, grupo y permisos.

## 16. umask — máscara de creación

`umask` influye en los permisos iniciales que reciben nuevos archivos y directorios.

Consulta:

```bash
umask
```

Puede mostrar, por ejemplo:

```text
0022
```

Tu valor puede ser diferente.

### Regla importante

No enseñaremos `umask` como una simple “resta decimal”.

El modelo correcto es:

> una máscara **elimina bits de permisos** del conjunto que la aplicación solicita al crear el objeto.

Para muchas demostraciones sencillas se parte conceptualmente de:

```text
archivos:     0666
directorios:  0777
```

y se eliminan los bits marcados por la máscara.

Pero una aplicación puede solicitar modos diferentes, y otras reglas también pueden influir.

## 17. Ejemplo conceptual de umask 022

Si una aplicación solicita para un archivo:

```text
0666 = rw-rw-rw-
```

y la máscara es:

```text
0022
```

se eliminan escritura de grupo y escritura de otros:

```text
0644 = rw-r--r--
```

Para un directorio solicitado con:

```text
0777
```

la misma máscara suele producir:

```text
0755 = rwxr-xr-x
```

No es “666 menos 22” como aritmética decimal.

## 18. Demostración segura de umask sin cambiar tu sesión principal

Cambiar `umask` afecta a la shell y a procesos descendientes. Para no alterar la configuración de tu sesión principal, usaremos una **subshell temporal**.

No necesitas dominar todavía la sintaxis de paréntesis; se estudiará más adelante.

Dentro de una carpeta de práctica vacía y verificada:

```bash
( umask 027; touch prueba-umask.txt; mkdir prueba-umask-dir; ls -ld prueba-umask.txt prueba-umask-dir )
```

Todo lo que está entre paréntesis se ejecuta en una subshell.

Al terminar, el `umask 027` de esa subshell desaparece con ella; tu shell principal conserva su valor anterior.

La práctica crea dos objetos dentro del laboratorio, pero no cambia permisos del sistema.

## 19. Interpretar umask 027

Conceptualmente:

```text
0 = no enmascarar bits del propietario
2 = quitar escritura al grupo
7 = quitar lectura, escritura y ejecución a otros
```

Para un archivo solicitado con 0666:

```text
0666
máscara 0027
→ típicamente 0640
```

Para un directorio solicitado con 0777:

```text
0777
máscara 0027
→ típicamente 0750
```

Después comprueba con `ls -ld`.

## 20. sudo — ejecutar una orden según una política de privilegios

`sudo` permite ejecutar órdenes como otro usuario según la configuración de seguridad.

En muchos sistemas se utiliza para tareas administrativas autorizadas.

No significa:

```text
“si falla, añade sudo”
```

### Antes de sudo, pregunta

1. ¿la tarea realmente requiere privilegios?
2. ¿estoy usando la ruta correcta?
3. ¿entiendo qué modificará?
4. ¿existe una alternativa sin privilegios?
5. ¿puedo revertir el cambio?

En este módulo no se ejecutan cambios administrativos mediante `sudo`.

## 21. sudo no corrige permisos mal entendidos

Si:

```bash
cat archivo.txt
```

falla por permisos, no debes concluir automáticamente:

```text
sudo cat archivo.txt
```

Primero determina si tienes derecho y necesidad de leer ese archivo.

Un error de permisos puede ser una protección correcta, no un problema que debas eliminar.

## 22. ACL — listas de control de acceso

Los permisos tradicionales tienen tres clases:

```text
propietario
grupo
otros
```

A veces eso no basta.

Una **ACL** puede permitir reglas más específicas, por ejemplo permisos para usuarios o grupos adicionales.

Conceptualmente:

```text
permisos tradicionales
+
entradas ACL adicionales
```

En Linux, herramientas comunes son:

```text
getfacl
setfacl
```

Su disponibilidad depende del sistema y paquetes instalados.

## 23. getfacl — inspección

Comprueba primero:

```bash
command -v getfacl
```

Si existe, sobre un archivo propio:

```bash
getfacl archivo.txt
```

Puede mostrar:

- propietario;
- grupo;
- entradas de usuario;
- entradas de grupo;
- máscara ACL;
- otros.

No necesitas memorizar todas las líneas todavía.

Si `getfacl` no está disponible, no instales nada para completar esta lección.

## 24. setfacl — modificación, solo concepto por ahora

`setfacl` modifica ACL.

Puede añadir o quitar permisos específicos.

**No ejecutaremos `setfacl` en esta lección** porque una entrada incorrecta puede cambiar el acceso de otros usuarios y porque todavía no hemos estudiado la máscara ACL con suficiente profundidad.

Primero aprendemos a inspeccionar.

## 25. La máscara ACL no es umask

No confundas:

- **umask**: influye en permisos iniciales al crear objetos;
- **mask de una ACL**: limita los permisos efectivos de determinadas entradas ACL.

Tienen nombres parecidos pero funciones diferentes.

## 26. El signo + en ls -l

En sistemas con soporte de ACL, `ls -l` puede mostrar un indicador adicional, por ejemplo:

```text
-rw-r-----+
```

El `+` puede indicar que existen datos de ACL extendidos.

No asumas que su ausencia o presencia se comporta exactamente igual en todos los sistemas y herramientas.

Si aparece, puedes investigar con `getfacl`.

## 27. Permisos no son toda la seguridad

Aunque un archivo muestre ciertos bits, el acceso efectivo también puede depender de:

- ACL;
- permisos de los directorios del camino;
- identidad efectiva;
- capacidades;
- políticas MAC como SELinux o AppArmor;
- sistema de archivos;
- montajes;
- atributos adicionales.

No necesitas dominar todo eso hoy.

La lección correcta es:

> `rwx` es fundamental, pero no representa por sí solo todo el modelo de seguridad de Linux.

## 28. Preparar la práctica

Entra al laboratorio:

```bash
cd ~/linux-lab
pwd
ls -la
```

Comprueba:

```bash
ls -ld ./modulo-12-permisos
```

Si no existe:

```bash
mkdir modulo-12-permisos
```

Después:

```bash
cd ./modulo-12-permisos
pwd
ls -la
```

No reutilices nombres sin inspeccionarlos.

## 29. Crear objetos de práctica

Si los nombres están libres:

```bash
touch privado.txt
touch compartido.txt
mkdir carpeta-privada
```

Comprueba:

```bash
ls -ld privado.txt compartido.txt carpeta-privada
```

Anota los permisos iniciales. Pueden variar según tu `umask`.

## 30. Práctica A — chmod simbólico

Primero:

```bash
chmod u=rw,g=,o= privado.txt
```

Esto intenta dejar:

```text
rw-------
```

Comprueba:

```bash
ls -l privado.txt
```

Explica:

- propietario: lectura y escritura;
- grupo: sin permisos;
- otros: sin permisos.

## 31. Práctica B — añadir lectura al grupo

Ejecuta:

```bash
chmod g+r privado.txt
```

Comprueba:

```bash
ls -l privado.txt
```

Ahora deberías poder reconocer:

```text
rw-r-----
```

si no hay otros factores que alteren la presentación.

Después quita de nuevo la lectura:

```bash
chmod g-r privado.txt
```

## 32. Práctica C — modo numérico

Sobre `compartido.txt`:

```bash
chmod 640 compartido.txt
```

Comprueba:

```bash
ls -l compartido.txt
```

Traduce 640:

```text
6 = rw-
4 = r--
0 = ---
```

No avances hasta poder explicar cada dígito.

## 33. Práctica D — permisos de directorio

Sobre la carpeta creada:

```bash
chmod 700 carpeta-privada
```

Comprueba:

```bash
ls -ld carpeta-privada
```

Interpreta:

```text
rwx------
```

En un directorio, `x` permite atravesarlo, no “ejecutar la carpeta”.

## 34. Práctica E — consultar umask

Ejecuta:

```bash
umask
```

Anota el valor para ti.

No lo cambies en la shell principal.

Después, si los nombres `prueba-umask.txt` y `prueba-umask-dir` están libres, realiza la demostración aislada:

```bash
( umask 027; touch prueba-umask.txt; mkdir prueba-umask-dir; ls -ld prueba-umask.txt prueba-umask-dir )
```

Al terminar, vuelve a ejecutar:

```bash
umask
```

Debería mostrar el mismo valor que antes en tu shell principal.

## 35. Práctica F — inspección ACL opcional

Comprueba:

```bash
command -v getfacl
```

Si existe:

```bash
getfacl compartido.txt
```

Solo interpreta:

- owner;
- group;
- user;
- group;
- other.

No modifiques ACL todavía.

## 36. Práctica G — leer propietario y grupo

Ejecuta:

```bash
ls -l compartido.txt
id
```

Compara:

- propietario del archivo;
- grupo del archivo;
- tu usuario;
- tus grupos.

No uses `chown` aunque los nombres no coincidan como esperabas. Primero entiende por qué.

## 37. Qué no haremos

No ejecutes en esta lección:

```text
sudo chmod ...
sudo chown ...
chmod -R ...
chmod 777 ...
chown -R ...
setfacl ...
```

No porque todas esas formas sean siempre inválidas, sino porque aumentan el impacto o requieren contexto que aún no hemos estudiado.

## 38. Errores frecuentes

| Error | Problema | Corrección |
|---|---|---|
| Lees `rwx` igual en archivo y directorio | `x` y otros bits tienen efectos distintos | Interpreta según el tipo de objeto |
| Usas `chmod 777` para resolver permisos | Das acceso excesivo | Aplica mínimo privilegio |
| Usas `chmod -R` sin revisar ruta | Amplías el alcance | Practica primero sobre un objeto |
| Intentas `chown` con sudo para aprender | Cambias propiedad sin necesidad | Solo estudia sintaxis en este módulo |
| Tratas umask como resta decimal | Modelo incorrecto | Piensa en bits enmascarados |
| Confundes umask con máscara ACL | Son mecanismos diferentes | Separa creación inicial de ACL efectiva |
| Añades sudo ante “Permission denied” | Saltas el diagnóstico | Revisa necesidad, ruta y permisos |
| Crees que rwx explica todo | Ignoras ACL y otros controles | Recuerda que es la capa básica |

## 39. Método para diagnosticar un problema de permisos

Antes de cambiar nada:

1. ejecuta `whoami`;
2. ejecuta `id`;
3. inspecciona el objeto con `ls -ld`;
4. identifica propietario y grupo;
5. traduce los permisos de propietario, grupo y otros;
6. revisa permisos de los directorios del camino si procede;
7. solo después decide si un cambio es necesario.

No empieces con `sudo chmod`.

## 40. Práctica independiente

Dentro de una nueva carpeta de tu laboratorio:

1. crea un archivo;
2. consulta sus permisos iniciales;
3. establece `600`;
4. traduce el resultado a letras;
5. cambia simbólicamente para añadir lectura al grupo;
6. comprueba el resultado;
7. crea un directorio con `700`;
8. explica qué significa `x` en ese directorio;
9. consulta `umask`;
10. explica por qué no usarías `chmod 777`.

No uses `sudo`, `chown`, `chmod -R` ni `setfacl`.

## 41. Mini evaluación

1. En `-rw-r-----`, ¿quién tiene escritura?
   - A) Solo el propietario.
   - B) Grupo y otros.
   - C) Todos.

2. ¿Qué representa `chmod 640 archivo`?
   - A) `rw-r-----`
   - B) `rwxrwxrwx`
   - C) `r--------`

3. En un directorio, ¿qué permite principalmente `x`?
   - A) Atravesarlo/acceder a entradas conocidas según los demás permisos.
   - B) Convertirlo en programa.
   - C) Borrarlo automáticamente.

4. ¿`chmod 777` es una solución general recomendada?
   - A) Sí.
   - B) No.

5. ¿`umask` debe explicarse como resta decimal simple?
   - A) Sí.
   - B) No.

6. ¿Qué herramienta cambia propietario?
   - A) `chown`
   - B) `grep`
   - C) `pwd`

7. ¿Debemos practicar `sudo chown` sobre archivos del sistema?
   - A) Sí.
   - B) No.

8. ¿Qué herramienta inspecciona ACL cuando está disponible?
   - A) `getfacl`
   - B) `tail`
   - C) `mkdir`

9. ¿umask y la máscara de ACL son lo mismo?
   - A) Sí.
   - B) No.

## 42. Registro de aprendizaje

Puedes responder:

```text
r en un archivo significa:
w en un archivo significa:
x en un archivo significa:
x en un directorio significa:
640 significa:
700 significa:
chmod sirve para:
chown sirve para:
umask sirve para:
sudo NO debe usarse cuando:
Una ACL sirve para:
Algo que todavía confundo:
Estado: EN APRENDIZAJE / PRACTICADO
```

## 43. Fuentes y límites

Fuentes principales:

- GNU Coreutils — permisos de archivo:
  https://www.gnu.org/software/coreutils/manual/html_node/File-permissions.html
- GNU Coreutils — `chmod`:
  https://www.gnu.org/software/coreutils/manual/html_node/chmod-invocation.html
- GNU Coreutils — `chown`:
  https://www.gnu.org/software/coreutils/manual/html_node/chown-invocation.html
- GNU Bash Reference Manual — `umask` como builtin:
  https://www.gnu.org/software/bash/manual/html_node/Bourne-Shell-Builtins.html
- sudo manual:
  https://www.sudo.ws/docs/man/sudo.man/
- Linux man-pages — ACL:
  https://man7.org/linux/man-pages/man5/acl.5.html

Se posponen:

- setuid, setgid y sticky bit en profundidad;
- ACL por defecto;
- `setfacl` práctico;
- capacidades de Linux;
- SELinux y AppArmor;
- políticas sudoers;
- permisos recursivos;
- cambios de propietario administrativos.

**Estado de la lección:** redactada y revisada documentalmente. La práctica real del estudiante sigue pendiente.

---

**Siguiente:** [Módulo 13 — Procesos: ps, top y htop opcional](modulo-13-procesos-ps-top-htop.md) · [Volver al índice](README.md)
