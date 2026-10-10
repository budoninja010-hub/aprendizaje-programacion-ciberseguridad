# Módulo 21 — Firewall: nftables, UFW y firewalld según el entorno

Manual Maestro de Linux y Shell Scripting — Edición 2026 · v3 · Vigesimoprimera entrega.

[Índice del manual](README.md) · [← Módulo 20](modulo-20-ssh-sistemas-autorizados.md) · [Arquitectura](00-indice-arquitectura.md) · [Módulo 22 →](modulo-22-vi-vim-edicion-segura.md)

## 1. Qué aprenderás

Al terminar este módulo podrás:

- explicar qué hace un firewall de host;
- distinguir filtrado de paquetes de autenticación, antivirus y cifrado;
- reconocer Netfilter como infraestructura del kernel Linux;
- explicar qué es nftables y qué hace la utilidad `nft`;
- reconocer UFW como interfaz simplificada documentada por Ubuntu;
- reconocer firewalld como gestor dinámico documentado por RHEL;
- distinguir tráfico de entrada, salida y reenvío;
- comprender reglas, políticas, estados de conexión y orden de evaluación;
- consultar qué herramientas existen sin modificar reglas;
- explicar por qué no debes mezclar varios gestores sin comprender cómo interactúan;
- elaborar un plan seguro antes de cambiar un firewall en una máquina local o remota.

Conocimientos previos:
- interfaces, direcciones IP y rutas;
- TCP/UDP y puertos;
- `ss`;
- systemd;
- SSH;
- permisos y mínimo privilegio.

**Seguridad:** las prácticas obligatorias son de identificación y lectura. No abriremos ni cerraremos puertos, no cambiaremos políticas, no habilitaremos/deshabilitaremos el firewall, no recargaremos reglas y no vaciaremos rulesets. Toda práctica futura de modificación se realizará únicamente en equipos propios, VMs, laboratorios, CTF o sistemas expresamente autorizados.

## 2. Qué es un firewall

Un firewall aplica reglas al tráfico de red.

Modelo simplificado:

```text
paquete
  ↓
reglas del firewall
  ↓
permitir / rechazar / descartar / continuar evaluación
```

Un firewall puede decidir según información como:

- dirección origen;
- dirección destino;
- protocolo;
- puerto;
- interfaz;
- estado de conexión;
- zona;
- otras propiedades.

## 3. Lo que un firewall NO es

Un firewall no sustituye:

- autenticación;
- parches;
- cifrado;
- permisos;
- configuración segura;
- antivirus/antimalware;
- monitoreo;
- copias de seguridad.

Ejemplo:

> permitir TCP 22 no autentica al usuario SSH.

Solo permite que el tráfico alcance el servicio si las demás condiciones también lo permiten.

## 4. Netfilter

Linux incluye el subsistema **Netfilter** en el kernel.

Las soluciones modernas de firewall en Linux utilizan esta infraestructura para clasificar y decidir el destino del tráfico.

Herramientas de espacio de usuario pueden configurar reglas que el kernel aplica.

Modelo:

```text
herramienta de usuario
        ↓
    Netfilter
        ↓
      kernel
```

No confundas Netfilter con una única utilidad de línea de comandos.

## 5. nftables

**nftables** es el framework moderno de filtrado de paquetes que sucede a los conjuntos históricos de herramientas como:

```text
iptables
ip6tables
arptables
ebtables
```

La utilidad principal es:

```text
nft
```

RHEL 10 documenta nftables como opción para escenarios donde se necesita control detallado del ruleset.

## 6. Elementos de nftables

Modelo inicial:

```text
tabla
 └─ cadena
     └─ regla
```

### Tabla

Agrupa cadenas y reglas dentro de una familia/contexto.

### Cadena

Contiene reglas y puede asociarse a puntos de procesamiento del tráfico.

### Regla

Describe coincidencias y una acción.

No vamos a crear ninguna todavía.

## 7. Familias de nftables

nftables admite familias como:

```text
ip
ip6
inet
arp
bridge
netdev
```

Para principiantes, `inet` es importante porque permite trabajar con IPv4 e IPv6 dentro de la misma familia de reglas.

No crearemos tablas ni cadenas en este módulo.

## 8. Tráfico de entrada, salida y reenvío

Tres conceptos fundamentales:

```text
INPUT/FILTRO DE ENTRADA   → tráfico dirigido al propio host
OUTPUT/FILTRO DE SALIDA   → tráfico originado por el propio host
FORWARD/REENVÍO           → tráfico que atraviesa el host hacia otro destino
```

Los nombres exactos de cadenas dependen de la herramienta y configuración.

