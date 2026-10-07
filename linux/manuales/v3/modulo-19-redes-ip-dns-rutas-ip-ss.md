# Módulo 19 — Redes básicas: IP, DNS, rutas, ip y ss

Manual Maestro de Linux y Shell Scripting — Edición 2026 · v3 · Decimonovena entrega.

[Estado actual](README.md) · [Módulo anterior](modulo-18-logs-journalctl-diagnostico.md) · [Arquitectura](00-indice-arquitectura.md)

## 1. Qué aprenderás

Al terminar este módulo podrás:

- explicar qué es una interfaz de red;
- reconocer una dirección IPv4 e IPv6;
- distinguir dirección IP, máscara/prefijo, gateway y DNS;
- explicar qué representa una ruta;
- consultar interfaces y direcciones con `ip`;
- consultar la tabla de rutas con `ip route`;
- interpretar de forma inicial una ruta por defecto;
- explicar qué hace DNS;
- realizar consultas de resolución de nombres con herramientas de lectura;
- consultar sockets con `ss`;
- distinguir un socket escuchando de una conexión establecida;
- reconocer que observar tu propio equipo no equivale a escanear otras redes.

Conocimientos previos:
- procesos;
- archivos;
- pipes;
- permisos;
- logs;
- systemd básico.

**Seguridad y alcance:** este módulo es de observación sobre tu propio equipo y tu propia red. No cambiaremos direcciones IP, rutas, DNS, interfaces ni firewall. No haremos escaneos de redes o puertos externos. No usaremos `ip link set`, `ip addr add/del`, `ip route add/del`, herramientas de escaneo ni `sudo` para ampliar acceso.

## 2. Qué es una red

Una red permite que dispositivos intercambien datos mediante protocolos.

Modelo simplificado:

```text
equipo A ── red ── equipo B
```

En Internet y redes locales, una parte fundamental de la comunicación utiliza la familia de protocolos IP.

No necesitas estudiar todavía Ethernet, ARP, TCP, UDP y DNS a nivel profundo. En este módulo construiremos el mapa básico.

## 3. Interfaz de red

Una **interfaz de red** es el punto lógico mediante el cual el sistema participa en una red.

Puede corresponder a:

- Ethernet;
- Wi‑Fi;
- loopback;
- interfaces virtuales;
- VPN;
- bridges;
- contenedores.

Nombres posibles:

```text
lo
eth0
enp3s0
wlan0
wlp2s0
```

Los nombres reales dependen del sistema.

## 4. Loopback

La interfaz:

```text
lo
```

es la interfaz de loopback.

Direcciones típicas:

```text
127.0.0.1   → IPv4 loopback
::1         → IPv6 loopback
```

Permiten que el equipo se comunique consigo mismo.

No significan “la IP de Internet” del equipo.

## 5. Dirección IP

Una dirección IP identifica una interfaz o punto de comunicación dentro de un contexto de red.

Ejemplo IPv4 ilustrativo:

```text
192.0.2.10
```

Ejemplo IPv6 reservado para documentación:

```text
2001:db8::10
```

Estos ejemplos pertenecen a rangos reservados para documentación y no representan tu red real.

## 6. IPv4

IPv4 usa direcciones de 32 bits.

Se escriben habitualmente como cuatro números decimales:

```text
192.0.2.10
```

Cada octeto va de 0 a 255.

No todas las direcciones IPv4 tienen el mismo propósito.

## 7. Rangos privados IPv4

Tres rangos privados importantes definidos para redes internas son:

```text
10.0.0.0/8
172.16.0.0/12
192.168.0.0/16
```

No son directamente enrutable como direcciones públicas en Internet.

Una dirección privada no debe confundirse con la dirección pública que pueda utilizar un router mediante NAT.

## 8. IPv6

IPv6 usa direcciones de 128 bits.

Ejemplo documental:

```text
2001:db8::1
```

IPv6 utiliza representación hexadecimal y permite abreviar grupos de ceros.

