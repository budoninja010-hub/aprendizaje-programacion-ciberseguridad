# Manual Maestro de Linux y Shell Scripting — Edición 2026 — Base Auditada v2

PROPÓSITO DEL MANUAL
Este manual está diseñado para aprender Linux desde cero, paso a paso y sin asumir conocimientos previos. La meta no es memorizar comandos, sino entender qué hace cada comando, cuándo usarlo, qué riesgos tiene y cómo comprobar el resultado.

REGLA DE APRENDIZAJE
Cada tema seguirá esta secuencia: qué es, para qué sirve, cómo se usa, ejemplo pequeño, explicación, errores típicos, ejercicio y mini evaluación. No se considera dominado un tema por una sola respuesta correcta.

REGLA DE SEGURIDAD
Las prácticas se realizarán en una máquina propia, una máquina virtual o un laboratorio expresamente autorizado. Antes de usar comandos que borren, sobrescriban, cambien permisos, modifiquen usuarios, alteren red o requieran sudo, se explicará el efecto y cómo verificar la ruta o el objetivo.

MÓDULO 0 — QUÉ ES GNU/LINUX Y CÓMO PENSAR EN ÉL

OBJETIVO
Entender qué es Linux, qué es GNU, qué es una distribución y por qué existen distintas familias de sistemas.

QUÉ ES
Linux es el núcleo o kernel que coordina recursos como CPU, memoria, dispositivos y procesos. Un sistema GNU/Linux combina el kernel Linux con herramientas, bibliotecas y utilidades que permiten trabajar con el sistema.

Una distribución reúne kernel, herramientas, instalador, gestor de paquetes, configuración y repositorios. Ubuntu y Debian pertenecen a una familia; Fedora y Red Hat Enterprise Linux pertenecen a otra. Los comandos básicos de navegación son muy parecidos, pero la instalación de paquetes y algunos servicios pueden cambiar.

PARA QUÉ SIRVE
Linux se usa en servidores, computadoras personales, nube, contenedores, dispositivos integrados, desarrollo de software y administración de sistemas.

CONCEPTO CLAVE
No existe un único “Linux” con una sola interfaz. Debes aprender primero los conceptos comunes y después reconocer las diferencias de cada distribución.

ERROR TÍPICO
Copiar un comando de Ubuntu y asumir que funcionará igual en Red Hat. La idea puede ser correcta, pero el gestor de paquetes o el nombre del servicio puede ser diferente.

EJERCICIO
Explica con tus palabras la diferencia entre kernel, distribución y shell.

MINI EVALUACIÓN
Pregunta: ¿Ubuntu y Red Hat son el mismo sistema?
Respuesta esperada: No. Son distribuciones diferentes de la familia GNU/Linux y comparten muchos conceptos, pero pueden usar herramientas distintas.

MÓDULO 1 — TERMINAL, CLI Y SHELL

OBJETIVO
Distinguir terminal, CLI y shell, y aprender los primeros comandos sin modificar el sistema.

QUÉ ES
La terminal es la aplicación donde escribes comandos. La CLI es la forma de interactuar mediante texto. La shell es el programa que interpreta lo que escribes. Bash es una shell muy utilizada en GNU/Linux.

PRIMEROS COMANDOS
pwd
Muestra el directorio actual. Piensa en él como tu GPS.

ls
Muestra el contenido del directorio actual.

ls -la
Muestra información detallada e incluye elementos ocultos.

whoami
Muestra el usuario con el que estás trabajando.

clear
Limpia la pantalla visualmente. No borra archivos.

man ls
Abre el manual del comando ls, si las páginas de manual están instaladas.

EJEMPLO PASO A PASO
Paso 1: escribe pwd.
Paso 2: observa la ruta.
Paso 3: escribe ls.
Paso 4: identifica uno o dos nombres que aparezcan.
Paso 5: escribe whoami.
Paso 6: no cambies nada todavía.

ERRORES TÍPICOS
Linux distingue mayúsculas y minúsculas. Documento.txt y documento.txt pueden ser archivos diferentes.
No debes asumir que el símbolo $ o # forma parte del comando cuando aparece en documentación.
Si un comando devuelve “command not found”, primero revisa ortografía y distribución antes de instalar cosas.

EJERCICIO
Ejecuta pwd, ls y whoami. Después explica qué información te dio cada uno.

MINI EVALUACIÓN
Pregunta: ¿pwd modifica archivos?
Respuesta esperada: No. Solo informa la ubicación actual.