Un equipo de escritorio normalmente no necesita comportarse como router solo porque tenga varias interfaces.

## 9. Aceptar, descartar y rechazar

Acciones conceptuales:

```text
accept → permitir
drop   → descartar silenciosamente
reject → rechazar y, según configuración, responder con un error
```

No existe una única elección correcta para todos los contextos.

La política debe diseñarse según el servicio, red y amenaza.

## 10. Stateful firewall

Un firewall **stateful** mantiene información sobre el estado de las conexiones.

Eso permite distinguir, por ejemplo:

```text
conexión nueva
conexión ya establecida
tráfico relacionado
```

Netfilter proporciona connection tracking para estos escenarios.

UFW es stateful por diseño según la documentación de Ubuntu.

## 11. Regla y política por defecto

Una cadena puede tener reglas específicas y una política aplicable cuando ninguna regla coincide, según el sistema utilizado.

Conceptualmente:

```text
reglas específicas
       ↓
si ninguna coincide
       ↓
política por defecto
```

La idea de “denegar por defecto” es importante en seguridad, pero **no debe aplicarse a ciegas** en una máquina remota porque podrías bloquear tu propio acceso.

## 12. Orden de evaluación

En muchos diseños de firewall, el orden de reglas importa.

Una regla anterior puede decidir el tráfico antes de que se evalúe otra posterior.

Por eso no basta con preguntar:

> “¿existe una regla para el puerto?”

También debes preguntar:

- ¿en qué cadena?;
- ¿en qué orden?;
- ¿qué tráfico coincide?;
- ¿qué política existe?;
- ¿qué gestor creó esa regla?.

## 13. UFW en Ubuntu

Ubuntu documenta:

```text
ufw
```

como una herramienta simplificada para crear un firewall de host.

UFW significa:

```text
Uncomplicated Firewall
```

La documentación de Ubuntu señala que está disponible y **deshabilitado inicialmente por defecto** (comprobado en la documentación de seguridad de Ubuntu el 9 de octubre de 2026).

No generalizamos ese comportamiento a Debian.

## 14. UFW no es “el firewall del kernel”

UFW es una interfaz de administración.

Por debajo utiliza capacidades de Netfilter mediante backends apropiados.

Modelo:

```text
UFW
 ↓
reglas de filtrado
 ↓
Netfilter
```

Por eso no debes pensar que UFW, nftables y Netfilter son tres firewalls completamente independientes.

## 15. Consulta de disponibilidad de UFW

Consulta segura:

```bash
command -v ufw
```

Si existe, puedes saber que la herramienta está instalada.

Una consulta como:

```text
ufw status
```

es de lectura, pero algunas configuraciones pueden requerir privilegios.

Si obtienes permiso denegado, **no añadas `sudo` solo para completar la práctica**.

## 16. Comandos UFW que modifican

Ejemplos administrativos:

```text
ufw enable
ufw disable
ufw allow ...
ufw deny ...
ufw delete ...
```

Estos comandos modifican la política o las reglas.

No se ejecutan en esta lección.

### Riesgo especial

Si administras un equipo por SSH y habilitas un firewall sin haber permitido correctamente el acceso necesario, puedes bloquear tu propia sesión o conexiones futuras.

## 17. firewalld

RHEL 10 documenta:

```text
firewalld
```

como firewall dinámico para casos comunes.

Conceptos importantes:

- zonas;
- servicios;
- puertos;
- políticas;
- reglas.

La interfaz principal de línea de comandos es:

```text
firewall-cmd
```

## 18. Zonas de firewalld

Una **zona** representa un nivel/contexto de confianza para tráfico asociado a interfaces o fuentes.

Ejemplos de nombres que pueden existir:

```text
public
home
internal
trusted
drop
```

No memorices sus políticas solo por el nombre.

Consulta la configuración efectiva del sistema.

## 19. Servicio en firewalld

Un “service” de firewalld agrupa información necesaria para permitir un servicio de red.

Puede incluir:

- puertos;
- protocolos;
- helpers/módulos según configuración.

Ejemplo conceptual:

```text
servicio SSH
→ TCP 22 de forma convencional
```

Pero SSH puede usar otro puerto, y la definición efectiva debe comprobarse.

## 20. runtime y permanent en firewalld

firewalld distingue entre:

```text
runtime   → estado efectivo actual
permanent → configuración persistente
```

Un cambio runtime puede perderse al recargar/reiniciar.

Un cambio permanent no necesariamente se aplica inmediatamente al runtime hasta realizar la acción correspondiente.

Esta diferencia es crítica.

No realizaremos cambios en ninguno de los dos.

## 21. Consultas firewalld