No estudiaremos todavía reglas completas de abreviación, SLAAC, DHCPv6, NDP o privacidad de direcciones.

## 9. Prefijo CIDR

Una dirección puede mostrarse así:

```text
192.0.2.10/24
```

El:

```text
/24
```

indica la longitud del prefijo de red.

En IPv6 es frecuente ver valores como:

```text
/64
```

No debes interpretar el prefijo como “número de equipos” directamente.

El cálculo de subredes se estudiará aparte.

## 10. ip — herramienta principal del módulo

La utilidad `ip` forma parte de iproute2.

Puede mostrar o modificar:

- direcciones;
- enlaces;
- rutas;
- vecinos;
- reglas;
- otros objetos de red.

En este módulo **solo utilizamos operaciones de consulta**.

La sintaxis general es:

```text
ip [opciones] OBJETO COMANDO
```

## 11. ip link show

Consulta:

```bash
ip link show
```

Muestra interfaces/enlaces conocidos por el kernel.

Puedes encontrar datos como:

- nombre;
- estado;
- MTU;
- flags;
- dirección de enlace.

No publiques direcciones MAC completas sin necesidad.

## 12. ip -br link

Una vista más compacta:

```bash
ip -br link
```

`-br` significa **brief**.

Es útil para principiantes porque reduce el ruido.

Ejemplo conceptual:

```text
lo      UNKNOWN
enp...  UP
```

No asumas que `UNKNOWN` en loopback representa una falla.

## 13. ip address

Consulta:

```bash
ip address show
```

Forma abreviada:

```bash
ip addr
```

Muestra direcciones asociadas a interfaces.

Puede incluir:

- IPv4;
- IPv6;
- scope;
- prefijo;
- lifetime.

## 14. Vista breve de direcciones

```bash
ip -br address
```

puede ser más fácil de leer.

Antes de compartir una salida, elimina:

- direcciones públicas;
- IPv6 globales;
- MAC;
- nombres de interfaces que revelen información privada si no son necesarios.

## 15. Estado UP no garantiza Internet

Una interfaz puede aparecer:

```text
UP
```

y aun así no tener acceso a Internet.

Para conectividad completa también pueden intervenir:

- dirección;
- ruta;
- gateway;
- DNS;
- firewall;
- enlace físico;
- proveedor;
- red remota.

No diagnostiques solo mirando una palabra.

## 16. Ruta

Una **ruta** indica cómo debe tratar el sistema tráfico destinado a determinadas redes o direcciones.

Modelo:

```text
destino → siguiente salto/interfaz
```

El kernel consulta su tabla de rutas para decidir por dónde enviar tráfico.

## 17. ip route

Consulta:

```bash
ip route show
```

o:

```bash
ip route
```

Muestra rutas IPv4 conocidas por el kernel en la tabla principal según el contexto.

No modifica nada.

## 18. Ruta por defecto

Puedes encontrar una línea conceptual como:

```text
default via 192.0.2.1 dev eth0
```

Significa, de forma simplificada:

- `default`: destinos sin una ruta más específica;
- `via`: siguiente salto o gateway;
- `dev`: interfaz utilizada.

La dirección es solo un ejemplo documental.

## 19. Gateway

Un **gateway** es un dispositivo o punto de siguiente salto que puede reenviar tráfico hacia otras redes.

En una red doméstica, el router suele cumplir ese papel para la ruta por defecto.

Pero no todo tráfico usa necesariamente el mismo gateway: las rutas más específicas pueden elegir otros caminos.

## 20. Regla de ruta más específica

En términos generales, el sistema selecciona rutas considerando la coincidencia del destino, y una ruta más específica puede prevalecer sobre una ruta por defecto.

No estudiaremos todavía:

- múltiples tablas;
- policy routing;
- métricas complejas;
- ECMP;
- VRF.

## 21. No modificar rutas

Comandos como:

```text
ip route add ...
ip route del ...
ip route replace ...
```

modifican enrutamiento.

Una ruta equivocada puede cortar conectividad.

