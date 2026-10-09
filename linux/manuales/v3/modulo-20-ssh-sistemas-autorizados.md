# Módulo 20 — SSH en sistemas propios o expresamente autorizados

Manual Maestro de Linux y Shell Scripting — Edición 2026 · v3 · Vigésima entrega.

[Índice del manual](README.md) · [← Módulo 19](modulo-19-redes-ip-dns-rutas-ip-ss.md) · [Arquitectura](00-indice-arquitectura.md) · [Módulo 21 →](modulo-21-firewall-nftables-ufw-firewalld.md)

## 1. Qué aprenderás

Al terminar este módulo podrás:

- explicar qué es SSH y para qué sirve;
- distinguir cliente SSH y servidor SSH;
- reconocer host, usuario y puerto;
- comprender el papel de la host key;
- explicar para qué sirve `~/.ssh/known_hosts`;
- interpretar una primera conexión sin aceptar claves a ciegas;
- distinguir contraseña de autenticación por clave pública;
- distinguir clave pública y clave privada;
- consultar la configuración efectiva del cliente sin conectarte;
- generar, de forma opcional, un par de claves de laboratorio y proteger la clave privada;
- reconocer qué prácticas no deben usarse en sistemas ajenos o sin autorización.

Conocimientos previos:
- IP, DNS, rutas y puertos;
- usuarios y permisos;
- archivos y rutas;
- procesos;
- conceptos básicos de seguridad.

**Alcance autorizado:** SSH se practica únicamente en equipos propios, máquinas virtuales, laboratorios, CTF autorizados o sistemas para los que tengas permiso expreso. El manual sí estudiará, en módulos avanzados, cómo pueden fallar los mecanismos de autenticación, qué configuraciones los debilitan, qué indicadores dejan esos intentos y cómo se detectan y corrigen. Las prácticas ofensivas se limitarán a entornos controlados y autorizados; no se usarán para intentar entrar a equipos ajenos ni para evadir controles en sistemas reales sin permiso.

## 2. Qué es SSH

SSH significa:

```text
Secure Shell
```

Es un protocolo y conjunto de herramientas para comunicación remota cifrada.

Un uso típico es iniciar una sesión de terminal en otro sistema:

```text
cliente SSH ── conexión cifrada ── servidor SSH
```

También puede utilizarse como base para transferencias seguras y otros mecanismos, pero este módulo se limita al acceso remoto básico.

## 3. Cliente y servidor

Dos componentes distintos:

```text
ssh  → cliente
sshd → servidor/daemon
```

El cliente inicia una conexión.

El servidor escucha y decide si permite autenticación según su configuración.

Tener el comando `ssh` instalado **no significa** que tu equipo esté ejecutando un servidor SSH.

## 4. Comprobar el cliente

Consulta:

```bash
command -v ssh
```

Después:

```bash
ssh -V
```

`ssh -V` muestra información de versión del cliente.

No realiza una conexión remota.

## 5. Sintaxis básica

La forma general:

```text
ssh usuario@host
```

Ejemplo conceptual, usando un nombre de laboratorio:

```text
ssh alumno@servidor-lab
```

No copies ese nombre literalmente si no existe.

Tres datos importantes:

- `usuario`: cuenta remota autorizada;
- `host`: nombre DNS o dirección del sistema autorizado;
- puerto: por defecto SSH suele usar TCP 22, aunque puede configurarse otro.

## 6. Puerto

Para un servidor configurado en un puerto distinto:

```text
ssh -p PUERTO usuario@host
```

`-p` del cliente SSH usa **p minúscula**.

No pruebes puertos al azar en sistemas externos.

En este curso el puerto debe provenir de la configuración de tu propio laboratorio o de la información proporcionada por el administrador autorizado.

## 7. Qué ocurre antes de autenticarte

Antes de aceptar tu usuario, el cliente debe identificar al servidor.

El servidor presenta una **host key**.

El cliente puede compararla con una identificación conocida previamente.

Esto ayuda a detectar:

- servidor equivocado;
- suplantación;
- cambios inesperados de clave;
- ciertos ataques de intermediario.