MÓDULO 2 — SISTEMA DE ARCHIVOS Y NAVEGACIÓN

OBJETIVO
Moverte con seguridad por directorios y entender rutas absolutas y relativas.

CONCEPTOS
/ representa la raíz del sistema.
/home suele contener directorios personales de usuarios.
/etc contiene gran parte de la configuración del sistema.
/var almacena datos variables, como ciertos registros y colas.
/tmp se usa para archivos temporales.
/usr contiene muchos programas, bibliotecas y recursos compartidos.

No memorices toda la jerarquía todavía. Primero aprende a navegar.

COMANDO cd
cd nombre
Entra a un subdirectorio.

cd ..
Sube un nivel.

cd ~
Va a tu directorio personal.

cd -
En Bash suele volver al directorio anterior.

RUTA ABSOLUTA
Empieza desde la raíz. Ejemplo:
/home/alumno/practicas

RUTA RELATIVA
Se interpreta desde tu ubicación actual. Ejemplo:
practicas
o
../practicas

EJEMPLO PASO A PASO
Crea únicamente una carpeta de práctica dentro de tu directorio personal:
mkdir -p ~/linux-lab
cd ~/linux-lab
pwd

mkdir crea directorios. La opción -p permite crear la ruta indicada sin fallar si los directorios superiores necesarios deben crearse.

REGLA DE SEGURIDAD
Antes de cualquier comando que modifique archivos, ejecuta pwd y confirma que estás dentro de ~/linux-lab o de otra carpeta creada específicamente para la práctica.

EJERCICIO
Dentro de ~/linux-lab crea una carpeta llamada modulo2 y entra en ella. Regresa después a ~/linux-lab usando cd ...

MINI EVALUACIÓN
Pregunta: ¿qué diferencia existe entre /home/alumno y home/alumno?
Respuesta esperada: La primera es una ruta absoluta; la segunda es relativa a la ubicación actual.

MÓDULO 3 — CREAR, COPIAR, MOVER Y BORRAR ARCHIVOS

OBJETIVO
Manipular archivos y directorios dentro del laboratorio sin trabajar a ciegas.

COMANDOS BÁSICOS
touch notas.txt
Crea un archivo vacío si no existe o actualiza su marca de tiempo si ya existe.

mkdir ejercicios
Crea un directorio.

cp notas.txt copia-notas.txt
Copia un archivo.

mv copia-notas.txt notas-respaldo.txt
Mueve o renombra un archivo.

rm notas-respaldo.txt
Borra un archivo.

rmdir ejercicios
Elimina un directorio únicamente si está vacío.

ADVERTENCIA IMPORTANTE
rm elimina archivos sin enviarlos necesariamente a una papelera. Antes de usarlo, verifica pwd y ls.

COMANDO DE ALTO RIESGO
rm -rf combina borrado recursivo con supresión de varias confirmaciones. No lo utilizaremos como comando rutinario de principiante. Solo se estudiará más adelante dentro de un laboratorio controlado y después de aprender a verificar rutas.

EJEMPLO SEGURO
cd ~/linux-lab
mkdir modulo3
cd modulo3
touch original.txt
cp original.txt copia.txt
ls -l
mv copia.txt respaldo.txt
ls -l
rm respaldo.txt
ls -l

ERRORES TÍPICOS
Ejecutar rm desde el directorio equivocado.
Confundir mv con cp: mv no crea una copia adicional; mueve o cambia el nombre.
Sobrescribir un archivo con cp o mv sin comprobar si el destino ya existe.

EJERCICIO
Crea archivo1.txt, cópialo como archivo2.txt y renombra la copia como respaldo.txt. No borres el original.

MINI EVALUACIÓN
Pregunta: ¿qué comando usarías para ver dónde estás antes de borrar algo?
Respuesta esperada: pwd.

MÓDULO 4 — LEER TEXTO, REDIRECCIONES Y TUBERÍAS

OBJETIVO
Comprender entrada, salida y composición de comandos.

LECTURA DE ARCHIVOS
cat archivo.txt
Muestra el contenido completo y es cómodo para archivos pequeños.

less archivo.txt
Permite navegar por contenido más largo.

head archivo.txt
Muestra las primeras líneas.

tail archivo.txt
Muestra las últimas líneas.

REDIRECCIÓN
echo "hola" > saludo.txt
Escribe la salida en saludo.txt y puede sobrescribir el contenido anterior.