Por eso no se practican aquí.

## 22. DNS

DNS significa:

```text
Domain Name System
```

Permite resolver nombres a información como direcciones IP.

Modelo:

```text
nombre → resolución DNS → dirección
```

Ejemplo conceptual:

```text
servidor.ejemplo → 192.0.2.20
```

DNS no es lo mismo que conectividad IP.

Puedes tener IP funcional y DNS roto, o resolver un nombre y aun así no poder conectarte al servicio.

## 23. Resolución de nombres y NSS

En Linux, una aplicación puede resolver nombres mediante mecanismos configurados por Name Service Switch (NSS), no necesariamente consultando DNS de forma directa.

Una herramienta útil es:

```bash
getent hosts localhost
```

Esto consulta la base de hosts mediante NSS.

No modifica nada.

## 24. getent ahosts

Si quieres consultar una resolución de nombre mediante NSS:

```bash
getent ahosts localhost
```

Para una práctica completamente local usamos `localhost`.

Resolver nombres públicos puede generar consultas de red, por lo que no es necesario para aprender el concepto inicial.

## 25. /etc/hosts

Este archivo puede proporcionar asociaciones locales de nombres:

```text
/etc/hosts
```

Consulta limitada:

```bash
head -n 10 /etc/hosts
```

No lo edites en este módulo.

No publiques su contenido completo si contiene nombres internos o información privada.

## 26. /etc/resolv.conf

Tradicionalmente:

```text
/etc/resolv.conf
```

contiene o apunta a información relacionada con resolución DNS.

En sistemas modernos puede ser:

- un archivo administrado;
- un symlink;
- parte de una integración con systemd-resolved;
- administrado por NetworkManager u otra herramienta.

No asumas una arquitectura universal.

Consulta segura:

```bash
ls -l /etc/resolv.conf
```

No lo modifiques manualmente.

## 27. resolvectl

Si tu sistema usa systemd-resolved y la herramienta existe:

```bash
command -v resolvectl
```

puedes consultar:

```bash
resolvectl status
```

La salida puede revelar:

- servidores DNS;
- dominios de búsqueda;
- interfaces.

No publiques esos datos completos.

Si `resolvectl` no existe, no instales nada para esta práctica.

## 28. Nombre DNS no equivale a puerto

DNS responde a preguntas sobre nombres.

Un servicio como web o SSH usa además protocolos y puertos.

Ejemplo conceptual:

```text
DNS → ¿a qué dirección corresponde el nombre?
TCP/UDP + puerto → ¿qué servicio/comunicación usa ese endpoint?
```

No mezcles ambos conceptos.

## 29. Socket

Un **socket** es un endpoint de comunicación.

En red puede asociarse a:

- protocolo;
- dirección local;
- puerto local;
- dirección remota;
- puerto remoto;
- estado.

No todos los sockets son de red IP; también existen sockets Unix.

En este módulo nos centraremos en TCP y UDP.

## 30. Puerto

TCP y UDP utilizan números de puerto de 16 bits.

Rango:

```text
0–65535
```

Un puerto no identifica por sí solo una aplicación de manera universal.

Por ejemplo, aunque ciertos servicios tienen puertos convencionales, una aplicación puede configurarse en otro puerto.

## 31. TCP y UDP

Resumen inicial:

```text
TCP → orientado a conexión
UDP → datagramas, sin conexión en el mismo sentido que TCP
```

No estudiaremos todavía handshake, ventanas, retransmisión, MTU o control de congestión.

## 32. ss

`ss` forma parte de iproute2 y muestra información de sockets.

Sustituye gran parte de los usos modernos que antiguamente se hacían con `netstat`.

Consulta:

```bash
ss
```

puede mostrar muchas conexiones/sockets.

Usaremos filtros.

## 33. ss -lnt

Consulta:

```bash
ss -lnt
```

Opciones:

```text
-l → listening
-n → mostrar valores numéricos, sin resolver nombres
-t → TCP
```