La identidad del servidor y la identidad del usuario son problemas distintos.

## 8. Host key

Una host key identifica criptográficamente al servidor SSH.

No es:

- tu contraseña;
- tu clave privada de usuario;
- la dirección IP;
- un certificado TLS de navegador.

Un servidor puede tener diferentes tipos de host key.

La verificación correcta debe hacerse mediante una huella (*fingerprint*) obtenida por un canal confiable.

## 9. Primera conexión

En una primera conexión a un host no conocido, SSH puede mostrar:

- tipo de clave;
- fingerprint;
- pregunta para confiar en el host.

No respondas `yes` automáticamente.

Primero compara la fingerprint con una fuente confiable, por ejemplo:

- consola local del servidor propio;
- documentación del laboratorio;
- administrador autorizado;
- inventario de infraestructura confiable.

**Procedimiento en un servidor propio o autorizado:** desde su consola confiable, el administrador puede consultar la huella de la clave pública del host con `ssh-keygen -l -f /etc/ssh/ssh_host_ed25519_key.pub`. En el cliente, compara visualmente la huella mostrada por SSH con la obtenida desde esa consola o canal independiente. No copies claves privadas ni aceptes huellas sin verificar.

Una fingerprint desconocida no debe aceptarse solo porque “es la primera vez”.

## 10. known_hosts

OpenSSH mantiene identificaciones de hosts conocidos normalmente en:

```text
~/.ssh/known_hosts
```

Cuando un host ya conocido presenta una clave distinta, el cliente lo advierte. Con la configuración predeterminada (`StrictHostKeyChecking ask`), y también con `yes` o `accept-new`, OpenSSH **se niega a conectar**. Solo si alguien configuró `StrictHostKeyChecking no`, la conexión puede continuar con restricciones, entre ellas la desactivación de la autenticación por contraseña (fuentes: `ssh_config(5)` y `ssh(1)`).

Eso no significa automáticamente un ataque; también puede ocurrir tras:

- reinstalación;
- regeneración de claves;
- cambio de servidor;
- cambio de IP reutilizada.

Pero la advertencia debe investigarse antes de continuar.

## 11. No desactivar StrictHostKeyChecking para “quitar el error”

Opciones que eliminan o debilitan la verificación de host pueden ocultar una advertencia de seguridad.

En este manual no enseñaremos como receta:

```text
StrictHostKeyChecking=no
```

ni prácticas equivalentes para ignorar cambios de host key.

La solución correcta es verificar la identidad del servidor.

## 12. Buscar una entrada conocida

Si ya tienes un host autorizado registrado, puedes consultar:

```bash
ssh-keygen -F NOMBRE_HOST
```

Esto busca el host en `known_hosts`.

No modifica el archivo.

Si no existe una entrada, simplemente puede significar que aún no te has conectado o que el nombre está almacenado de otra forma.

## 13. Configuración efectiva sin conectar

Una práctica especialmente segura:

```bash
ssh -G localhost
```

`-G` hace que el cliente evalúe la configuración efectiva para ese destino y la imprima, sin establecer una sesión remota.

Para limitar la salida:

```bash
ssh -G localhost | head -n 20
```

Puedes observar valores como:

- hostname;
- user;
- port;
- opciones de autenticación.

No modifica el sistema.

## 14. Archivo de configuración del cliente

La configuración del usuario suele estar en:

```text
~/.ssh/config
```

y la configuración general del cliente en:

```text
/etc/ssh/ssh_config
```

No todos los usuarios tienen un `~/.ssh/config`.

En esta lección solo consultamos si existen.

No publiques el archivo completo: puede contener hostnames, usuarios, rutas y nombres internos.

## 15. Autenticación

Después de verificar al servidor, SSH debe autenticar al usuario.

Métodos que OpenSSH puede soportar incluyen, según configuración:

- clave pública;
- password;
- keyboard-interactive;
- otros mecanismos.

Que un método exista en el cliente no significa que el servidor lo permita.

## 16. Autenticación por contraseña

En un entorno autorizado, el servidor puede solicitar una contraseña.

Reglas:

