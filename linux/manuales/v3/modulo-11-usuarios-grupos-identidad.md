# Módulo 11 — Usuarios y grupos: whoami, id, UID, GID e identidad

Manual Maestro de Linux y Shell Scripting — Edición 2026 · v3 · Undécima entrega.

[Índice del manual](README.md) · [← Módulo 10](modulo-10-grep-find-locate.md) · [Arquitectura](00-indice-arquitectura.md) · [Módulo 12 →](modulo-12-permisos-chmod-chown-umask-sudo-acl.md)

## 1. Qué aprenderás

Al terminar este módulo podrás:

- explicar qué representa un usuario en GNU/Linux;
- distinguir nombre de usuario de UID;
- distinguir nombre de grupo de GID;
- reconocer grupo primario y grupos suplementarios;
- consultar tu identidad con `whoami` e `id`;
- interpretar una salida básica de `id`;
- reconocer que `root` y UID 0 requieren especial cuidado;
- diferenciar consultar identidad de modificar usuarios o grupos.

Conocimientos previos:
- terminal y Bash;
- lectura de archivos;
- rutas;
- `grep` básico.

**Seguridad:** este módulo es de consulta. No crearemos, eliminaremos ni modificaremos usuarios o grupos. No cambiaremos contraseñas ni archivos de cuentas. No uses `sudo` para estas prácticas. No publiques listas completas de usuarios, nombres reales, rutas personales ni otros datos de identidad en GitHub o en el chat.

## 2. Qué es un usuario

Un **usuario** es una identidad que el sistema utiliza para asociar procesos, archivos, permisos y otras decisiones de acceso.

No debes pensar únicamente en “una persona que inicia sesión”.

También pueden existir cuentas utilizadas por:

- servicios;
- demonios;
- aplicaciones;
- tareas del sistema.

Por eso un equipo Linux puede tener más cuentas que personas.

## 3. Nombre de usuario y UID

Una cuenta suele tener un nombre legible, por ejemplo:

```text
alumno
```

Pero internamente el sistema utiliza un identificador numérico:

```text
UID
```

UID significa **User Identifier**.

Modelo:

```text
nombre de usuario ──► UID
alumno              ──► 1000   (ejemplo ilustrativo)
```

El número 1000 es solo un ejemplo. No asumas que tu UID será ese.

**Idea importante:** los permisos del sistema se basan en identificadores y metadatos, no únicamente en el texto visible del nombre.

## 4. Qué es un grupo

Un **grupo** reúne identidades para facilitar decisiones de acceso.

En lugar de asignar determinados permisos individualmente a muchas cuentas, un sistema puede usar pertenencia a grupos.

Los grupos también tienen:

- un nombre;
- un identificador numérico llamado **GID**.

GID significa **Group Identifier**.

Modelo:

```text
nombre de grupo ──► GID
estudiantes       ──► 1000   (ejemplo ilustrativo)
```

De nuevo, el número es solo ilustrativo.

## 5. Grupo primario y grupos suplementarios

Un usuario puede tener:

- un **grupo primario**;
- cero o más **grupos suplementarios**.

El grupo primario participa, entre otras cosas, en la asociación de grupo que puede recibir un archivo nuevo según el contexto y las reglas aplicables.

Los grupos suplementarios amplían pertenencias disponibles para decisiones de acceso.

No estudiaremos todavía todos los detalles de creación de archivos ni de ACL; el Módulo 12 introduce los permisos y las ACL básicas. El bit SGID de directorios queda fuera del núcleo inicial y se pospone.

## 6. whoami — quién soy en esta sesión

Ejecuta:

```bash
whoami
```

En GNU Coreutils, `whoami` muestra el nombre asociado al **usuario efectivo** del proceso actual.

Es equivalente conceptualmente a:

```bash
id -un
```

para esta consulta.

**No confundas** `whoami` con “mostrar todas las cuentas del sistema”. Solo responde quién eres desde el punto de vista de la identidad efectiva actual.

Referencia: GNU Coreutils — `whoami`.

## 7. id — información de identidad

Ejecuta:

```bash
id
```

Una salida ilustrativa podría parecerse a:

```text
uid=1000(alumno) gid=1000(alumno) groups=1000(alumno),27(ejemplo)
```

Tu salida será diferente.

Partes básicas:

- `uid=` → UID del usuario;
- `gid=` → GID del grupo primario;
- `groups=` → grupos asociados.

No copies una salida ilustrativa como si fuera la tuya.

## 8. Consultar solo el UID

```bash
id -u
```

Muestra el UID numérico de la identidad actual.

Para solicitar el nombre en vez del número:

```bash
id -un
```

Aquí:

- `-u` selecciona el identificador de usuario;
- `-n` solicita el nombre correspondiente.

Por eso `id -un` se relaciona con `whoami`.

## 9. Consultar el GID primario

```bash
id -g
```

Muestra el GID primario numérico.

Para el nombre:

```bash
id -gn
```

No confundas UID y GID:

```text
UID = usuario
GID = grupo
```

## 10. Consultar grupos

```bash
id -G
```

muestra identificadores numéricos de los grupos.

Con nombres:

```bash
id -Gn
```

También puede existir la utilidad:

```bash
groups
```

para mostrar nombres de grupos asociados.

En este manual priorizamos `id` porque reúne varias consultas relacionadas en una sola herramienta.

## 11. Por qué importan los identificadores numéricos

Supón un archivo con propietario:

```text
alumno
```

Visualmente ves un nombre.

Pero el sistema mantiene identificadores numéricos asociados a propietario y grupo.

Eso ayuda a comprender situaciones como:

- archivos copiados entre sistemas;
- cuentas recreadas;
- contenedores;
- volúmenes compartidos;
- discrepancias entre nombres y números.

Todavía no resolveremos esos escenarios. Solo necesitamos entender que nombre e ID son conceptos relacionados, no idénticos.

## 12. root y UID 0

Tradicionalmente, la cuenta administrativa principal se llama:

```text
root
```

y utiliza UID:

```text
0
```

UID 0 recibe tratamiento privilegiado especial en muchos controles del sistema.

**Regla de seguridad:** no trabajes como root para prácticas ordinarias.

Para aprender navegación, lectura, búsqueda y Bash básico debes utilizar tu usuario normal.

Más adelante estudiaremos privilegios mínimos y `sudo` de forma controlada.

## 13. root no significa “modo mágico”

Aunque root tiene privilegios muy amplios, eso no elimina:

- errores humanos;
- rutas incorrectas;
- comandos destructivos;
- pérdida de datos;
- restricciones externas;
- mecanismos modernos de seguridad;
- límites de contenedores o entornos.

Tener más privilegios aumenta el impacto posible de un error.

Por eso:

> privilegio elevado se usa solo cuando una tarea realmente lo exige.

## 14. sudo y la identidad

`sudo` puede permitir ejecutar una orden con otra identidad de acuerdo con una política configurada.

En muchos sistemas, el caso habitual es ejecutar una orden autorizada con privilegios elevados.

No significa que debas anteponer `sudo` a cualquier comando que falle.

En este módulo no ejecutaremos ninguna orden administrativa.

## 15. /etc/passwd — información de cuentas

Tradicionalmente, información básica de cuentas se expone en:

```text
/etc/passwd
```

A pesar de su nombre, en sistemas modernos no suele contener las contraseñas secretas en texto claro.

Una línea típica tiene campos separados por `:`.

No necesitas memorizar todos los campos todavía.

Puedes consultar de forma limitada:

```bash
head -n 5 /etc/passwd
```

pero **no pegues la salida completa** en el chat o en GitHub: puede revelar nombres de cuentas y estructura del sistema.

## 16. /etc/shadow no es material de práctica

Las credenciales y datos sensibles relacionados con autenticación pueden almacenarse en archivos protegidos como:

```text
/etc/shadow
```

No intentes abrirlo con `sudo` para completar el módulo.

No necesitamos su contenido para aprender usuarios y grupos.

**Regla:** nunca publiques hashes, credenciales ni archivos de autenticación.

## 17. /etc/group — información de grupos

Información tradicional sobre grupos se encuentra en:

```text
/etc/group
```

Puedes observar unas pocas líneas:

```bash
head -n 5 /etc/group
```

De nuevo, no compartas el archivo completo si no es necesario.

La herramienta `id` es mejor para consultar tus pertenencias actuales sin revisar manualmente grandes archivos.

## 18. Nombre visible frente a identidad efectiva

Una sesión puede tener conceptos de identidad más complejos que “el nombre con el que inicié sesión”.