Esto muestra sockets TCP en escucha.

Es una consulta local, no un escaneo de otras máquinas.

## 34. ss -lnu

Para UDP:

```bash
ss -lnu
```

Opciones:

```text
-l → listening/unconnected según el contexto
-n → numérico
-u → UDP
```

La semántica de “listen” no es idéntica entre TCP y UDP porque UDP no establece conexiones como TCP.

## 35. ss -tn

Consulta:

```bash
ss -tn
```

muestra sockets TCP con valores numéricos.

Puede revelar direcciones remotas y conexiones activas.

**No publiques la salida completa.**

Úsalo solo para observar tu propio equipo.

## 36. Estado TCP

Puedes ver estados como:

```text
LISTEN
ESTAB
TIME-WAIT
CLOSE-WAIT
```

No necesitas memorizar todos ahora.

Dos básicos:

```text
LISTEN → espera conexiones entrantes
ESTAB  → conexión establecida
```

Un socket LISTEN no significa automáticamente que esté accesible desde Internet. Influyen:

- dirección de bind;
- firewall;
- routing;
- NAT;
- red.

## 37. 0.0.0.0 y ::

En una escucha puedes encontrar:

```text
0.0.0.0:PUERTO
```

o:

```text
[::]:PUERTO
```

De forma general indican binding a direcciones wildcard de IPv4 o IPv6.

Pero la exposición real depende de firewall, namespaces, configuración del socket y red.

No concluyas “está público en Internet” solo por ver wildcard.

## 38. 127.0.0.1 y ::1 en escucha

Si un servicio escucha únicamente en:

```text
127.0.0.1
::1
```

está ligado al loopback correspondiente.

Eso normalmente limita el acceso a la propia máquina desde ese namespace de red.

No cambies el bind para “hacerlo accesible” en esta lección.

## 39. ss y procesos

Una opción frecuente de `ss` permite mostrar procesos asociados, pero la visibilidad depende de permisos.

No usaremos esa opción como requisito porque puede revelar información de procesos y algunas entradas requieren privilegios.

En este nivel basta con aprender:

- dirección;
- puerto;
- protocolo;
- estado.

## 40. netstat e ifconfig en contexto

Herramientas históricas como:

```text
ifconfig
route
netstat
```

pertenecen al conjunto net-tools y todavía pueden existir.

Este manual prioriza:

```text
ip
ss
```

porque forman parte de iproute2 y cubren la administración/consulta moderna de red.

No afirmamos que net-tools haya “desaparecido”; simplemente no será la herramienta principal.

## 41. Diagnóstico por capas

Si “Internet no funciona”, no empieces cambiando DNS o firewall.

Sigue una secuencia:

```text
1. interfaz
2. dirección
3. ruta
4. resolución de nombres
5. sockets/servicio
6. logs
```

Esto evita cambiar varias cosas a la vez.

## 42. Paso 1 — interfaz

Consulta:

```bash
ip -br link
```

Pregunta:

- ¿la interfaz esperada existe?;
- ¿está UP?;
- ¿es loopback, física o virtual?.

No la subas/bajes.

## 43. Paso 2 — dirección

```bash
ip -br address
```

Pregunta:

- ¿tiene IPv4?;
- ¿tiene IPv6?;
- ¿qué prefijo usa?;
- ¿la dirección parece local/privada?.

No compartas direcciones completas si no son necesarias.

## 44. Paso 3 — ruta

```bash
ip route
```

Pregunta:

- ¿existe una ruta por defecto?;
- ¿qué interfaz usa?;
- ¿existen rutas más específicas?.

No añadas ni borres rutas.

## 45. Paso 4 — nombres

Prueba local:

```bash
getent hosts localhost
```

Si necesitas revisar configuración:

```bash
ls -l /etc/resolv.conf
```

y, si existe:

```bash
resolvectl status
```

No edites nada.

## 46. Paso 5 — sockets

Consulta:

```bash
ss -lnt
```

Si investigas UDP:

```bash
ss -lnu
```