- no escribas la contraseña en el chat;
- no la guardes en scripts;
- no la pases como argumento visible;
- no reutilices credenciales sin autorización;
- no pruebes contraseñas repetidamente.

SSH no convierte una mala práctica de contraseñas en una práctica segura.

## 17. Autenticación por clave pública

Modelo:

```text
usuario conserva clave privada
servidor conoce clave pública autorizada
```

Durante la autenticación, el cliente demuestra que posee la clave privada sin enviarla al servidor como archivo.

La clave privada nunca debe compartirse.

## 18. Clave pública y clave privada

Un par de claves contiene:

```text
clave privada → SECRETA
clave pública → puede distribuirse al sistema autorizado
```

Ejemplos de nombres tradicionales:

```text
id_ed25519      → privada
id_ed25519.pub  → pública
```

No dependas solo del nombre: entiende qué archivo es cuál.

## 19. Regla absoluta: la privada no va a GitHub

Nunca subas a GitHub:

- claves SSH privadas;
- passphrases;
- tokens;
- contraseñas;
- archivos `.env`;
- credenciales.

Si detectamos una clave privada antes de un commit, la subida debe detenerse.

Una clave privada expuesta debe considerarse comprometida y rotarse según el sistema afectado.

## 20. Permisos de ~/.ssh

OpenSSH aplica controles sobre archivos sensibles.

Una clave privada debe ser accesible únicamente según permisos apropiados para el usuario.

No uses:

```text
chmod 777
```

sobre `~/.ssh` o claves.

Como referencia habitual de OpenSSH: `~/.ssh` debe estar restringido al propietario (modo `700`); las claves privadas y `~/.ssh/config` pueden mantenerse en modo `600`. `authorized_keys` también debe estar protegido frente a escritura ajena. Comprueba los permisos con `ls -ld ~/.ssh` y `ls -l ~/.ssh/config` cuando existan. No cambies permisos de archivos reales sin comprender primero M12 y las políticas del equipo.

## 21. Generar una clave de laboratorio — opcional

Esta sección explica el procedimiento; **no lo ejecutes aquí**. La práctica correspondiente es la sección 41 (Práctica E). Si lo ejecutaras dos veces, el segundo `mkdir` fallaría y `ssh-keygen` preguntaría si quieres sobrescribir la clave.

Solo para un ejercicio local, puedes generar un par nuevo **sin reutilizar una clave real**.

Dentro de:

```text
~/linux-lab/modulo-20-ssh/
```

crea una carpeta privada:

```bash
mkdir -m 700 claves-lab
```

Después, de forma opcional:

```bash
ssh-keygen -t ed25519 -f ./claves-lab/lab_ed25519 -C "linux-lab"
```

Cuando pregunte una passphrase, elige una solo para esta clave y **no la compartas**.

Esto crea:

```text
lab_ed25519      → privada
lab_ed25519.pub  → pública
```

**No subas ninguno de esos archivos al repositorio de aprendizaje.** La clave privada está explícitamente prohibida y la pública de laboratorio tampoco aporta valor al repositorio.

## 22. Por qué Ed25519

OpenSSH actual soporta Ed25519 como tipo de clave.

Para este curso es una opción moderna y sencilla para una clave de laboratorio.

No necesitas comparar algoritmos criptográficos en profundidad todavía.

No uses tipos obsoletos solo porque aparezcan en tutoriales antiguos.

## 23. Passphrase de la clave

La passphrase protege el archivo de clave privada si alguien obtiene una copia del archivo.

No es enviada como contraseña al servidor.

Modelo:

```text
passphrase → protege la privada local
clave privada → demuestra identidad
clave pública → registrada en servidor autorizado
```

No confundas estos tres elementos.

## 24. Fingerprint de una clave pública

Sobre la pública de laboratorio:

```bash
ssh-keygen -lf ./claves-lab/lab_ed25519.pub
```

Esto muestra una fingerprint.

La fingerprint es una representación compacta útil para comparar claves.

No revela la clave privada.

## 25. authorized_keys — concepto

En una cuenta remota configurada para autenticación por clave pública, las claves autorizadas suelen almacenarse en un archivo como:

```text
~/.ssh/authorized_keys
```

