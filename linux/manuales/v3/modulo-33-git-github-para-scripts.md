# Módulo 33 — Git y GitHub para scripts; puente al itinerario específico de Git

Manual Maestro de Linux y Shell Scripting — Edición 2026 · v3 · Trigésima tercera entrega.

[Índice del manual](README.md) · [← Módulo 32](modulo-32-rsync-copias-restauracion.md) · [Arquitectura](00-indice-arquitectura.md) · [Módulo 34 →](modulo-34-almacenamiento-lsblk-df-du-montaje-fstab.md)

## 1. Propósito de este módulo

Este módulo no sustituye al **Manual Maestro de Git y GitHub — Edición 2026**.

Su función es darte autonomía suficiente para guardar de forma segura tus scripts de Linux/Bash en Git y GitHub sin duplicar todo el itinerario específico de Git.

Objetivo de evidencia:

> **Revisar diferencias y guardar commits sin secretos.**

## 2. Qué aprenderás

Al terminar este módulo podrás:

- explicar la diferencia entre Git y GitHub;
- reconocer repositorio, working tree, staging area e historial;
- comprobar el estado con `git status`;
- revisar cambios con `git diff`;
- preparar cambios con `git add`;
- revisar exactamente lo que entrará al commit con `git diff --staged`;
- crear commits pequeños con mensajes claros;
- consultar historial con `git log`;
- entender qué hace `.gitignore` y qué no hace;
- detectar archivos sensibles antes de añadirlos;
- verificar un remoto con `git remote -v`;
- distinguir commit local de `push` a GitHub;
- realizar un `push` solo cuando el repositorio y la rama sean correctos;
- usar `git restore --staged` para sacar un archivo del staging sin borrar el archivo de trabajo;
- comprender por qué `git restore` puede descartar cambios y debe revisarse antes de usarlo;
- evitar comandos destructivos o de reescritura de historial mientras aprendes.

## 3. Git y GitHub no son lo mismo

**Git** es un sistema de control de versiones distribuido.

**GitHub** es una plataforma que puede alojar repositorios Git y añadir colaboración, revisión, issues, pull requests, Actions y otras funciones.

Puedes usar Git sin GitHub.

También puedes tener un repositorio Git local que todavía no se haya publicado en ningún servidor.

## 4. Modelo mental mínimo

```text
working tree
    ↓ git add
staging area / index
    ↓ git commit
historial local
    ↓ git push
repositorio remoto en GitHub
```

Cada flecha es una acción distinta.

## 5. Qué es el working tree

Es la copia de archivos que estás editando en tu carpeta de proyecto.

Ejemplo:

```text
script.sh
README.md
.gitignore
```

Los cambios que haces primero existen en tu working tree.

## 6. Qué es el staging area

También se llama **index**.

Sirve para preparar el contenido del próximo commit.

Git no obliga a incluir todos tus cambios juntos.

Puedes preparar solo algunos archivos o incluso partes de archivos.

## 7. Qué es un commit

Un commit registra el contenido preparado en el index junto con metadatos y un mensaje.

Un commit debe representar una unidad lógica de cambio.

Ejemplo de este proyecto:

```text
linux: práctica de funciones Bash
```

Mejor que:

```text
cambios
```

## 8. GitHub entra después

Un commit existe localmente aunque no hayas hecho `push`.

`git push` publica commits hacia un remoto configurado.

Por eso:

```text
commit ≠ push
```

## 9. Comprobar Git

```bash
git --version
```

Después:

```bash
command -v git
```

Son operaciones de consulta.

## 10. Preparar el laboratorio

```bash
test -d ~/linux-lab && \
cd ~/linux-lab && \
mkdir -p modulo-33-git && \
cd modulo-33-git && pwd
pwd
```

Etiqueta: **creación en laboratorio**.

## 11. Inicializar un repositorio de práctica

```bash
git init -b main
```

Esto crea metadatos Git dentro de:

```text
.git/
```

No sube nada a Internet.

## 12. Consultar estado

```bash
git status
```

`git status` muestra, entre otras cosas:

- cambios preparados para commit;
- cambios modificados pero no preparados;
- archivos no rastreados;
- información de rama.

Es uno de los comandos que debes ejecutar con más frecuencia.

**Antes del ejemplo: qué es un here-document.** La sintaxis `<<'EOF'` entrega al comando varias líneas de entrada hasta encontrar una línea que contenga únicamente `EOF`. Las comillas alrededor de `EOF` impiden que Bash expanda variables y sustituciones de comandos dentro del bloque. En `cat > archivo`, el signo `>` crea o sobrescribe el archivo: comprueba antes que el nombre está libre y que estás en el directorio del laboratorio. Si ya existe, conserva la versión anterior y usa Vim para editarla sin perder el trabajo.

## 13. Crear un archivo de práctica

```bash
cat > hola.sh <<'EOF'
#!/usr/bin/env bash
printf 'Hola desde Git y Bash\n'
EOF
```

Después:

```bash
git status
```

`hola.sh` debe aparecer como archivo no rastreado.

## 14. Revisar antes de añadir

Para un archivo no rastreado pequeño puedes inspeccionarlo con:

```bash
cat hola.sh
```

También:

```bash
bash -n hola.sh
```

Si ShellCheck está disponible:

```bash
shellcheck hola.sh
```

Primero revisa contenido; después prepara el commit.

## 15. `git add`

```bash
git add hola.sh
```

`git add` añade el contenido actual del archivo al index.

Importante:

> Si modificas el archivo después de `git add`, debes volver a ejecutar `git add` para preparar esa nueva versión.

## 16. Confirmar estado después de `git add`

```bash
git status
```

Ahora `hola.sh` debe aparecer preparado para commit.

## 17. Revisar lo preparado

```bash
git diff --staged
```

Este paso es obligatorio en nuestro flujo de aprendizaje.

No basta con saber qué archivos están staged; debes revisar **qué contenido** entrará.

## 18. Flujo mínimo antes de commit

```text
git status
git diff
git add archivo
git diff --staged
git status
git commit
```

Esta secuencia reduce commits accidentales.

## 19. Crear el primer commit

```bash
git commit -m 'linux: primer script Bash versionado'
```

El commit registra únicamente el contenido preparado.

## 20. Consultar historial

```bash
git log --oneline --decorate
```

Esto muestra una vista compacta del historial.

## 21. Modificar el script

```bash
printf "printf 'Segunda línea de práctica\\n'\n" >> hola.sh
```

Después:

```bash
git status
git diff
```

`git diff` muestra cambios del working tree que todavía no están staged.

## 22. `git diff` y `git diff --staged`

Modelo:

```text
git diff
working tree ↔ index

git diff --staged
index ↔ HEAD
```

`HEAD` suele referirse al commit actual de la rama.

## 23. Preparar segundo cambio

```bash
git add hola.sh
git diff --staged
```

Solo si la diferencia es correcta:

```bash
git commit -m 'linux: amplía práctica de salida con printf'
```

## 24. Commits pequeños

Evita guardar en un mismo commit:

- un script Bash;
- una configuración de red;
- documentación no relacionada;
- archivos binarios grandes;
- credenciales;
- cambios experimentales de otro tema.

Mejor:

```text
un cambio lógico → un commit claro
```

## 25. Qué hace `.gitignore`

Un archivo `.gitignore` especifica patrones de archivos **no rastreados** que Git debe ignorar.

Ejemplo:

```gitignore
*.log
tmp/
.env
```

## 26. Qué `.gitignore` NO hace

Si un archivo ya está rastreado, añadirlo después a `.gitignore` no hace que Git deje de rastrearlo automáticamente.

Esto es importante con secretos.

`.gitignore` es prevención, no una herramienta mágica para borrar historial.

## 27. Regla de secretos

Nunca prepares ni publiques:

- contraseñas;
- tokens;
- API keys;
- cookies;
- claves SSH privadas;
- archivos `.env` con secretos;
- credenciales de nube;
- datos personales innecesarios.

GitHub advierte explícitamente que no debes añadir, confirmar ni subir información sensible a un repositorio remoto.