Pregunta:

- ¿el servicio parece estar escuchando?;
- ¿en qué dirección?;
- ¿en qué puerto?.

No escanees otro equipo para responderlo.

## 47. Paso 6 — logs

Si el problema corresponde a una unidad systemd:

```bash
systemctl status NOMBRE.service
journalctl -u NOMBRE.service -b -n 30
```

Observa antes de reiniciar.

## 48. Privacidad de información de red

No publiques sin necesidad:

- dirección IP pública;
- IPv6 global;
- MAC;
- gateway;
- servidores DNS internos;
- dominios de búsqueda internos;
- lista completa de sockets;
- IP remotas de conexiones;
- hostnames privados.

Para pedir ayuda, comparte solo los campos imprescindibles y sustituye identificadores privados cuando se pueda conservar el significado técnico.

## 49. Qué no haremos

No ejecutaremos:

```text
ip link set ... up/down
ip addr add ...
ip addr del ...
ip route add ...
ip route del ...
edición de /etc/resolv.conf
cambios con nmcli
cambios con networkctl
escaneo de puertos
escaneo de subredes
```

Esas acciones requieren contexto adicional o pertenecen a administración/ciberseguridad posterior.

## 50. Práctica A — interfaces

```bash
ip -br link
```

Identifica:

- loopback;
- una interfaz adicional, si existe;
- estado.

No compartas MAC.

## 51. Práctica B — direcciones

```bash
ip -br address
```

Para ti, identifica:

- IPv4;
- IPv6;
- prefijo.

No necesitas pegar la salida.

## 52. Práctica C — rutas

```bash
ip route
```

Busca la palabra:

```text
default
```

si existe.

Explica qué interfaz usaría esa ruta.

## 53. Práctica D — localhost

```bash
getent hosts localhost
```

Explica:

- nombre consultado;
- dirección devuelta;
- por qué no necesita representar Internet.

## 54. Práctica E — DNS del sistema

```bash
command -v resolvectl
```

Si existe:

```bash
resolvectl status
```

Solo observa.

Si no existe:

```text
resolvectl no disponible; práctica omitida
```

## 55. Práctica F — TCP escuchando

```bash
ss -lnt
```

Identifica:

- columna de estado;
- dirección local;
- puerto.

No publiques la lista completa.

## 56. Práctica G — UDP local

```bash
ss -lnu
```

Compara con TCP.

No interpretes ausencia de estado ESTAB como error: UDP funciona de forma diferente.

## 57. Práctica H — clasificar datos

Clasifica:

```text
192.168.1.20/24
default via ...
127.0.0.1
::1
LISTEN
ESTAB
53
443
```

Categorías:

- dirección/prefijo;
- ruta;
- loopback;
- estado TCP;
- puerto.

Los puertos 53 y 443 son ejemplos convencionales, no una garantía del servicio real.

## 58. Errores frecuentes

| Error | Problema | Corrección |
|---|---|---|
| Confundes IP con DNS | Dirección y resolución son conceptos distintos | Separa capa de nombres de capa IP |
| “UP = Internet funciona” | Faltan ruta/DNS/otros factores | Diagnostica por pasos |
| “default = única ruta” | Puede haber rutas más específicas | Lee tabla completa |
| “LISTEN = abierto a Internet” | Depende de bind, firewall y red | No concluyas exposición solo con ss |
| “puerto 443 = siempre HTTPS” | Es convención, no garantía absoluta | Confirma aplicación/protocolo |
| Publicas `ss -tn` completo | Puede revelar IP remotas | Comparte solo fragmentos |
| Editas resolv.conf directamente | Puede ser administrado por otra herramienta | Identifica quién gestiona DNS |
| Usas ifconfig/netstat como única referencia | Son herramientas históricas | Aprende primero ip/ss |
| Cambias ruta por prueba | Puedes cortar conectividad | Solo consulta |
| Escaneas otra red para aprender | No es necesario | Observa tu propio host |