echo "otra línea" >> saludo.txt
Agrega contenido al final.

REGLA DE SEGURIDAD
El operador > puede sobrescribir un archivo existente. Antes de usarlo sobre un archivo importante, revisa el nombre y considera crear una copia.

TUBERÍA
Una tubería conecta la salida de un comando con la entrada de otro:
printf "uno\ndos\ntres\n" | grep "dos"

Aquí printf produce texto y grep conserva las líneas que coinciden con el patrón.

CONCEPTO CLAVE
Una tubería no significa “guardar en un archivo”. Para guardar se utiliza una redirección u otra herramienta apropiada.

EJERCICIO
Dentro de ~/linux-lab crea colores.txt con tres líneas usando printf. Después usa grep para localizar una de ellas.

MINI EVALUACIÓN
Pregunta: ¿qué diferencia hay entre > y >>?
Respuesta esperada: > reemplaza la salida del archivo destino; >> agrega al final.

MÓDULO 5 — BÚSQUEDA CON grep, find Y locate

OBJETIVO
Buscar texto y archivos sin recorrer manualmente todo el sistema.

grep
Busca patrones dentro del texto.

Ejemplos:
grep "error" registro.txt
grep -i "error" registro.txt
grep -n "error" registro.txt

-i ignora diferencias entre mayúsculas y minúsculas.
-n muestra número de línea.

find
Busca archivos y directorios recorriendo una ruta real.

Ejemplos seguros dentro del laboratorio:
find ~/linux-lab -type f
find ~/linux-lab -type f -name "*.txt"
find ~/linux-lab -type d

locate
Puede buscar usando una base de datos indexada y normalmente es muy rápido, pero puede no estar instalado y su índice puede no reflejar archivos creados hace pocos segundos. Por eso no debe confundirse con find.

ERROR TÍPICO
Decir que locate y find hacen exactamente lo mismo. locate consulta un índice; find recorre rutas según criterios.

EJERCICIO
Crea tres archivos .txt en subdirectorios distintos de ~/linux-lab y encuentra los tres con find.

MINI EVALUACIÓN
Pregunta: si acabas de crear un archivo y quieres una búsqueda fiable por ruta, ¿qué herramienta básica usarías?
Respuesta esperada: find.

MÓDULO 6 — USUARIOS, GRUPOS Y PERMISOS

OBJETIVO
Entender identidad, propiedad y permisos antes de modificarlos.

IDENTIDAD
whoami muestra el usuario actual.
id muestra UID, GID y grupos asociados.

ARCHIVOS IMPORTANTES
/etc/passwd contiene información de cuentas y parámetros básicos.
/etc/group contiene información de grupos.
/etc/shadow contiene hashes de contraseñas y datos relacionados con expiración; normalmente requiere privilegios para su lectura.

PERMISOS
ls -l archivo.txt puede mostrar algo parecido a:
-rw-r--r--

El primer carácter indica el tipo de objeto. Después aparecen tres grupos de permisos: propietario, grupo y otros.

r significa lectura.
w significa escritura.
x significa ejecución en archivos; en directorios está relacionado con poder atravesar o acceder a entradas según los demás permisos.

chmod
Cambia permisos.

Ejemplo dentro del laboratorio:
chmod u+x script.sh

Modo octal:
r = 4
w = 2
x = 1

Un permiso como 754 representa:
propietario 7 = rwx
grupo 5 = r-x
otros 4 = r--

UMASK
umask no debe enseñarse simplemente como “restar números”. Conceptualmente, establece bits de permisos que se eliminan de los permisos base al crear archivos y directorios.

PROPIEDAD
chown puede cambiar propietario y grupo y suele requerir privilegios. No lo utilizaremos hasta trabajar administración con una máquina virtual preparada para ello.

sudo
sudo permite ejecutar un comando con privilegios elevados según la configuración del sistema. No significa “modo administrador permanente” y no debe anteponerse automáticamente a todos los comandos.

EJERCICIO
Dentro de ~/linux-lab crea practica.sh, ejecuta ls -l, añade permiso de ejecución solo al propietario con chmod u+x y vuelve a revisar ls -l.

MINI EVALUACIÓN
Pregunta: en rwxr-xr--, ¿qué puede hacer “otros”?
Respuesta esperada: leer, pero no escribir ni ejecutar.

MÓDULO 7 — PROCESOS, TRABAJOS Y SEÑALES