Si existe:

```bash
command -v firewall-cmd
```

puedes intentar una consulta no modificadora:

```bash
firewall-cmd --state
```

Si responde:

```text
running
```

el servicio está activo.

También existen consultas como:

```text
firewall-cmd --get-active-zones
firewall-cmd --list-all
```

Si requieren autorización en tu entorno, no eleves privilegios solo por la práctica.

## 22. nft y lectura del ruleset

Consulta de disponibilidad:

```bash
command -v nft
```

La orden conceptual para listar el ruleset es:

```text
nft list ruleset
```

A menudo la lectura completa requiere privilegios.

Si tu usuario no puede verla, registra:

```text
ruleset no accesible sin privilegios
```

y continúa.

No uses `sudo` solo para terminar el ejercicio.

## 23. nft flush ruleset — comando de alto riesgo

Existe una operación que puede vaciar el conjunto de reglas:

```text
nft flush ruleset
```

**No la ejecutes.**

Puede eliminar protecciones de red y afectar reglas instaladas por otras herramientas que compartan infraestructura.

Se incluye solo para que puedas reconocerla como una orden peligrosa.

## 24. No mezclar gestores a ciegas

RHEL 10 advierte que no deben operar simultáneamente servicios de firewall que puedan interferirse entre sí.

Problema conceptual:

```text
firewalld administra reglas
+
administrador modifica nftables manualmente sin coordinación
=
estado difícil de razonar
```

Antes de modificar, identifica quién administra el firewall.

## 25. iptables en contexto

`iptables` sigue apareciendo en documentación, sistemas heredados y capas de compatibilidad.

Pero nftables es el framework moderno sucesor.

No significa que todo comando `iptables` haya dejado de existir.

Tampoco significa que debas convertir reglas automáticamente sin comprender la implementación.

## 26. iptables-nft

Algunos sistemas ofrecen herramientas `iptables` que traducen o interactúan con infraestructura nftables.

Esto hace todavía más importante no asumir que:

```text
“veo iptables” = “estoy usando exclusivamente el framework histórico”
```

La implementación concreta debe verificarse.

## 27. Firewall y SSH

Antes de modificar un firewall en un servidor remoto:

1. confirma el puerto real de SSH;
2. confirma la interfaz/red desde la que administras;
3. conserva una sesión existente;
4. asegúrate de tener acceso alternativo o consola;
5. aplica el cambio mínimo;
6. verifica antes de cerrar la sesión.

En este módulo **no hacemos ese cambio**; solo aprendemos el procedimiento mental.

## 28. Firewall y servicios escuchando

Compara:

```bash
ss -lnt
```

con el firewall.

`ss` responde:

> ¿qué sockets están escuchando localmente?

El firewall responde:

> ¿qué tráfico puede pasar según las reglas?

Un servicio puede escuchar pero estar bloqueado por firewall.

También puede existir una regla permitiendo un puerto sin que ningún servicio esté escuchando.

## 29. Firewall no “abre un servicio”

Si permites un puerto en un firewall:

- no instala software;
- no inicia el servicio;
- no configura autenticación;
- no crea automáticamente una aplicación que escuche.

Por eso:

```text
servicio
+
socket escuchando
+
ruta
+
firewall
+
autenticación
```

son piezas distintas.

## 30. IPv4 e IPv6

Una política que protege solo IPv4 puede dejar IPv6 con un comportamiento distinto si el host lo utiliza.

Al diseñar firewalls debes revisar ambos protocolos cuando sean relevantes.

nftables con familia `inet` puede tratar IPv4 e IPv6 en un mismo ruleset.

No deshabilites IPv6 simplemente para evitar aprender sus reglas.

## 31. Entrada y salida

Muchos tutoriales se concentran en tráfico entrante.

Pero un firewall también puede controlar:

- tráfico saliente;
- tráfico reenviado.

Bloquear salida sin planificación puede romper:

- DNS;
- actualizaciones;
- sincronización;
- APIs;
- repositorios;
- servicios.

No establezcas políticas de salida restrictivas a ciegas.

## 32. Forwarding

El tráfico **forwarded** atraviesa el equipo.

Ejemplos:

- router;
- gateway;
- host con redes virtuales;
- host de contenedores.

Un equipo con Docker, Podman, Kubernetes u otras tecnologías puede tener reglas adicionales.

No modifiques rulesets de un host con contenedores sin comprender qué componente los administra.

## 33. NAT no es igual a firewall

NAT modifica información de direccionamiento/puertos para determinados flujos.

Firewall filtra tráfico.

Pueden coexistir en Netfilter, pero son conceptos distintos.