### Si el secreto YA fue confirmado o publicado

Añadir el archivo a `.gitignore` o borrar el secreto en un commit nuevo **no invalida una credencial que ya fue expuesta**.

GitHub recomienda tratar una credencial filtrada como comprometida. El orden defensivo es:

```text
1. detener nuevos pushes o cambios innecesarios
2. identificar qué credencial fue expuesta y qué servicio la emitió
3. revocar o rotar la credencial con su proveedor
4. actualizar de forma segura los sistemas legítimos que dependían de ella
5. retirar el secreto del código y del working tree
6. decidir si hace falta sanear el historial del repositorio
7. coordinar la limpieza de clones, forks o ramas afectadas si corresponde
8. revisar por qué ocurrió y añadir prevención
```

La prioridad es **invalidar la credencial**, no “hacer desaparecer el texto” primero.

GitHub señala que reescribir historial puede tener efectos secundarios importantes:

- cambia hashes de commits;
- puede afectar ramas y pull requests;
- otros clones pueden volver a introducir el secreto;
- requiere coordinación con colaboradores;
- un secreto puede seguir existiendo en forks, clones o referencias históricas.

Por eso este módulo **no enseña una receta automática de force-push o reescritura de historial**. Si realmente ocurre una exposición, primero se revoca/rota la credencial y después se sigue la documentación oficial de GitHub para la limpieza apropiada.

### Push protection y secret scanning

GitHub puede detectar ciertos secretos y bloquear un push mediante **push protection**.

Si un push es bloqueado por un secreto real:

```text
no lo fuerces ni lo ignores por comodidad
→ retira el secreto
→ revoca/rota si ya pudo quedar expuesto
→ vuelve a revisar el commit
```

Push protection es una capa preventiva; no reemplaza tu propia revisión.

**Antes de ejecutar:** `cat > archivo <<'EOF'` utiliza un *here-document*: envía a `cat` las líneas siguientes hasta el delimitador `EOF`. Las comillas impiden expansiones de variables y comandos dentro del bloque. La redirección `>` **crea o sobrescribe** el destino; verifica que estás en el laboratorio y que el archivo no existe antes de continuar. Si ya existe, revísalo y edítalo con Vim o conserva una copia.

## 28. Crear `.gitignore` de práctica

```bash
cat > .gitignore <<'EOF'
*.log
tmp/
.env
EOF
```

Después:

```bash
git status
```

## 29. Probar que `.gitignore` funciona

```bash
printf 'registro\n' > prueba.log
mkdir -p tmp
printf 'temporal\n' > tmp/dato.txt
```

Después:

```bash
git status
```

`prueba.log` y `tmp/dato.txt` no deberían aparecer como candidatos normales para seguimiento por esos patrones.

## 30. Ver por qué algo está ignorado

Puedes consultar:

```bash
git check-ignore -v prueba.log
```

Esto ayuda a identificar qué patrón de ignore coincidió.

## 31. Revisar antes de `git add .`

`git add .` puede preparar muchos cambios bajo el directorio actual.

Antes de usarlo:

```bash
git status
git diff
```

En este manual preferimos al principio:

```bash
git add archivo_especifico
```

porque obliga a decidir qué entra.

## 32. Si añadiste algo al staging por error

Para sacar un archivo del staging sin borrar el archivo de trabajo:

```bash
git restore --staged archivo
```

Después verifica:

```bash
git status
```

## 33. Cuidado con `git restore` sin `--staged`

```bash
git restore archivo
```

puede reemplazar cambios del working tree con contenido de la fuente de restauración.

Eso puede descartar trabajo no guardado.

Regla:

> Antes de usar `git restore` sobre el working tree, revisa `git status` y `git diff`.

## 34. Comandos destructivos fuera del núcleo

No usamos como rutina en este módulo:

```text
git reset --hard
git clean -fd
git checkout -- archivo
git push --force
git rebase --onto ...
```

Algunos son útiles en contextos concretos, pero pueden descartar trabajo o reescribir historial.