OBJETIVO
Observar procesos y comprender cómo solicitar que terminen.

ps
Muestra información de procesos.

ps aux
Forma habitual de ver una lista amplia en sistemas GNU/Linux.

top
Muestra procesos y uso de recursos de forma interactiva.

jobs
Muestra trabajos asociados a la shell actual.

Ctrl+Z
Suspende normalmente el trabajo en foreground.

bg
Continúa un trabajo suspendido en background cuando el programa y la terminal lo permiten.

fg
Lleva un trabajo al foreground.

SEÑALES Y kill
kill PID envía por defecto una señal de terminación, normalmente SIGTERM, que permite al proceso reaccionar y cerrar de manera ordenada.

kill -9 PID envía SIGKILL. Esa señal no puede ser manejada ni ignorada por el proceso. Debe reservarse para casos en los que una terminación normal no funciona.

REGLA
Primero identifica correctamente el proceso. Después intenta una terminación normal. SIGKILL no es el primer paso.

EJERCICIO SEGURO
Abre una segunda terminal, ejecuta sleep 300, localiza el proceso y termina únicamente ese proceso con una señal normal.

MINI EVALUACIÓN
Pregunta: ¿por qué no debemos empezar siempre con kill -9?
Respuesta esperada: porque impide al proceso manejar la terminación de forma normal y puede dejar trabajo o estado sin cerrar correctamente.

MÓDULO 8 — PAQUETES Y ACTUALIZACIONES

OBJETIVO
Entender que la instalación de software depende de la familia de distribución.

DEBIAN Y UBUNTU
apt es una herramienta común para gestionar paquetes.

Ejemplo informativo:
apt search nombre-paquete

Instalar, actualizar o eliminar paquetes modifica el sistema y puede requerir sudo. Lo haremos únicamente cuando la práctica lo requiera.

FEDORA Y RED HAT
dnf es una herramienta común en sistemas modernos de esta familia.

Ejemplo informativo:
dnf search nombre-paquete

CONCEPTO CLAVE
No copies instrucciones de apt en un sistema que utiliza dnf. Primero identifica la distribución:
cat /etc/os-release

REGLA DE SEGURIDAD
Antes de instalar o eliminar paquetes, verifica qué sistema estás usando y qué paquete será afectado.

EJERCICIO
Ejecuta cat /etc/os-release y anota el nombre de tu distribución. No instales nada todavía.

MÓDULO 9 — RED BÁSICA Y SSH

OBJETIVO
Reconocer interfaces, direcciones, conectividad y el propósito de SSH.

ip addr
Muestra interfaces y direcciones IP.

ip route
Muestra rutas de red.

ping
Envía solicitudes ICMP para comprobar conectividad cuando el destino y la red lo permiten.

ss
Permite inspeccionar sockets y conexiones.

SSH
SSH permite una conexión cifrada a otro sistema que administra el usuario o para el que tiene autorización.

Cliente básico:
ssh usuario@servidor

No practicaremos acceso a sistemas ajenos. Las pruebas deben limitarse a máquinas propias, máquinas virtuales, laboratorios o servicios expresamente autorizados.

CLAVES SSH
Las claves privadas son secretos. Nunca deben subirse a GitHub, pegarse en documentos públicos ni compartirse.

EJERCICIO
En tu propia máquina ejecuta ip addr e identifica el nombre de una interfaz. Después ejecuta ip route y localiza la ruta por defecto si existe.

MINI EVALUACIÓN
Pregunta: ¿qué dato nunca debe subirse al repositorio?
Respuesta esperada: una clave SSH privada, contraseñas, tokens u otras credenciales.

MÓDULO 10 — FIREWALL UFW EN UBUNTU

OBJETIVO
Entender el propósito de un firewall de host antes de cambiar reglas.

QUÉ ES
Ubuntu utiliza UFW como una interfaz sencilla para administrar reglas de firewall de host. Puede gestionar reglas sobre la infraestructura de filtrado del kernel.

COMANDOS DE INSPECCIÓN
sudo ufw status
sudo ufw status verbose

Estos comandos consultan el estado, aunque sudo puede solicitar autenticación.

ADVERTENCIA
Activar un firewall o cambiar reglas puede cortar conectividad. En un servidor remoto, nunca debes habilitar reglas sin confirmar primero cómo conservarás el acceso autorizado.