Por eso `whoami` se define alrededor del **usuario efectivo**.

Más adelante, al estudiar procesos y privilegios, veremos con más detalle:

- identidad real;
- identidad efectiva;
- cambios de privilegio;
- procesos.

Por ahora basta con saber que `whoami` responde la identidad efectiva que la herramienta observa.

## 19. Preparar la práctica

Entra al laboratorio:

```bash
cd ~/linux-lab
pwd
```

No necesitas crear archivos para consultar tu identidad.

Si quieres registrar tus respuestas, crea una carpeta de práctica:

```bash
ls -ld ./modulo-11-identidad
```

Si no existe:

```bash
mkdir modulo-11-identidad
```

No guardes automáticamente en ella la salida completa de archivos de cuentas.

## 20. Práctica A — whoami

Ejecuta:

```bash
whoami
```

Anota para ti el nombre mostrado.

Pregunta:

> ¿esto representa el UID numérico?

No. Representa el nombre de la identidad efectiva.

## 21. Práctica B — id

Ejecuta:

```bash
id
```

Sin copiar la salida completa al chat, identifica:

- UID;
- nombre del usuario;
- GID primario;
- nombre del grupo primario;
- grupos adicionales, si aparecen.

## 22. Práctica C — consultas específicas

Ejecuta una por una:

```bash
id -u
id -un
id -g
id -gn
id -G
id -Gn
```

Relaciona:

```text
-u  → usuario
-g  → grupo primario
-G  → grupos
-n  → nombres en vez de IDs numéricos
```

No memorices las opciones sin entender qué dato cambia.

## 23. Práctica D — comparar whoami con id -un

Ejecuta:

```bash
whoami
id -un
```

En una sesión normal deberían referirse al mismo usuario efectivo.

Si no comprendes un resultado inesperado, no intentes corregir usuarios o privilegios: registra la diferencia y revísala.

## 24. Práctica E — inspección limitada de cuentas

Ejecuta:

```bash
head -n 5 /etc/passwd
```

Después:

```bash
head -n 5 /etc/group
```

Objetivo:

- reconocer que existen archivos tradicionales de información de cuentas y grupos;
- no memorizar cada línea;
- no modificar nada.

No subas estas salidas a GitHub.

## 25. Práctica F — buscar tu propio nombre de usuario de forma controlada

Primero obtén tu nombre con:

```bash
whoami
```

Luego consulta tu propia cuenta. La orden siguiente usa `$(id -un)`: Bash ejecuta primero `id -un` y coloca su resultado en ese lugar, así no necesitas escribir tu nombre. Esta sintaxis se estudia a fondo en el Módulo 24.

```bash
getent passwd "$(id -un)"
```

`id -un` obtiene el nombre de usuario actual; `getent passwd` consulta la base de cuentas mediante NSS, que también puede integrar servicios de directorio como LDAP o SSSD. Buscar solo en `/etc/passwd` con `grep` no permite concluir que una cuenta no existe si la búsqueda queda vacía.

Si la línea aparece, no la publiques completa. Úsala solo para reconocer la relación entre nombre de cuenta y registro del sistema.

## 26. Usuarios de servicio

Si observas `/etc/passwd`, puedes encontrar nombres que no correspondan a personas.

Eso es normal.

Muchos servicios usan cuentas separadas para limitar privilegios y aislar responsabilidades.

No elimines una cuenta porque “no reconoces su nombre”.

Modificar cuentas de servicio sin entenderlas puede romper aplicaciones o el sistema.

## 27. UID bajo o alto no define por sí solo “humano” o “seguro”

Las distribuciones suelen reservar rangos para diferentes tipos de cuentas, pero los rangos concretos dependen de políticas y distribución.

No memorices una regla universal como:

```text
UID menor que X = servicio
UID mayor que X = persona
```

sin consultar la política real del sistema.

Para identificar tu propia cuenta usa herramientas como `id`, no una suposición basada solo en el número.

## 28. Errores frecuentes