Se estudiarán en el itinerario específico de Git cuando corresponda.

## 35. Configurar identidad de commits

Git necesita una identidad para crear commits.

Consulta primero:

```bash
git config --get user.name
git config --get user.email
```

Si falta, configura solo lo necesario siguiendo tu política de privacidad.

No publiques información personal innecesaria.

## 36. Configuración local vs global

```text
--local  → solo repositorio actual
--global → configuración del usuario
```

Para un laboratorio, una configuración local puede ser suficiente y evita cambiar otros repositorios.

Ejemplo conceptual:

```text
git config --local user.name 'Nombre de práctica'
git config --local user.email 'correo autorizado'
```

No inventes ni publiques una dirección personal si no quieres asociarla a commits.

## 37. Qué es un remoto

Un remoto es una referencia a otro repositorio.

Consulta:

```bash
git remote -v
```

Si no aparece nada, el repositorio de práctica no tiene remoto configurado.

## 38. `origin` no es GitHub por definición

`origin` es solo un nombre convencional de remoto.

Puede apuntar a:

- GitHub;
- otro servidor;
- otra ubicación accesible.

No asumas el destino: verifica `git remote -v`.

## 39. Añadir remoto

Forma general:

```text
git remote add origin URL_DEL_REPOSITORIO
```

Esto modifica la configuración local del repositorio.

Antes de ejecutarlo en una práctica real, verifica:

- propietario;
- nombre del repositorio;
- protocolo;
- URL completa.

## 40. `git push`

Forma típica:

```text
git push -u origin main
```

`push` envía commits locales hacia el remoto.

Antes:

```bash
git status
git log --oneline --decorate -n 5
git remote -v
git branch --show-current
```

Debes saber exactamente qué rama y qué repositorio estás publicando.

## 41. Autenticación a GitHub

GitHub no acepta la contraseña normal de tu cuenta como contraseña Git para operaciones HTTPS.

Según el método configurado, puedes usar:

- Git Credential Manager u otro gestor compatible;
- GitHub CLI;
- token de acceso personal para HTTPS;
- claves SSH.

**Nunca escribas tokens o claves privadas dentro del repositorio.**

## 42. Este proyecto ya usa integración GitHub

Durante la construcción de este manual, el tutor guarda cada módulo en el repositorio:

```text
budoninja010-hub/aprendizaje-programacion-ciberseguridad
```

Este Módulo 33 formaliza cómo podrás entender y ejecutar tú mismo ese flujo.

## 43. Flujo seguro para tus ejercicios

Para cada práctica con valor de aprendizaje:

```text
1. crear/corregir ejercicio
2. revisar código
3. comprobar que no contiene secretos
4. git status
5. git diff
6. git add archivo concreto
7. git diff --staged
8. git status
9. git commit -m 'mensaje claro'
10. verificar remoto/rama
11. git push cuando corresponda
```

## 44. Ejemplos de mensajes de commit

```text
python: ejercicio de variables y print
java: práctica de clases y objetos
linux: práctica de permisos
linux: ejercicio de funciones Bash
cybersecurity: laboratorio defensivo de análisis de logs
```

El mensaje debe explicar qué aprendiste o qué cambió.

## 45. No sobrescribir aprendizaje anterior

Si corriges un ejercicio:

```text
commit 1 → versión inicial / WIP
commit 2 → corrección
```

Así conservas el historial.

No reemplaces silenciosamente el aprendizaje anterior si el historial tiene valor.

## 46. Archivo en progreso

Un ejercicio incompleto puede guardarse si tiene valor pedagógico.

Mensaje posible:

```text
linux: WIP práctica de bucles
```

Después:

```text
linux: corrige práctica de bucles y quoting
```

## 47. Revisar un commit después de crearlo

```bash
git show --stat --oneline HEAD
```

Para revisar contenido:

```bash
git show HEAD
```

Confirma que no se haya colado un archivo inesperado.

## 48. Revisar archivos rastreados

```bash
git ls-files
```

Esto ayuda a responder:

```text
¿qué archivos están bajo seguimiento?
```