No estudiaremos NAT en profundidad todavía.

## 34. REJECT frente a DROP

Conceptualmente:

```text
DROP   → descarta
REJECT → rechaza de forma explícita según el protocolo/regla
```

No hay una regla universal de “siempre usa DROP”.

La decisión depende del entorno, diagnóstico y política.

## 35. Logs del firewall

Los firewalls pueden registrar determinados eventos.

Pero habilitar logging excesivo puede:

- llenar logs;
- consumir recursos;
- crear ruido;
- registrar datos sensibles.

No activaremos logging nuevo en esta lección.

Usaremos los logs existentes cuando lleguemos a laboratorios defensivos.

## 36. Preparar la práctica

No necesitas crear reglas.

Primero identifica el sistema:

```bash
cat /etc/os-release
```

Después:

```bash
command -v nft
command -v ufw
command -v firewall-cmd
command -v iptables
```

Anota solo qué herramientas existen.

## 37. Práctica A — identificar gestor probable

Completa:

```text
Distribución:
nft disponible:
ufw disponible:
firewall-cmd disponible:
iptables disponible:
```

No concluyas todavía cuál administra realmente el firewall solo porque un binario exista.

## 38. Práctica B — servicios systemd relacionados

Consulta:

```bash
systemctl list-unit-files | grep -E 'firewalld|nftables|ufw'
```

Esto solo busca nombres conocidos entre unidades.

No habilites ni inicies ninguno.

## 39. Práctica C — firewalld si existe

Si `firewall-cmd` existe:

```bash
firewall-cmd --state
```

Si funciona sin privilegios, registra el estado.

Si no funciona por permisos o porque firewalld no está activo, no fuerces la práctica.

## 40. Práctica D — UFW si existe

Si `ufw` existe, primero:

```bash
command -v ufw
```

La consulta conceptual de estado es:

```text
ufw status
```

Si tu sistema requiere privilegios para verla, no añadas `sudo` solo por este ejercicio.

## 41. Práctica E — nftables si existe

Si `nft` existe, reconoce:

```text
nft list ruleset
```

como la consulta del conjunto de reglas.

Si no tienes permisos para verla, no eleves privilegios.

**Nunca ejecutes `nft flush ruleset`.**

## 42. Práctica F — comparar servicio y firewall

Ejecuta:

```bash
ss -lnt
```

Elige un socket local que reconozcas.

Responde conceptualmente:

- ¿qué dirección escucha?;
- ¿qué puerto?;
- ¿el hecho de escuchar demuestra que el firewall lo permite externamente?.

Respuesta esperada a la última: no.

## 43. Práctica G — clasificar acciones

Clasifica como:

```text
CONSULTA
MODIFICA
ALTO RIESGO
```

Ejemplos:

```text
command -v nft
firewall-cmd --state
ufw status
nft list ruleset
ufw enable
ufw allow 22
firewall-cmd --add-service=ssh
nft add rule ...
nft flush ruleset
```

No ejecutes las acciones que modifican.

## 44. Práctica H — escenario SSH

Escenario:

```text
Administras un servidor propio solo por SSH.
Quieres activar un firewall.
No tienes consola alternativa.
No has confirmado el puerto SSH.
```

Decisión correcta:

> no activar todavía.

Primero debes diseñar y verificar el acceso de administración y un plan de recuperación.

## 45. Método seguro antes de cambiar un firewall

1. identifica distribución;
2. identifica gestor real;
3. guarda/consulta la configuración actual;
4. identifica interfaces;
5. identifica servicios escuchando;
6. identifica qué tráfico necesitas;
7. considera IPv4 e IPv6;
8. prepara acceso alternativo;
9. aplica el cambio mínimo;
10. verifica conectividad;
11. revisa logs;
12. documenta el cambio.

## 46. Método de diagnóstico

Si un servicio “no responde”:

1. ¿el proceso está activo?;
2. ¿escucha con `ss`?;
3. ¿en qué dirección/puerto?;
4. ¿existe ruta?;
5. ¿el firewall permite el flujo?;
6. ¿la aplicación exige autenticación?;
7. ¿los logs muestran errores?.

No empieces abriendo puertos al azar.

## 47. Errores frecuentes