| Error | Problema | Corrección |
|---|---|---|
| Confundes nombre con UID | Uno es etiqueta legible; otro identificador numérico | Usa `id -un` frente a `id -u` |
| Confundes UID con GID | Usuario y grupo son conceptos distintos | Recuerda U=user, G=group |
| Crees que solo existen cuentas humanas | Servicios también usan cuentas | No elimines cuentas desconocidas |
| Ejecutas todo con root | Amplías innecesariamente el impacto | Usa usuario normal |
| Antepones `sudo` si algo falla | Privilegios no corrigen errores conceptuales | Revisa la tarea y la ruta |
| Intentas leer `/etc/shadow` | Es información sensible y no necesaria | No lo hagas |
| Publicas `/etc/passwd` completo | Revela información del sistema | Comparte solo el mínimo necesario |

## 29. Método para interpretar id

Si ves una salida compleja de `id`:

1. localiza `uid=`;
2. identifica número y nombre;
3. localiza `gid=`;
4. identifica grupo primario;
5. localiza `groups=`;
6. separa cada pertenencia;
7. no cambies nada solo porque haya grupos que no reconozcas.

## 30. Práctica independiente

Sin copiar la tabla de opciones:

1. muestra tu nombre efectivo;
2. consulta tu UID numérico;
3. consulta el nombre asociado a ese usuario;
4. consulta el GID primario;
5. consulta el nombre del grupo primario;
6. muestra tus grupos por nombre;
7. explica la diferencia entre UID y GID;
8. explica por qué no debemos practicar como root.

No uses `sudo`.

## 31. Mini evaluación

1. ¿Qué significa UID?
   - A) User Identifier.
   - B) Universal Internet Directory.
   - C) User Installation Driver.

2. ¿Qué significa GID?
   - A) General Internet Data.
   - B) Group Identifier.
   - C) GNU Internal Disk.

3. ¿Qué muestra `whoami` en GNU Coreutils?
   - A) La identidad efectiva por nombre.
   - B) Todos los usuarios.
   - C) Los archivos del usuario.
   - D) La contraseña.

4. ¿Qué muestra `id -u`?
   - A) UID numérico.
   - B) GID.
   - C) Nombre del host.
   - D) Ruta actual.

5. ¿Qué muestra `id -g`?
   - A) UID.
   - B) GID primario.
   - C) Todos los procesos.
   - D) La shell.

6. ¿Puede un usuario pertenecer a varios grupos?
   - A) Sí.
   - B) No.

7. ¿Debemos abrir `/etc/shadow` con sudo para esta lección?
   - A) Sí.
   - B) No.

8. ¿Trabajar como root reduce el impacto de errores?
   - A) Sí.
   - B) No.

## 32. Registro de aprendizaje

Puedes responder:

```text
Un usuario es:
Un grupo es:
UID significa:
GID significa:
whoami muestra:
id -u muestra:
id -g muestra:
id -Gn muestra:
¿Por qué no debo trabajar como root?:
Algo que todavía confundo:
Estado: EN APRENDIZAJE / PRACTICADO
```

Antes de compartir respuestas, elimina nombres de cuenta privados si no son necesarios.

## 33. Fuentes y límites

Clasificación y estado de los enlaces de esta sección: [catálogo de fuentes](auditorias/06-catalogo-fuentes.md) (jerarquía E04, comprobación del 9 de octubre de 2026).

Fuentes principales:

- GNU Coreutils — `whoami`:
  https://www.gnu.org/software/coreutils/manual/html_node/whoami-invocation.html
- GNU Coreutils — `id`:
  https://www.gnu.org/software/coreutils/manual/html_node/id-invocation.html
- Linux man-pages — `passwd(5)`:
  https://man7.org/linux/man-pages/man5/passwd.5.html
- Linux man-pages — `group(5)`:
  https://man7.org/linux/man-pages/man5/group.5.html
- Linux man-pages — credentials:
  https://man7.org/linux/man-pages/man7/credentials.7.html

Se posponen:

- creación y eliminación de cuentas;
- `useradd`, `usermod`, `userdel`;
- `groupadd` y administración de grupos;
- contraseñas y `passwd`;
- PAM;
- NSS;
- LDAP y directorios;
- capacidades de Linux;
- identidad real, efectiva y saved IDs en profundidad;
- sudoers;
- ACL.

**Estado de la lección:** redactada y revisada documentalmente. La práctica real del estudiante sigue pendiente.

---

**Siguiente:** [Módulo 12 — Permisos, propietarios, chmod, chown, umask, sudo y ACL básica](modulo-12-permisos-chmod-chown-umask-sudo-acl.md) · [Volver al índice](README.md)