del usuario remoto.

Agregar una clave a ese archivo **otorga capacidad de autenticación** según la configuración.

Por eso no modificaremos `authorized_keys` en esta lección sin un servidor de laboratorio definido y autorización explícita.

## 26. ssh-copy-id — existe, pero se pospone

`ssh-copy-id` puede facilitar instalar una clave pública en una cuenta remota autorizada.

No se usa en esta lección porque:

- modifica la cuenta remota;
- requiere verificar primero el servidor;
- requiere confirmar qué clave se copia;
- requiere un objetivo autorizado.

Se introducirá solo cuando trabajemos con una VM o servidor propio claramente identificado.

## 27. Conexión a localhost — solo si ya existe sshd

Comprueba:

```bash
ss -lnt
```

y, si usas systemd:

```bash
systemctl status ssh.service
systemctl status ssh.socket
systemctl status sshd.service
```

Comprueba **solo la unidad que exista**: Ubuntu reciente puede activar OpenSSH mediante `ssh.socket`, mientras que RHEL suele utilizar `sshd.service`. Una unidad `ssh.service` inactiva no demuestra por sí sola que el servidor esté apagado. Contrasta con la escucha de puertos mediante `ss -lnt`.

**No instales ni habilites un servidor SSH solo para completar este módulo.**

Si ya tienes un sshd propio configurado y sabes que `localhost` es tu equipo, una conexión local puede ser válida.

Si no, se omite.

## 28. sshd no debe exponerse por accidente

Instalar o habilitar un servidor SSH puede hacer que escuche en una interfaz de red según configuración.

Eso implica decisiones de:

- firewall;
- usuarios;
- autenticación;
- exposición;
- actualizaciones;
- logs;
- políticas de acceso.

Por eso la instalación/configuración del servidor se pospone.

## 29. Root login

El acceso SSH directo como root aumenta el impacto de una credencial comprometida y depende de la política del sistema.

No configuraremos ni recomendaremos habilitar root login en este módulo.

Trabajaremos con cuentas normales y mínimo privilegio.

## 30. Ataques contra autenticación: qué sí estudiaremos

Para aprender ciberseguridad de forma completa, el manual sí abordará más adelante, dentro de laboratorios propios o CTF autorizados:

- qué es fuerza bruta y por qué funciona cuando existen credenciales débiles;
- qué es password spraying a nivel conceptual;
- qué configuraciones de SSH aumentan el riesgo;
- qué registros e indicadores dejan los intentos de autenticación fallidos;
- cómo detectar patrones anómalos;
- cómo aplicar bloqueo, MFA, claves, políticas de contraseña y mínimo privilegio;
- cómo revisar y corregir una configuración vulnerable.

La finalidad será comprender **el mecanismo de fallo, la detección y la mitigación**.

No se incluirán procedimientos operativos destinados a vulnerar sistemas reales sin autorización ni automatizaciones reutilizables contra terceros.

## 31. Ejecutar un comando remoto

SSH puede ejecutar un comando en un host autorizado:

```text
ssh usuario@host comando
```

Pero todavía no lo practicaremos.

Primero debes dominar:

- identidad del servidor;
- autenticación;
- permisos;
- salida remota;
- diferencias entre shell local y remota.

## 32. SCP y SFTP

OpenSSH incluye herramientas como:

```text
scp
sftp
```

para transferencia de archivos.

No se desarrollan en este módulo para no mezclar acceso remoto con transferencia.

Se introducirán después de que puedas identificar claramente origen, destino y permisos.

## 33. Agente SSH

`ssh-agent` puede mantener claves cargadas en memoria para evitar reintroducir passphrases repetidamente.

Eso implica decisiones adicionales de seguridad de sesión.

No lo configuraremos aún.

Nunca copies variables, sockets o material sensible a repositorios.

## 34. Archivo known_hosts cambiado

Si SSH avisa que la host key cambió:

1. detén la conexión;
2. identifica el host;
3. confirma si hubo reinstalación/cambio legítimo;
4. compara la nueva fingerprint por un canal confiable;
5. solo entonces corrige la entrada antigua si corresponde.