| Error | Problema | Corrección |
|---|---|---|
| “Firewall = antivirus” | Funciones distintas | Separa controles |
| “Puerto permitido = servicio activo” | La app puede no estar escuchando | Comprueba con `ss` |
| “LISTEN = accesible desde Internet” | Faltan firewall, ruta y NAT | Evalúa todo el camino |
| Habilitas UFW remotamente sin plan | Puedes bloquear SSH | Prepara acceso antes |
| Mezclas firewalld y nft manual | Estado difícil de predecir | Identifica un gestor |
| Ejecutas `nft flush ruleset` | Puedes eliminar protecciones | No usar en práctica |
| Solo proteges IPv4 | IPv6 puede seguir activo | Evalúa ambos |
| Abres un puerto para “probar” | Amplías superficie | Diagnostica primero |
| Usas sudo para cualquier consulta | Privilegios innecesarios | Mantén mínimo privilegio |
| Copias reglas de otra distro | Modelo/gestor puede diferir | Sigue documentación del entorno |

## 48. Práctica independiente

Sin modificar el firewall:

1. identifica distribución;
2. detecta `nft`, `ufw`, `firewall-cmd` e `iptables`;
3. identifica unidades relacionadas mediante systemd;
4. consulta firewalld solo si está disponible y accesible sin elevar privilegios;
5. reconoce cómo consultar UFW sin ejecutarlo si requiere privilegios;
6. reconoce `nft list ruleset` como consulta;
7. revisa tus sockets locales con `ss -lnt`;
8. explica por qué un socket en LISTEN no demuestra exposición;
9. explica por qué no mezclarías gestores;
10. explica el riesgo de cambiar un firewall por SSH.

## 49. Mini evaluación

1. ¿Netfilter pertenece al kernel Linux?
   - A) Sí.
   - B) No.

2. ¿nftables es el sucesor moderno de varias herramientas históricas de filtrado?
   - A) Sí.
   - B) No.

3. ¿UFW es documentado por Ubuntu como interfaz simplificada?
   - A) Sí.
   - B) No.

4. ¿Ubuntu documenta UFW inicialmente deshabilitado por defecto?
   - A) Sí.
   - B) No.

5. ¿firewalld utiliza el concepto de zonas?
   - A) Sí.
   - B) No.

6. ¿`runtime` y `permanent` significan lo mismo en firewalld?
   - A) Sí.
   - B) No.

7. ¿un puerto permitido significa que un servicio está ejecutándose?
   - A) Sí.
   - B) No.

8. ¿un socket LISTEN garantiza exposición pública?
   - A) Sí.
   - B) No.

9. ¿debes ejecutar `nft flush ruleset` para aprender?
   - A) Sí.
   - B) No.

10. ¿debes planificar acceso alternativo antes de cambiar el firewall de un servidor remoto?
   - A) Sí.
   - B) No.

## 50. Registro de aprendizaje

Puedes responder:

```text
Un firewall sirve para:
Netfilter es:
nftables es:
nft es:
UFW es:
firewalld es:
Una zona es:
runtime significa:
permanent significa:
LISTEN no significa exposición porque:
¿Por qué no mezclo gestores?:
¿Por qué no ejecuto nft flush ruleset?:
Algo que todavía confundo:
Estado: EN APRENDIZAJE / PRACTICADO
```

## 51. Fuentes y límites

Clasificación y estado de los enlaces de esta sección: [catálogo de fuentes](auditorias/06-catalogo-fuentes.md) (jerarquía E04, comprobación del 9 de octubre de 2026).

Fuentes principales verificadas para esta edición:

- Netfilter/nftables (proyecto original): https://www.netfilter.org/projects/nftables/index.html
- nftables (documentación del proyecto): https://wiki.nftables.org/
- firewalld (documentación original): https://firewalld.org/documentation/
- UFW se documenta con las fuentes oficiales de Ubuntu que siguen.
- Ubuntu Security — Firewall:
  https://documentation.ubuntu.com/security/security-features/network/firewall/
- Ubuntu Server — Firewall / UFW:
  https://ubuntu.com/server/docs/firewalls/
- RHEL 10 — Configuring firewalls and packet filters:
  https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/configuring_firewalls_and_packet_filters/
- RHEL 10 — Getting started with nftables:
  https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/configuring_firewalls_and_packet_filters/getting-started-with-nftables

Se posponen:

- creación real de reglas nftables;
- habilitación real de UFW;
- zonas y servicios firewalld prácticos;
- cambios runtime/permanent;
- reglas IPv4/IPv6;
- forwarding;
- NAT;
- logging de firewall;
- sets/maps avanzados;
- rate limiting;
- políticas por interfaz/origen;
- hardening práctico de SSH con firewall;
- laboratorios ofensivos/defensivos controlados.

**Estado de la lección:** redactada y revisada documentalmente. Las prácticas obligatorias son de consulta; no modifican el firewall.

---

**Siguiente:** [Módulo 22 — vi/Vim: edición segura de archivos de texto](modulo-22-vi-vim-edicion-segura.md) · [Volver al índice](README.md)
