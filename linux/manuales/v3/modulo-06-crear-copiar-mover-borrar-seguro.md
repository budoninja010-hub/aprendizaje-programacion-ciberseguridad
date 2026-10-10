# Módulo 6 — Crear, copiar, mover, renombrar y borrar con seguridad

Manual Maestro de Linux y Shell Scripting — Edición 2026 · v3 · Sexta entrega.

[Índice del manual](README.md) · [← Módulo 5](modulo-05-arbol-fhs-proc-sys-enlaces.md) · [Arquitectura](00-indice-arquitectura.md) · [Módulo 7 →](modulo-07-cat-less-head-tail.md)

## 1. Qué aprenderás

Al terminar este módulo podrás crear archivos y directorios de práctica, copiar archivos, moverlos o renombrarlos y distinguir correctamente `rm` de `rmdir`.

También aprenderás una regla esencial: **antes de borrar, primero comprueba ubicación, objetivo y tipo de objeto**.

Conocimientos previos:
- `pwd`, `ls`, `cd`;
- rutas absolutas y relativas;
- laboratorio `~/linux-lab`;
- reconocimiento básico de archivos, directorios y enlaces.

**Seguridad:** en este módulo todas las operaciones se limitan a una carpeta nueva dentro de `~/linux-lab`. No se utiliza `sudo`. No se usa `rm -rf`. No se modifica `/etc`, `/usr`, `/var`, `/proc` ni `/sys`.

**Cómo leer este módulo:** las secciones 2 a 14 explican cada orden con ejemplos. No las ejecutes todavía; la práctica empieza en la sección 15, dentro de la carpeta del laboratorio.

## 2. Crear un archivo con touch

`touch` se utiliza principalmente para modificar marcas de tiempo de archivos. Si el archivo indicado no existe, normalmente crea un archivo vacío.

Ejemplo:

```bash
touch notas.txt
```

Si `notas.txt` no existe, se crea un archivo vacío.

Comprueba:

```bash
ls -l notas.txt
```

**Importante:** si el archivo ya existe, `touch notas.txt` no lo vacía ni reemplaza su contenido; actualiza marcas de tiempo según el comportamiento normal de `touch`.

**Error típico:** pensar que `touch` siempre “crea desde cero”. Si el archivo ya existe, el efecto es diferente.

Referencia: GNU Coreutils, `touch`.

## 3. Crear directorios con mkdir

Ya utilizaste `mkdir`.

Ejemplo:

```bash
mkdir documentos
```

Esto crea un directorio llamado `documentos` en la ubicación actual.

Comprueba:

```bash
ls -ld documentos
```

Si el nombre ya existe, `mkdir` normalmente informa un error. En este curso ese error es útil: evita que sobreescribas o confundas una práctica existente.

### Opción -p

```bash
mkdir -p proyecto/notas
```

`-p` permite crear directorios padre necesarios y no falla únicamente porque ya exista la jerarquía prevista.

No uses `-p` automáticamente cuando quieras detectar nombres ya ocupados.

## 4. Copiar con cp

`cp` copia archivos y, con opciones apropiadas, directorios.

Ejemplo:

```bash
cp original.txt copia.txt
```

Aquí:
- `original.txt` es la fuente;
- `copia.txt` es el destino.

La copia es independiente del archivo original.

Comprueba:

```bash
ls -l original.txt copia.txt
```

Referencia: GNU Coreutils, `cp`.

## 5. Riesgo de sobrescritura con cp

Si el destino ya existe, `cp` puede reemplazar su contenido dependiendo de la operación y opciones utilizadas.

Por eso este manual no enseña a copiar “a ciegas”.

Antes:

```bash
ls -l
```

Después confirma que el destino que planeas usar no contiene trabajo que quieras conservar.

En prácticas iniciales puedes usar:

```bash
cp -i original.txt copia.txt
```

`-i` solicita confirmación antes de sobrescribir un archivo destino existente.

Esto ayuda a aprender, pero **no sustituye comprender qué estás copiando**.