EJEMPLO CONCEPTUAL
Si administras tu propio servidor por SSH, la documentación de Ubuntu muestra que pueden existir reglas para permitir el servicio SSH antes de habilitar otras restricciones. La práctica concreta se realizará solo en una máquina virtual o servidor propio.

EJERCICIO
En una máquina Ubuntu propia, limita la práctica a consultar el estado de UFW. No habilites ni modifiques reglas hasta revisar el laboratorio correspondiente.

MÓDULO 11 — vi Y Vim DESDE CERO

OBJETIVO
Editar un archivo pequeño sin quedar atrapado dentro del editor.

MODOS BÁSICOS
Modo normal: interpreta teclas como comandos.
Modo inserción: permite escribir texto.
Modo de comandos con dos puntos: permite guardar, salir y ejecutar otras órdenes del editor.

SECUENCIA MÍNIMA
vim notas.txt
Pulsa i para entrar en inserción.
Escribe una línea.
Pulsa Esc.
Escribe :w y Enter para guardar.
Escribe :q y Enter para salir.

ATAJOS INICIALES
i entra en inserción.
Esc vuelve al modo normal.
yy copia una línea.
dd elimina y guarda la línea en un registro interno para posible pegado.
p pega después o debajo de la posición correspondiente.
u deshace.
/palabra busca hacia adelante.
:w guarda.
:q sale si no hay cambios pendientes.
:wq guarda y sale.
:q! sale descartando cambios no guardados.

ADVERTENCIA
:q! descarta cambios no guardados. Antes de usarlo debes saber que perderás esas ediciones.

NUMERACIÓN DE LÍNEAS
Dentro de Vim:
:set number
Para desactivarla:
:set nonumber

EJERCICIO
Crea ~/linux-lab/vim-practica.txt, escribe tres líneas, activa números de línea y guarda correctamente.

MÓDULO 12 — BASH SCRIPTING DESDE CERO

OBJETIVO
Crear scripts pequeños, comprender cada línea y avanzar de variables a lógica.

PRIMER SCRIPT
Crea dentro de ~/linux-lab un archivo hola.sh con:

#!/usr/bin/env bash
echo "Hola desde Bash"

EXPLICACIÓN LÍNEA POR LÍNEA
#!/usr/bin/env bash solicita localizar Bash mediante env y usarlo como intérprete.
echo muestra texto.

EJECUCIÓN
Puedes ejecutarlo explícitamente con:
bash hola.sh

Más adelante puedes darle permiso de ejecución:
chmod u+x hola.sh
./hola.sh

VARIABLES
nombre="Hugo"
echo "Hola $nombre"

No debe haber espacios alrededor del signo = en una asignación básica.

ENTRADA
read -r -p "Escribe tu nombre: " nombre
echo "Hola $nombre"

-r evita que read interprete barras invertidas de manera especial.

ARGUMENTOS
$0 representa cómo se invocó el script.
$1 representa el primer argumento.
$# representa el número de argumentos.
"$@" representa todos los argumentos preservando sus límites cuando se cita correctamente.

ARITMÉTICA
a=5
b=3
suma=$((a + b))
echo "$suma"

CONDICIONALES
numero=10
if (( numero > 5 )); then
    echo "Es mayor que 5"
else
    echo "Es 5 o menor"
fi

BUCLE for
for numero in 1 2 3
do
    echo "$numero"
done

BUCLE while
contador=1
while (( contador <= 3 ))
do
    echo "$contador"
    ((contador++))
done

FUNCIONES
saludar() {
    local nombre="$1"
    echo "Hola $nombre"
}

saludar "Linux"

CÓDIGOS DE SALIDA
Por convención, 0 indica éxito y un valor distinto de 0 indica alguna condición no exitosa o error según el programa.

Después de ejecutar un comando:
echo "$?"
muestra el código de salida más reciente.

BUENA PRÁCTICA
Cita variables cuando representen texto o rutas:
"$archivo"
"$directorio"

EJERCICIO
Crea un script que pida un nombre, lo guarde en una variable y muestre un saludo. Después crea una segunda versión que reciba el nombre como primer argumento.

MINI EVALUACIÓN
Pregunta: ¿qué diferencia existe entre ejecutar bash hola.sh y ./hola.sh?
Respuesta esperada: la primera invoca Bash explícitamente; la segunda ejecuta el archivo directamente y depende, entre otras cosas, de permisos de ejecución y de un intérprete definido apropiadamente.

MÓDULO 13 — AUTOMATIZACIÓN CON cron