No elimines la advertencia a ciegas.

## 35. ssh-keygen -R — solo tras verificar

Existe:

```text
ssh-keygen -R NOMBRE_HOST
```

para retirar entradas de `known_hosts`.

Es una operación que modifica tu archivo.

No se practica aquí.

Primero debes demostrar que el cambio de host key es legítimo.

## 36. Preparar el laboratorio

```bash
cd ~/linux-lab
pwd
```

Comprueba:

```bash
ls -ld ./modulo-20-ssh
```

Si no existe:

```bash
mkdir modulo-20-ssh
```

Después:

```bash
cd modulo-20-ssh
pwd
```

No copies archivos reales de `~/.ssh` al laboratorio.

## 37. Práctica A — comprobar cliente

```bash
command -v ssh
ssh -V
```

Responde para ti:

- ¿está instalado el cliente?;
- ¿qué implementación/versión reporta?.

No necesitas actualizarlo por esta práctica.

## 38. Práctica B — configuración efectiva

```bash
ssh -G localhost | head -n 20
```

Identifica:

- hostname;
- user;
- port.

No se realiza una conexión.

## 39. Práctica C — archivos de configuración

Consulta:

```bash
ls -ld ~/.ssh
ls -l ~/.ssh/config
```

Si no existen, no los crees solo por la práctica.

No publiques su contenido.

## 40. Práctica D — known_hosts

Consulta:

```bash
ls -l ~/.ssh/known_hosts
```

Si existe, no lo abras completo ni lo subas.

Si ya conoces un hostname autorizado:

```bash
ssh-keygen -F NOMBRE_HOST
```

Si no tienes uno, omite esa parte.

## 41. Práctica E — clave de laboratorio opcional

Solo si quieres practicar generación:

```bash
mkdir -m 700 claves-lab
ssh-keygen -t ed25519 -f ./claves-lab/lab_ed25519 -C "linux-lab"
```

Después:

```bash
ls -l ./claves-lab
ssh-keygen -lf ./claves-lab/lab_ed25519.pub
```

No abras ni copies la clave privada.

No hagas commit de `claves-lab`.

## 42. Práctica F — clasificar archivos

Clasifica:

```text
~/.ssh/config
~/.ssh/known_hosts
id_ed25519
id_ed25519.pub
authorized_keys
/etc/ssh/ssh_config
```

Responde:

- configuración de cliente;
- hosts conocidos;
- privada;
- pública;
- claves autorizadas en cuenta remota;
- configuración global del cliente.

## 43. Práctica G — decidir si conectarse

Caso:

```text
Servidor propio: sí
Fingerprint verificada: no
```

Decisión:

> no aceptar todavía; verificar primero.

Caso:

```text
Servidor desconocido encontrado en Internet
Autorización: no
```

Decisión:

> no intentar conexión ni autenticación.

## 44. Errores frecuentes

| Error | Problema | Corrección |
|---|---|---|
| Aceptas cualquier host key | Puedes confiar en el servidor equivocado | Verifica fingerprint |
| Confundes host key con user key | Identifican entidades distintas | Separa servidor y usuario |
| Subes la clave privada a GitHub | Comprometes identidad | Nunca la publiques |
| Usas `chmod 777 ~/.ssh` | Permisos inseguros | Usa mínimo privilegio |
| Ignoras aviso de host key cambiada | Puedes ocultar un incidente | Investiga |
| Desactivas StrictHostKeyChecking | Debilitas verificación | Mantén verificación |
| Instalas sshd sin pensar | Puedes exponer un servicio | Posponer hasta módulo de servidor |
| Pruebas contraseñas ajenas | No autorizado | Solo cuentas propias/autorizadas |
| Confundes cliente con servidor | `ssh` no implica `sshd` activo | Comprueba por separado |
| Publicas known_hosts/config | Revelas infraestructura | Mantén privados los detalles |

## 45. Método seguro antes de una conexión SSH

1. confirma que el sistema es propio o autorizado;
2. identifica hostname/IP correcto;
3. confirma puerto;
4. confirma usuario;
5. obtén fingerprint por un canal confiable;
6. conecta;
7. verifica la host key;
8. autentícate con un método autorizado;
9. usa mínimo privilegio;
10. revisa logs ante anomalías.