## 6. Copiar directorios

Por defecto, `cp` no copia directorios de forma recursiva.

Para copiar un directorio y su contenido se utiliza una opción recursiva, por ejemplo:

```bash
cp -R carpeta-origen carpeta-copia
```

En este módulo solo la usarás dentro del laboratorio.

No necesitas aprender todavía todas las diferencias entre `-R`, `-r` y `-a`. Más adelante veremos preservación de metadatos y copias más completas.

## 7. Mover y renombrar con mv

`mv` sirve para mover o renombrar archivos y directorios.

Renombrar:

```bash
mv borrador.txt notas.txt
```

Mover a otra carpeta:

```bash
mv notas.txt documentos/
```

En el primer caso cambia el nombre. En el segundo cambia la ubicación.

Referencia: GNU Coreutils, `mv`.

## 8. Diferencia entre cp y mv

Modelo mental:

```text
cp = conservar original + crear copia
mv = cambiar nombre o ubicación del objeto
```

Ejemplo:

```bash
cp uno.txt dos.txt
```

Después pueden existir ambos.

En cambio:

```bash
mv uno.txt dos.txt
```

el nombre `uno.txt` deja de representar el objeto original en esa ubicación si la operación termina correctamente.

**Error típico:** usar `mv` esperando conservar una copia.

## 9. Riesgo de sobrescritura con mv

`mv` también puede reemplazar un destino existente en determinadas circunstancias.

Para prácticas iniciales:

```bash
mv -i origen.txt destino.txt
```

`-i` puede pedir confirmación antes de reemplazar.

Pero primero debes inspeccionar:

```bash
pwd
ls -la
```

No conviertas `-i` en una excusa para dejar de verificar las rutas.

## 10. Borrar archivos con rm

`rm` elimina archivos.

Ejemplo:

```bash
rm archivo.txt
```

A diferencia de una interfaz gráfica, `rm` no debe asumirse como “mover a la papelera”.

Antes de usarlo en este curso:

```bash
pwd
ls -l archivo.txt
```

Después decide si ese archivo es realmente el objetivo.

### Opción interactiva

Durante el aprendizaje puedes usar:

```bash
rm -i archivo.txt
```

`-i` pregunta antes de eliminar cada archivo.

Referencia: GNU Coreutils, `rm`.

## 11. rmdir: solo directorios vacíos

`rmdir` elimina directorios vacíos.

Ejemplo:

```bash
rmdir carpeta-vacia
```

Si la carpeta contiene archivos o subdirectorios, la operación falla.

Ese fallo es útil para un principiante porque evita eliminar contenido accidentalmente.

Referencia: GNU Coreutils, `rmdir`.

## 12. rm y rmdir no son equivalentes

Recuerda:

```text
rm archivo.txt
rmdir carpeta-vacia
```

No enseñaremos todavía borrado recursivo como práctica rutinaria.

GNU `rm` dispone de opciones recursivas como `-r` o `-R`, pero implican un alcance mucho mayor porque pueden eliminar árboles completos de directorios.

## 13. Por qué no usamos rm -rf como hábito

`rm -rf` combina dos comportamientos de alto impacto:

- `-r`: eliminación recursiva;
- `-f`: fuerza la operación y elimina varias confirmaciones.

Eso puede borrar muchos archivos si la ruta es incorrecta.

Por eso:

- no aparece como comando normal de principiante;
- no se usa para “limpiar” ejercicios;
- no se añade `sudo`;
- no se prueba sobre directorios del sistema.

Más adelante podrás estudiar qué significa técnicamente, pero no necesitas ejecutarlo para aprender Linux correctamente.

## 14. Los tres controles antes de borrar

Antes de una eliminación revisa:

### Control 1 — ubicación

```bash
pwd
```

¿Estás donde crees?

### Control 2 — objetivo

```bash
ls -ld nombre
```

¿El nombre existe y es el objeto esperado?

### Control 3 — alcance