## 49. Diferencia entre no rastreado e ignorado

```text
untracked → Git lo ve pero todavía no está en historial
ignored   → una regla indica que normalmente no debe añadirse
tracked   → Git ya lo sigue
```

Son estados diferentes.

## 50. Git no es una copia de seguridad universal

Git es excelente para archivos de texto y proyectos versionables.

No reemplaza automáticamente:

- backup del sistema;
- copias de discos;
- snapshots;
- almacenamiento de grandes binarios;
- protección frente a secretos ya filtrados.

## 51. GitHub tampoco debe ser un almacén de secretos

Un repositorio privado reduce exposición pública, pero no convierte las credenciales en contenido apropiado para versionar.

Los secretos deben gestionarse con mecanismos específicos.

Si un secreto real ya llegó al repositorio:

```text
repositorio privado ≠ credencial segura
borrar en el commit siguiente ≠ credencial revocada
.gitignore ≠ limpieza del historial
```

La primera acción de seguridad es invalidar o rotar la credencial con el proveedor correspondiente.

## 52. Práctica A — estado y primer commit

Dentro de `~/linux-lab/modulo-33-git`:

```bash
git status
git add hola.sh
git diff --staged
git commit -m 'linux: primer script Bash versionado'
git log --oneline --decorate
```

Explica qué cambió en cada etapa.

## 53. Práctica B — segundo commit pequeño

Modifica `hola.sh`.

Después:

```bash
git status
git diff
git add hola.sh
git diff --staged
git commit -m 'linux: amplía práctica de printf'
```

## 54. Práctica C — `.gitignore`

```bash
git add .gitignore
git diff --staged
git commit -m 'git: agrega exclusiones de laboratorio'
```

Después comprueba:

```bash
git check-ignore -v prueba.log
```

## 55. Práctica D — sacar algo del staging

Modifica dos archivos de práctica.

Prepara ambos:

```bash
git add hola.sh .gitignore
```

Después saca solo uno:

```bash
git restore --staged .gitignore
git status
```

Verifica que `.gitignore` siga existiendo en tu working tree.

## 56. Práctica E — auditoría antes de publicar

Ejecuta:

```bash
git status
git diff
git diff --staged
git ls-files
git remote -v
git branch --show-current
```

Responde antes de cualquier push:

```text
¿qué cambios publicaré?
¿hay secretos?
¿qué rama uso?
¿qué remoto es?
¿el repositorio es el correcto?
```

## 57. Errores frecuentes

| Error | Problema | Corrección |
|---|---|---|
| `git add .` sin revisar | puedes preparar archivos inesperados | `status`/`diff` y archivos concretos |
| commit sin `diff --staged` | no sabes exactamente qué entra | revisar staged antes |
| subir `.env` | posible exposición de secretos | ignorar y gestionar secretos fuera de Git |
| creer que borrar el secreto en un commit nuevo lo invalida | la credencial puede seguir activa y existir en historial | revocar/rotar primero; después limpiar código/historial |
| creer que `.gitignore` elimina un archivo ya rastreado | no afecta automáticamente a tracked ni borra historial | corregir seguimiento y evaluar saneamiento histórico |
| confundir commit con push | son etapas distintas | commit local, push remoto |
| asumir que `origin` es correcto | puede apuntar a otro destino | `git remote -v` |
| usar `git restore archivo` sin revisar | puede descartar cambios | `status` + `diff` primero |
| usar `reset --hard` para «arreglar todo» | puede destruir trabajo | no usar en este nivel |
| `push --force` por rutina | puede reescribir historial remoto | posponer hasta dominar consecuencias |
| commits gigantes | dificultan revisión/aprendizaje | commits pequeños y temáticos |

## 58. Detección de error 1

Analiza:

```bash
git add .
git commit -m 'cosas'
```

Problemas:

- no se revisó estado;
- no se revisó diferencia;
- no se comprobó contenido staged;
- mensaje poco informativo.

Mejor flujo:

```bash
git status
git diff
git add archivo_concreto
git diff --staged
git commit -m 'linux: describe el cambio real'
```