## 46. Práctica independiente

Sin conectarte a sistemas externos:

1. confirma que existe el cliente SSH;
2. consulta su versión;
3. muestra configuración efectiva para `localhost`;
4. identifica puerto y usuario resultantes;
5. comprueba si existe `~/.ssh`;
6. explica para qué sirve `known_hosts`;
7. explica diferencia entre pública y privada;
8. explica por qué la privada nunca va a GitHub;
9. explica qué harías ante una host key cambiada;
10. explica qué autorización necesitarías antes de usar SSH contra otro equipo;
11. explica qué parte ofensiva de SSH estudiarías únicamente en un laboratorio autorizado;
12. indica qué evidencia revisarías para detectar intentos anómalos de autenticación.

## 47. Mini evaluación

1. ¿qué comando es el cliente OpenSSH?
   - A) `ssh`
   - B) `sshd`
   - C) `ss`

2. ¿`sshd` es el servidor?
   - A) Sí.
   - B) No.

3. ¿la host key identifica al servidor?
   - A) Sí.
   - B) No.

4. ¿`known_hosts` ayuda a recordar identidades de servidores?
   - A) Sí.
   - B) No.

5. ¿debes aceptar una fingerprint desconocida sin verificar?
   - A) Sí.
   - B) No.

6. ¿la clave privada puede subirse a GitHub?
   - A) Sí.
   - B) No.

7. ¿la clave pública y la privada son el mismo archivo?
   - A) Sí.
   - B) No.

8. ¿`ssh -G localhost` establece una sesión remota?
   - A) Sí.
   - B) No.

9. ¿debes desactivar StrictHostKeyChecking para eliminar advertencias?
   - A) Sí.
   - B) No.

10. ¿puedes practicar SSH contra un sistema ajeno sin permiso?
   - A) Sí.
   - B) No.

## 48. Registro de aprendizaje

Puedes responder:

```text
SSH sirve para:
ssh es:
sshd es:
Una host key identifica:
known_hosts sirve para:
Una clave privada:
Una clave pública:
authorized_keys sirve para:
¿Por qué verifico la fingerprint?:
¿Por qué no desactivo StrictHostKeyChecking?:
¿Qué sistemas puedo usar para practicar?:
Algo que todavía confundo:
Estado: EN APRENDIZAJE / PRACTICADO
```

## 49. Fuentes y límites

Clasificación y estado de los enlaces de esta sección: [catálogo de fuentes](06-catalogo-fuentes.md) (jerarquía E04, comprobación del 9 de octubre de 2026).

Fuentes principales verificadas:

- OpenSSH `ssh(1)`:
  https://man.openbsd.org/ssh
- OpenSSH `ssh-keygen(1)`:
  https://man.openbsd.org/ssh-keygen
- OpenSSH `ssh_config(5)`:
  https://man.openbsd.org/ssh_config
- OpenSSH `sshd(8)`:
  https://man.openbsd.org/sshd
- OpenSSH `sshd_config(5)`:
  https://man.openbsd.org/sshd_config

Se posponen:

- instalación y exposición de `sshd`;
- configuración de `sshd_config`;
- firewall para SSH;
- `authorized_keys` práctico en un servidor;
- `ssh-copy-id`;
- `ssh-agent`;
- SCP/SFTP;
- forwarding de puertos;
- ProxyJump;
- certificados SSH;
- bastion hosts;
- hardening avanzado;
- análisis de ataques contra autenticación en laboratorio;
- detección de fuerza bruta/password spraying en logs;
- ejercicios ofensivos controlados en CTF o máquinas propias;
- mitigaciones avanzadas como MFA, rate limiting y políticas de acceso.

**Estado de la lección:** redactada y revisada documentalmente. Las prácticas son locales o requieren sistema propio/autorizado; no se realizan intentos contra terceros.

---

**Siguiente:** [Módulo 21 — Firewall: nftables, UFW y firewalld según el entorno](modulo-21-firewall-nftables-ufw-firewalld.md) · [Volver al índice](README.md)