Pregunta:

> ¿Voy a eliminar un archivo, un directorio vacío o algo que contiene más elementos?

Si la respuesta no está clara, no ejecutes la eliminación.

`pwd` y `ls` ayudan, pero no son una garantía automática: también debes interpretar la ruta y el tipo de objeto.

## 15. Práctica guiada — preparar el laboratorio

Entra al laboratorio:

```bash
cd ~/linux-lab
pwd
ls -la
```

Si `cd` falla, detente.

Comprueba si existe:

```bash
ls -ld ./modulo-06-archivos
```

Si informa que no existe:

```bash
mkdir modulo-06-archivos
```

Después:

```bash
cd ./modulo-06-archivos
pwd
ls -la
```

No borres una carpeta previa para repetir la práctica. Si existe, inspecciona primero su contenido.

## 16. Crear archivos de práctica

Crea dos archivos vacíos:

```bash
touch original.txt
touch temporal.txt
```

Comprueba:

```bash
ls -l
```

Debes identificar ambos archivos.

## 17. Copiar

Ejecuta:

```bash
cp original.txt copia.txt
```

Después:

```bash
ls -l
```

Responde:

- ¿sigue existiendo `original.txt`?
- ¿aparece `copia.txt`?

La respuesta esperada es sí a ambas si la copia terminó correctamente.

## 18. Renombrar

Ahora:

```bash
mv copia.txt respaldo.txt
```

Comprueba:

```bash
ls -l
```

Debes poder explicar que:
- `copia.txt` ya no aparece con ese nombre;
- `respaldo.txt` representa el objeto movido/renombrado.

## 19. Crear y mover a un directorio

Crea:

```bash
mkdir documentos
```

Después mueve:

```bash
mv respaldo.txt documentos/
```

Comprueba:

```bash
ls -l
ls -l documentos
```

Explica la diferencia entre la ubicación anterior y la nueva.

## 20. Borrado controlado de un archivo de práctica

Solo eliminaremos `temporal.txt`, que se creó específicamente para este ejercicio.

Primero:

```bash
pwd
ls -l temporal.txt
```

Si ambas comprobaciones coinciden con la práctica:

```bash
rm -i temporal.txt
```

Lee la pregunta que muestre `rm` y confirma solo si el nombre coincide exactamente.

Después:

```bash
ls -l
```

No elimines `original.txt` ni la carpeta `documentos`.

## 21. Práctica de rmdir

Crea una carpeta vacía:

```bash
mkdir vacia
```

Comprueba:

```bash
ls -ld vacia
```

Después:

```bash
rmdir vacia
```

Comprueba otra vez:

```bash
ls -ld vacia
```

Ahora debería aparecer un mensaje indicando que ya no existe.

Ese mensaje, después de una eliminación deliberada y verificada, puede ser el resultado esperado.

## 22. Provocar un error seguro con rmdir

Crea:

```bash
mkdir no-vacia
touch no-vacia/nota.txt
```

Intenta:

```bash
rmdir no-vacia
```

Debe fallar porque contiene `nota.txt`.

**No corrijas el error borrando el archivo.**

Déjala así para recordar qué protege `rmdir`.

## 23. Errores frecuentes

| Error | Por qué ocurre | Corrección mínima |
|---|---|---|
| `cp` deja dos archivos y creías que movería | `cp` copia | Usa `mv` solo cuando quieras mover/renombrar |
| `mv` hace desaparecer el nombre original | Se movió o renombró | Comprueba el destino antes de repetir |
| `rmdir` falla en una carpeta | No está vacía | Inspecciona; no borres contenido automáticamente |
| `rm` elimina el archivo equivocado | Ruta o nombre incorrecto | Verifica `pwd`, objetivo y alcance |
| Aparece “Permission denied” | No tienes permiso | No añadas `sudo`; revisa la ubicación |
| Un nombre empieza con `-` | Puede interpretarse como opción | No improvises; aprende después el uso de `--` o rutas explícitas |
| Quieres usar `rm -rf` para limpiar rápido | Estás aumentando demasiado el alcance | Conserva la práctica o elimina de forma controlada más adelante |