## 59. Detección de error 2

Analiza un repositorio que contiene:

```text
.env
token.txt
id_rsa
```

Antes de cualquier `git add`, detén el flujo.

Esos nombres pueden indicar secretos o credenciales.

No deben subirse.

Si una credencial real ya hubiera sido confirmada o publicada, el procedimiento cambia:

```text
detener → revocar/rotar → retirar del código → evaluar limpieza de historial
```

No intentes “solucionarlo” únicamente agregando el archivo a `.gitignore`.

## 60. Detección de error 3

Analiza:

```bash
git push origin main
```

sin revisar el remoto.

Primer paso correcto:

```bash
git remote -v
git branch --show-current
```

Después confirma el repositorio y la rama.

## 61. Práctica independiente

Crea `estado_sistema.sh` dentro de un repositorio de laboratorio.

Debe:

1. usar Bash;
2. mostrar solo información no sensible como `uname -s` y `pwd` del laboratorio;
3. pasar `bash -n`;
4. pasar ShellCheck si está disponible;
5. tener un `.gitignore` razonable;
6. ejecutar `git status` antes de preparar cambios;
7. revisar `git diff`;
8. añadir solo los archivos necesarios;
9. revisar `git diff --staged`;
10. crear un commit con mensaje claro;
11. no contener secretos ni datos personales;
12. explicar qué cambiaría antes de un eventual push.

## 62. Mini evaluación

1. ¿Git y GitHub son exactamente lo mismo? A) Sí B) No
2. ¿`git status` muestra estado del working tree/index? A) Sí B) No
3. ¿`git add` prepara contenido para el próximo commit? A) Sí B) No
4. ¿un commit publica automáticamente en GitHub? A) Sí B) No
5. ¿`git diff` y `git diff --staged` comparan lo mismo? A) Sí B) No
6. ¿debes revisar `git diff --staged` antes del commit? A) Sí B) No
7. ¿`.gitignore` afecta automáticamente archivos ya rastreados? A) Sí B) No
8. ¿un token debe subirse si el repositorio es privado? A) Sí B) No
9. Si una credencial real ya fue publicada, ¿la primera prioridad es revocarla o rotarla? A) Sí B) No
10. ¿añadir un secreto ya publicado a `.gitignore` invalida esa credencial? A) Sí B) No
11. ¿reescribir historial puede afectar commits, ramas, PRs y clones? A) Sí B) No
12. ¿`git restore --staged` puede sacar un archivo del staging? A) Sí B) No
13. ¿`git restore archivo` puede descartar cambios del working tree? A) Sí B) No
14. ¿`origin` garantiza que el remoto sea GitHub correcto? A) Sí B) No
15. ¿debes revisar `git remote -v` antes de un push importante? A) Sí B) No
16. ¿los commits pequeños facilitan revisión? A) Sí B) No
17. ¿Git reemplaza todos los tipos de backup? A) Sí B) No
18. ¿este módulo sustituye el itinerario completo de Git/GitHub? A) Sí B) No

## 63. Registro de aprendizaje

```text
Git es:
GitHub es:
Working tree significa:
Staging area significa:
`git status` sirve para:
`git diff` muestra:
`git diff --staged` muestra:
`git add` hace:
`git commit` hace:
`git push` hace:
`.gitignore` sirve para:
¿qué no hace `.gitignore`?:
`git restore --staged` sirve para:
¿por qué reviso el remoto antes de push?:
Regla de secretos:
Si un secreto ya fue publicado, primero debo:
¿Por qué `.gitignore` no resuelve una exposición pasada?:
¿Por qué reescribir historial requiere coordinación?:
Algo que todavía confundo:
Estado: EN APRENDIZAJE / PRACTICADO
```

## 64. Puerta de dominio

Para considerar este módulo **DOMINADO** deberás poder en más de una práctica:

1. explicar Git vs GitHub;
2. distinguir working tree, index y commit;
3. revisar cambios antes de prepararlos;
4. preparar solo archivos elegidos;
5. revisar staged antes de commit;
6. crear un commit claro sin copiar el mensaje;
7. detectar un archivo que no debe subirse;
8. explicar qué hacer si una credencial real ya fue expuesta;
9. distinguir revocar/rotar una credencial de limpiar historial Git;
10. verificar rama y remoto antes de push;
11. explicar por qué un repositorio privado tampoco debe contener secretos.

## 65. Enlace al itinerario específico de Git

Este módulo cubre únicamente la autonomía mínima necesaria para tus scripts Linux.

El itinerario específico de Git/GitHub profundiza en:

- modelo de objetos de Git;
- ramas;
- merge;
- conflictos;
- rebase;
- tags;
- remotos avanzados;
- pull requests;
- estrategias de colaboración;
- reflog;
- reset/restore/revert con más detalle;
- GitHub Actions;
- GitOps y su Apéndice B específico.

No adelantes esos temas aquí si todavía no corresponden en el itinerario de Git.

## 66. Fuentes y límites

Clasificación y estado de los enlaces de esta sección: [catálogo de fuentes](06-catalogo-fuentes.md) (jerarquía E04, comprobación del 9 de octubre de 2026).

Fuentes principales:

- Git — `git status`: https://git-scm.com/docs/git-status
- Git — `git add`: https://git-scm.com/docs/git-add
- Git — `git commit`: https://git-scm.com/docs/git-commit
- Git — `git restore`: https://git-scm.com/docs/git-restore
- Git — `.gitignore`: https://git-scm.com/docs/gitignore
- GitHub Docs — Adding locally hosted code to GitHub: https://docs.github.com/en/migrations/importing-source-code/using-the-command-line-to-import-source-code/adding-locally-hosted-code-to-github
- GitHub Docs — Personal access tokens: https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens
- GitHub Docs — Removing sensitive data from a repository: https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository
- GitHub Docs — Remediating a leaked secret: https://docs.github.com/en/code-security/tutorials/remediate-leaked-secrets/remediating-a-leaked-secret
- GitHub Docs — Push protection: https://docs.github.com/en/code-security/concepts/secret-security/push-protection

Puntos verificados documentalmente:

- `git status` distingue cambios entre HEAD, index y working tree y muestra archivos no rastreados;
- `git add` añade al index el contenido que existe en el momento de ejecutar el comando;
- `git commit` crea un commit con el contenido actual del index;
- `git restore --staged` puede restaurar contenido del index desde HEAD;
- `git restore` sobre el working tree puede reemplazar contenido local;
- `.gitignore` especifica archivos intencionalmente no rastreados y no afecta automáticamente archivos ya rastreados;
- GitHub advierte que nunca deben añadirse, confirmarse o subirse contraseñas, API keys u otra información sensible;
- si una credencial real ya fue expuesta, GitHub recomienda revocarla o rotarla como primera medida; retirar texto del repositorio no invalida por sí solo la credencial;
- reescribir historial puede cambiar hashes, afectar colaboradores y permitir recontaminación desde clones o ramas antiguas, por lo que requiere coordinación;
- push protection puede bloquear pushes que contienen secretos compatibles con sus detectores, pero no sustituye la revisión humana;
- un repositorio local puede conectarse a GitHub mediante un remoto y posteriormente publicarse con `git push` tras autenticación.

Se posponen al itinerario específico:

- `git reset` en profundidad;
- `git clean`;
- rebase;
- cherry-pick;
- reflog;
- force push;
- resolución avanzada de conflictos;
- hooks;
- submodules/subtrees;
- firma de commits;
- Git LFS;
- GitHub Actions;
- estrategias de ramas y GitOps en profundidad.

**Estado de la lección:** redactada y revisada documentalmente contra Git y GitHub Docs. El flujo pedagógico exige revisar diferencias, excluir secretos y confirmar remoto/rama antes de publicar.

---

**Siguiente:** [Módulo 34 — Almacenamiento: `lsblk`, `df`, `du`, montaje y `fstab`](modulo-34-almacenamiento-lsblk-df-du-montaje-fstab.md) · [Volver al índice](README.md)