## 59. Método de diagnóstico inicial de red

Cuando hay un problema:

1. identifica la interfaz con `ip -br link`;
2. revisa dirección con `ip -br address`;
3. revisa rutas con `ip route`;
4. prueba resolución local con `getent`;
5. revisa DNS del sistema si procede;
6. revisa sockets del servicio con `ss`;
7. revisa status/logs;
8. cambia una sola cosa cuando tengas una hipótesis;
9. documenta el resultado.

## 60. Práctica independiente

Sin cambiar configuración:

1. identifica la interfaz loopback;
2. identifica una interfaz de red adicional;
3. consulta sus direcciones;
4. localiza el prefijo;
5. identifica la ruta por defecto si existe;
6. resuelve `localhost`;
7. comprueba si `resolvectl` existe;
8. lista TCP en escucha;
9. lista UDP;
10. explica por qué ninguna de estas consultas es un escaneo de otra máquina.

## 61. Mini evaluación

1. ¿Qué muestra `ip -br link`?
   - A) Interfaces de forma breve.
   - B) Paquetes instalados.
   - C) Usuarios.

2. ¿Qué muestra `ip -br address`?
   - A) Direcciones asociadas a interfaces.
   - B) Logs.
   - C) Procesos.

3. ¿Qué muestra `ip route`?
   - A) Tabla de rutas.
   - B) DNS cache exclusivamente.
   - C) Contraseñas.

4. ¿127.0.0.1 es loopback IPv4?
   - A) Sí.
   - B) No.

5. ¿::1 es loopback IPv6?
   - A) Sí.
   - B) No.

6. ¿DNS e IP son el mismo concepto?
   - A) Sí.
   - B) No.

7. ¿`ss -lnt` muestra sockets TCP en escucha con valores numéricos?
   - A) Sí.
   - B) No.

8. ¿un socket LISTEN demuestra por sí solo exposición a Internet?
   - A) Sí.
   - B) No.

9. ¿debemos modificar rutas en este módulo?
   - A) Sí.
   - B) No.

10. ¿debemos escanear otra red para aprender `ss`?
   - A) Sí.
   - B) No.

## 62. Registro de aprendizaje

Puedes responder:

```text
Una interfaz es:
IPv4 es:
IPv6 es:
Un prefijo /24 representa:
Una ruta sirve para:
Una ruta default sirve para:
DNS sirve para:
Loopback IPv4 es:
Loopback IPv6 es:
ss sirve para:
LISTEN significa:
ESTAB significa:
¿Por qué no comparto toda mi salida de red?:
Algo que todavía confundo:
Estado: EN APRENDIZAJE / PRACTICADO
```

## 63. Fuentes y límites

Fuentes principales verificadas:

- iproute2 — `ip(8)`:
  https://man7.org/linux/man-pages/man8/ip.8.html
- iproute2 — `ip-address(8)`:
  https://man7.org/linux/man-pages/man8/ip-address.8.html
- iproute2 — `ip-route(8)`:
  https://man7.org/linux/man-pages/man8/ip-route.8.html
- iproute2 — `ss(8)`:
  https://man7.org/linux/man-pages/man8/ss.8.html
- Linux man-pages / glibc — `getent(1)`:
  https://man7.org/linux/man-pages/man1/getent.1.html
- systemd — `resolvectl`:
  https://www.freedesktop.org/software/systemd/man/latest/resolvectl.html

Se posponen:

- subnetting detallado;
- ARP/NDP;
- DHCP;
- configuración con NetworkManager;
- netplan;
- systemd-networkd;
- Wi‑Fi administrativo;
- modificación de rutas;
- firewall;
- NAT;
- packet capture;
- escaneo;
- namespaces de red;
- troubleshooting avanzado TCP.

**Estado de la lección:** redactada y revisada documentalmente. Las prácticas son locales y de consulta; no modifican red ni examinan sistemas ajenos.

Siguiente módulo por redactar: **Módulo 20 — SSH en sistemas propios o expresamente autorizados**.