## 24. Práctica independiente

Sin copiar la secuencia guiada:

1. Dentro de `~/linux-lab`, crea una carpeta nueva para una segunda práctica.
2. Crea `archivo1.txt`.
3. Cópialo como `archivo2.txt`.
4. Renombra la copia como `respaldo.txt`.
5. Crea un directorio `guardados`.
6. Mueve `respaldo.txt` dentro.
7. Comprueba cada paso con `ls`.
8. Explica antes de borrar qué objeto podrías eliminar de forma segura.
9. No uses `rm -rf`.

Si algo falla, conserva el estado y explica el error; no reinicies borrando todo.

## 25. Mini evaluación

1. ¿Qué hace normalmente `cp`?
   - A) Copia.
   - B) Borra.
   - C) Cambia permisos.
   - D) Reinicia.

2. ¿Qué hace `mv`?
   - A) Solo copia.
   - B) Mueve o renombra.
   - C) Solo lista.
   - D) Cambia usuario.

3. ¿Qué elimina `rmdir`?
   - A) Cualquier árbol de archivos.
   - B) Directorios vacíos.
   - C) Procesos.
   - D) Paquetes.

4. ¿`rm` debe suponerse equivalente a una papelera gráfica?
   - A) Sí.
   - B) No.

5. ¿Cuál es el orden correcto antes de borrar?
   - A) Borrar y después comprobar.
   - B) Comprobar ubicación, objetivo y alcance.
   - C) Añadir `sudo`.
   - D) Usar siempre `-f`.

6. ¿Por qué no usamos `rm -rf` como práctica rutinaria?
   - A) Porque no existe.
   - B) Porque puede eliminar recursivamente con pocas protecciones si la ruta es incorrecta.
   - C) Porque solo funciona en Windows.
   - D) Porque crea archivos.

## 26. Registro de aprendizaje

Puedes responder:

```text
cp sirve para:
mv sirve para:
rm sirve para:
rmdir sirve para:
Antes de borrar debo comprobar:
Un error que provoqué de forma segura:
Algo que todavía confundo:
Estado: EN APRENDIZAJE / PRACTICADO
```

No se considera dominado porque una práctica salga una vez. En otra sesión deberás realizar un ejercicio equivalente sin copiar y detectar un error por tu cuenta.

## 27. Fuentes y límites

Clasificación y estado de los enlaces de esta sección: [catálogo de fuentes](auditorias/06-catalogo-fuentes.md) (jerarquía E04, comprobación del 9 de octubre de 2026).

Fuentes principales:

- GNU Coreutils — `cp`: https://www.gnu.org/software/coreutils/manual/html_node/cp-invocation.html
- GNU Coreutils — `mv`: https://www.gnu.org/software/coreutils/manual/html_node/mv-invocation.html
- GNU Coreutils — `rm`: https://www.gnu.org/software/coreutils/manual/html_node/rm-invocation.html
- GNU Coreutils — `rmdir`: https://www.gnu.org/software/coreutils/manual/html_node/rmdir-invocation.html
- GNU Coreutils — `touch`: https://www.gnu.org/software/coreutils/manual/html_node/touch-invocation.html

Esta lección usa una selección pequeña de opciones. No intenta cubrir todas las posibilidades de GNU Coreutils.

**Vigencia (E05):** la lección se redactó con GNU Coreutils 9.11. El 9 de octubre de 2026 el manual oficial en línea documenta la versión 9.12. Las opciones usadas aquí son básicas, pero tu sistema puede tener otra versión: compruébala con `cp --version`.

**Estado de la lección:** redactada y revisada documentalmente. La práctica real del estudiante sigue pendiente.

---

**Siguiente:** [Módulo 7 — Leer archivos con cat, less, head y tail](modulo-07-cat-less-head-tail.md) · [Volver al índice](README.md)