OBJETIVO
Comprender la programación periódica sin empezar con tareas destructivas.

QUÉ ES
cron es un mecanismo tradicional de planificación de tareas presente en muchos sistemas Unix y GNU/Linux. Su disponibilidad y servicio concreto dependen de la distribución y configuración. En sistemas modernos también existen temporizadores de systemd.

COMANDOS
crontab -l
Lista las tareas del usuario.

crontab -e
Edita las tareas del usuario.

ADVERTENCIA
crontab -r puede eliminar la tabla de cron del usuario. No lo utilizaremos en prácticas iniciales.

FORMATO BÁSICO
minuto hora día-del-mes mes día-de-semana comando

EJEMPLO CONCEPTUAL
30 2 * * * comando
representa una ejecución diaria a las 02:30 según el entorno de cron.

BUENA PRÁCTICA
Antes de programar un comando, ejecútalo manualmente y verifica rutas absolutas, permisos, entorno y destino de la salida.

EJERCICIO
Sin modificar crontab todavía, interpreta estas expresiones:
0 9 * * 1
*/10 * * * *

MÓDULO 14 — PUENTE HACIA GIT

OBJETIVO
Conectar las habilidades de terminal con el aprendizaje de Git.

ANTES DE USAR GIT DEBES PODER
Explicar qué hace pwd.
Moverte con cd.
Listar con ls.
Crear una carpeta de práctica.
Crear y editar un archivo.
Distinguir ruta absoluta y relativa.
Entender que los archivos ocultos empiezan normalmente con punto.
Leer mensajes de error sin ejecutar comandos al azar.

PRIMERA COMPROBACIÓN
git --version
Solo informa la versión instalada si Git está disponible.

No inicia un repositorio ni modifica tu proyecto.

A partir de aquí, Git se estudiará en su propio Manual Maestro de Git y GitHub para no mezclar control de versiones con administración de Linux.

CORRECCIONES APLICADAS AL MATERIAL ANTERIOR

1. El manual anterior comenzaba con permisos y administración de usuarios. Se reordenó para iniciar con terminal, navegación y archivos.
2. Se eliminó la idea de que practicar es el “único” método efectivo. La práctica es esencial, pero el aprendizaje también requiere explicación, recuperación activa, retroalimentación y repetición.
3. Se corrigió la explicación de umask: no se enseña como una simple resta decimal.
4. Se redujo el uso de sudo en ejemplos de principiante.
5. Se sustituyeron ejemplos de búsqueda sobre rutas sensibles por un laboratorio en el directorio personal.
6. Se evita enseñar rm -rf como comando rutinario.
7. Se diferencia SIGTERM de SIGKILL y se reserva SIGKILL para situaciones justificadas.
8. Se distingue locate de find y se advierte que locate depende de un índice.
9. Se separan las familias apt y dnf.
10. Se evita presentar una distribución científica histórica como recomendación vigente.
11. Se añade una regla explícita de no subir claves, contraseñas, tokens ni archivos de secretos a GitHub.
12. Se añade una transición clara desde Linux hacia Git.

RUTA DE APRENDIZAJE

Etapa 1: terminal y navegación.
Etapa 2: archivos, texto y búsquedas.
Etapa 3: usuarios, permisos y procesos.
Etapa 4: paquetes y red básica.
Etapa 5: Vim.
Etapa 6: Bash Scripting.
Etapa 7: automatización.
Etapa 8: Git.
Etapa 9: administración Linux más avanzada.
Etapa 10: laboratorios defensivos de ciberseguridad en entornos propios o autorizados.

CRITERIO PARA AVANZAR
No avanzaremos solo porque un ejercicio salga bien una vez. Antes de pasar de tema debes poder explicar el concepto con tus palabras, resolver un ejercicio parecido sin copiar e identificar al menos un error frecuente.

FUENTES DE REFERENCIA PRINCIPALES

GNU Bash Reference Manual.
https://www.gnu.org/software/bash/manual/

GNU Coreutils.
https://www.gnu.org/software/coreutils/manual/

Ubuntu Server Documentation — Firewall / UFW.
https://ubuntu.com/server/docs/firewalls/

Red Hat Documentation.
https://docs.redhat.com/

OpenSSH Manual Pages.
https://www.openssh.com/manual.html

NOTA EDITORIAL
Esta es una base auditada de aprendizaje. Las prácticas y capítulos se ampliarán con nuevas versiones sin borrar el historial anterior.
