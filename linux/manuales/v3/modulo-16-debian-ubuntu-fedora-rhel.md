# Módulo 16 — Diferencias entre Debian, Ubuntu, Fedora y RHEL

Manual Maestro de Linux y Shell Scripting — Edición 2026 · v3 · Decimosexta entrega.

[Índice del manual](README.md) · [← Módulo 15](modulo-15-paquetes-repositorios-actualizaciones.md) · [Arquitectura](00-indice-arquitectura.md) · [Módulo 17 →](modulo-17-systemd-unidades-servicios-init.md)

## 1. Qué aprenderás

Al terminar este módulo podrás:

- distinguir Debian, Ubuntu, Fedora y RHEL sin tratarlas como sistemas idénticos;
- reconocer qué distribuciones usan paquetes DEB y cuáles RPM;
- relacionar APT/dpkg con Debian/Ubuntu;
- relacionar DNF/RPM con Fedora/RHEL tradicionales;
- comprender diferencias generales de ciclo de publicación y soporte;
- reconocer diferencias de políticas y herramientas de seguridad;
- evitar copiar instrucciones de una distribución a otra sin verificar;
- identificar tu distribución y versión antes de administrar paquetes, firewall o seguridad.

Conocimientos previos:
- distribución y versión;
- paquetes y repositorios;
- usuarios y permisos;
- procesos;
- lectura de `/etc/os-release`.

**Seguridad:** este módulo es de identificación y comparación. Las prácticas son de lectura. No instalaremos paquetes, no cambiaremos repositorios, no modificaremos firewall, SELinux ni AppArmor, y no realizaremos migraciones de versión.

## 2. Cuatro distribuciones, no cuatro “sabores idénticos”

Todas pueden ejecutar un kernel Linux y muchas herramientas GNU, pero difieren en aspectos como:

- proyecto y gobernanza;
- ciclo de publicación;
- política de soporte;
- selección de versiones de software;
- repositorios;
- formato y herramientas de paquetes;
- políticas de seguridad;
- documentación;
- soporte comercial;
- convenciones administrativas.

Por eso un comando válido en una distribución no debe copiarse automáticamente a otra.

## 3. Debian

Debian es una distribución comunitaria con varias ramas de desarrollo y mantenimiento.

La documentación oficial distingue al menos:

```text
stable
testing
unstable
```

En octubre de 2026, la rama estable actual es:

```text
Debian 13 "trixie"
```

Debian recomienda `stable` como la versión de producción para la mayoría de usuarios.

Fuentes:
- https://www.debian.org/releases/
- https://www.debian.org/doc/manuals/debian-reference/

## 4. Debian stable, testing y unstable

Modelo simplificado:

```text
unstable → desarrollo activo
   ↓
testing  → preparación de la siguiente estable
   ↓
stable   → publicación estable
```

No interpretes `testing` como una simple “versión estable pero más nueva”.

Debian advierte que mezclar suites sin una política clara puede producir problemas de dependencias y versiones.

Para este curso, las prácticas de administración se diseñan pensando en una versión estable soportada.

## 5. Paquetes en Debian

Debian utiliza paquetes:

```text
.deb
```

Herramientas importantes:

```text
APT  → gestión de alto nivel
dpkg → gestión local/base de paquetes Debian
```

En la referencia Debian actual se recomienda `apt` para operaciones interactivas y `apt-get` para scripts y determinados casos automatizados.

No reemplaces `apt` por DNF ni RPM.

## 6. Ubuntu

Ubuntu deriva de Debian, pero es una distribución distinta con:

- su propio ciclo de publicación;
- repositorios propios;
- selección de paquetes propia;
- políticas de soporte propias;
- herramientas y documentación específicas;
- soporte comercial de Canonical.

Que Ubuntu use paquetes DEB no significa que puedas mezclar repositorios Debian y Ubuntu.

## 7. Ubuntu LTS e interim

Ubuntu publica nuevas versiones aproximadamente cada seis meses.

Existen dos tipos principales:

```text
LTS      → Long Term Support
interim  → publicación de soporte corto
```

Las versiones LTS aparecen cada dos años y reciben cinco años de mantenimiento de seguridad estándar para el componente principal; las versiones interim tienen soporte mucho más corto, actualmente nueve meses.

En 2026 existe Ubuntu 26.04 LTS.

Fuente:
- https://ubuntu.com/project/docs/release-team/ubuntu-releases/

## 8. Ubuntu no es “Debian con otro fondo de pantalla”

Aunque comparten formato DEB y APT, pueden diferir en:

- versiones de paquetes;
- repositorios;
- parches;
- calendarios;
- defaults;
- integración del escritorio;
- kernel y hardware enablement;
- mecanismos de soporte;
- componentes de repositorio.

No añadas un repositorio Debian a Ubuntu ni uno Ubuntu a Debian salvo que documentación especializada y compatible lo indique explícitamente. Para principiantes, se consideran ecosistemas separados.

## 9. AppArmor en Ubuntu

Ubuntu documenta **AppArmor instalado y cargado por defecto**.

AppArmor es un Linux Security Module que aplica control de acceso obligatorio mediante perfiles.

Consulta de estado, si la herramienta existe:

```bash
command -v aa-status
```

y, si está disponible:

```bash
aa-status
```

No deshabilites AppArmor para “resolver” un problema sin diagnóstico.

Fuente:
- https://ubuntu.com/server/docs/security-apparmor/

## 10. Debian y AppArmor: estado predeterminado y verificación

**Debian habilita AppArmor de forma predeterminada desde Debian 10**, según su documentación oficial. Esto no significa que todas las instalaciones tengan los mismos perfiles cargados ni que el servicio esté activo en un sistema modificado. Para comprobarlo, consulta `aa-status` si la herramienta está disponible; no actives ni cambies perfiles durante la práctica.

Fuente: https://wiki.debian.org/AppArmor/HowToUse


Debian dispone de AppArmor y documentación relacionada, pero este manual **no afirmará que todas las instalaciones Debian tengan exactamente el mismo estado o conjunto de perfiles por defecto**.

La configuración puede depender de:

- versión;
- instalación;
- paquetes;
- entorno;
- decisiones del administrador.

Regla:

> consulta el sistema real; no heredes automáticamente un “default” de Ubuntu hacia Debian.

## 11. Fedora

Fedora Linux es una distribución comunitaria de evolución rápida.

En sistemas Fedora tradicionales, el software del host se distribuye principalmente en paquetes RPM y se administra con DNF.

Fedora también posee variantes basadas en imágenes, como Silverblue/CoreOS, donde el modelo de actualización del host puede usar `rpm-ostree` en lugar del flujo tradicional de DNF para el sistema base.

Por eso incluso dentro de “Fedora” debes identificar la variante antes de administrar paquetes.

Fuentes:
- https://docs.fedoraproject.org/
- https://docs.fedoraproject.org/en-US/atomic-desktops/ (Fedora Atomic Desktops User Guide; la dirección anterior `/fedora-silverblue/` redirige a esta guía, comprobado el 9 de octubre de 2026)

## 12. Fedora tradicional y paquetes

Modelo simplificado:

```text
formato/base de paquetes → RPM
gestión de alto nivel    → DNF
```

Ejemplos de consulta:

```bash
command -v dnf
command -v rpm
```

No instales nada por el simple hecho de que esos comandos existan.

## 13. Fedora image-based

En variantes image-based, el sistema host puede administrarse con un modelo transaccional o basado en imágenes.

Ejemplo de herramienta:

```text
rpm-ostree
```

Eso significa que una guía para Fedora Workstation tradicional no debe copiarse automáticamente a Fedora Silverblue o CoreOS.

Primero identifica:

```bash
cat /etc/os-release
command -v rpm-ostree
```

Las consultas son seguras; no ejecutes rebase, deploy, rollback o upgrade en esta lección.

## 14. Fedora y SELinux

Fedora utiliza SELinux ampliamente y su documentación de actualización contempla políticas y relabeling de SELinux.

Consulta, si la herramienta existe:

```bash
command -v getenforce
```

Después:

```bash
getenforce
```

Puede mostrar estados como:

```text
Enforcing
Permissive
Disabled
```

No cambies el modo de SELinux en este módulo.

## 15. RHEL

RHEL significa:

```text
Red Hat Enterprise Linux
```

Es una distribución empresarial de Red Hat con:

- ciclo de vida largo;
- documentación empresarial;
- soporte mediante suscripción según el producto;
- certificaciones e integración con ecosistemas empresariales;
- políticas de estabilidad y mantenimiento distintas a Fedora.

RHEL 10 es la rama principal actual documentada en esta edición.

Fuente:
- https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10

## 16. Ciclo de vida de RHEL

Red Hat documenta un ciclo de vida de diez años para RHEL 8, 9 y 10 a través de fases de soporte, seguido de opciones de soporte extendido.

Esto contrasta con distribuciones de cadencia mucho más rápida.

No significa que “RHEL sea viejo”: significa que prioriza previsibilidad, compatibilidad y mantenimiento empresarial dentro de una rama.

Fuente:
- https://access.redhat.com/support/policy/updates/errata

## 17. RHEL y paquetes

RHEL usa:

```text
RPM → formato/base de paquetes
DNF → herramienta de alto nivel
```

La documentación actual de RHEL 10 utiliza DNF para:

- buscar paquetes;
- consultar repositorios;
- instalar;
- actualizar;
- eliminar.

No debes asumir que un repositorio Fedora es apropiado para RHEL aunque ambos usen RPM.

## 18. Fedora y RHEL no son intercambiables

Comparten tecnologías importantes, pero no son “la misma distribución”.

Pueden diferir en:

- versiones de paquetes;
- repositorios;
- soporte;
- ciclos de publicación;
- políticas de actualización;
- certificación;
- disponibilidad de software;
- compatibilidad ABI/API según componentes.

Regla:

> un paquete RPM no es automáticamente válido para cualquier distribución que use RPM.

## 19. SELinux en RHEL

RHEL 10 documenta SELinux como parte central de su modelo de seguridad.

También integra decisiones de SELinux con systemd y servicios.

Consulta segura:

```bash
getenforce
```

si la herramienta está instalada.

No ejecutes:

```text
setenforce 0
```

como forma automática de “arreglar permisos”.

Primero diagnostica contexto, etiquetas y política.

Fuente:
- https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_selinux/

## 20. firewalld y nftables en RHEL

RHEL 10 documenta:

- `firewalld`;
- `nftables`;
- otros mecanismos de filtrado según el caso.

No estudiaremos reglas todavía.

Consulta segura:

```bash
command -v firewall-cmd
```

No abras puertos ni cambies zonas en este módulo.

Fuente:
- documentación RHEL 10 de firewalls y packet filters.

## 21. Ubuntu y firewall: no generalizar a Debian

Ubuntu documenta UFW como herramienta de firewall sencilla.

Eso **no permite afirmar** que “Debian y Ubuntu usan UFW por defecto de la misma manera”.

En este manual:

```text
Ubuntu → UFW se estudia según documentación Ubuntu
Debian → verificar herramientas/configuración reales
Fedora/RHEL → firewalld/nftables según documentación y entorno
```

La administración práctica llegará en el módulo de firewall.

## 22. systemd

Las versiones actuales principales de Debian, Ubuntu, Fedora y RHEL usan systemd ampliamente para servicios y arranque.

Herramienta:

```text
systemctl
```

Pero:

- unidades disponibles;
- presets;
- nombres de servicios;
- políticas;
- configuración;

pueden variar entre distribuciones.

No copies un nombre de servicio sin verificarlo.

## 23. Tabla comparativa principal

| Área | Debian | Ubuntu | Fedora tradicional | RHEL |
|---|---|---|---|---|
| Paquete principal | DEB | DEB | RPM | RPM |
| Alto nivel | APT | APT | DNF | DNF |
| Bajo nivel | dpkg | dpkg | RPM | RPM |
| Ciclo | stable/testing/unstable | LTS/interim | rápido | empresarial de largo ciclo |
| Seguridad MAC destacada | AppArmor habilitado por defecto desde Debian 10; verificar estado real | AppArmor documentado por defecto | SELinux | SELinux |
| Firewall | verificar entorno | UFW documentado por Ubuntu | firewalld/nftables según entorno | firewalld/nftables |
| Soporte comercial principal | no como producto empresarial único | Canonical | comunidad/proveedores diversos | Red Hat |
| Variante image-based destacada | no es el foco de esta tabla | no es el foco | Silverblue/CoreOS | existen tecnologías empresariales, fuera de este módulo |

La tabla es una orientación. Nunca sustituye consultar la versión concreta.

## 24. Misma orden, distinto contexto

Ejemplo:

```bash
systemctl status ssh
```

puede funcionar en un sistema y no en otro si el servicio se llama distinto, no está instalado o usa otra configuración.

Otro ejemplo:

```text
apt install ...
```

no corresponde a RHEL.

Y:

```text
dnf install ...
```

no corresponde a Debian estándar.

## 25. No copies rutas de repositorios entre distribuciones

Ejemplos conceptuales:

```text
Debian/Ubuntu → configuración APT
Fedora/RHEL   → configuración DNF/repositorios RPM
```

Incluso dentro de una misma familia las rutas y formatos pueden evolucionar.

Ubuntu moderno documenta fuentes en formato deb822 bajo:

```text
/etc/apt/sources.list.d/
```

Debian también admite diferentes archivos de sources.

No edites esos archivos en esta lección.

## 26. No mezcles paquetes por extensión

Un archivo termina en:

```text
.rpm
```

Eso no responde:

> ¿es compatible con mi RHEL/Fedora, versión y arquitectura?

Igualmente:

```text
.deb
```

no significa:

> funciona igual en cualquier Debian/Ubuntu.

La compatibilidad depende de más factores que la extensión.

## 27. Arquitectura también importa

Una distribución puede ofrecer paquetes para arquitecturas como:

```text
x86_64 / amd64
aarch64 / arm64
otras
```

Los nombres exactos de arquitectura pueden variar entre ecosistemas.

Consulta:

```bash
uname -m
```

y usa la herramienta de paquetes correspondiente para confirmar arquitectura de paquetes.

No descargues un paquete solo porque “parece Linux”.

## 28. Versiones de software

Fedora suele incorporar software nuevo con rapidez.

RHEL mantiene versiones dentro de una política empresarial y puede proporcionar correcciones de seguridad mediante backports sin cambiar necesariamente al número de versión más reciente que veas en upstream.

Debian stable también prioriza estabilidad durante su ciclo.

Ubuntu LTS equilibra estabilidad y mantenimiento prolongado.

Por eso:

> número de versión más alto no significa automáticamente sistema más seguro.

## 29. Backport

Un **backport** toma una corrección o cambio y lo adapta a una versión mantenida sin adoptar necesariamente toda la versión upstream nueva.

Esto es importante cuando compares:

```text
versión aparente
```

con:

```text
estado real de parches de seguridad
```

No declares una vulnerabilidad solo porque un paquete tenga un número de versión “antiguo”; consulta los avisos de seguridad de la distribución.

## 30. Fuentes de documentación correctas

Prioridad:

```text
Debian → debian.org
Ubuntu → ubuntu.com / documentation.ubuntu.com
Fedora → docs.fedoraproject.org
RHEL → docs.redhat.com / access.redhat.com
```

Una respuesta de foro puede ayudar, pero no debe reemplazar la documentación oficial para cambios de sistema.

## 31. Preparar la práctica

Ejecuta:

```bash
cat /etc/os-release
```

Localiza:

```text
ID
ID_LIKE
VERSION_ID
PRETTY_NAME
```

`ID_LIKE` puede ayudar a conocer relación con otras familias, pero no significa que ambas distribuciones sean intercambiables.

## 32. Práctica A — identificar herramientas

Ejecuta:

```bash
command -v apt
command -v dpkg-query
command -v dnf
command -v rpm
command -v rpm-ostree
```

No instales herramientas ausentes.

Completa:

```text
Mi distribución:
Mi versión:
APT:
dpkg-query:
DNF:
RPM:
rpm-ostree:
```

## 33. Práctica B — identificar seguridad MAC

Consulta únicamente disponibilidad:

```bash
command -v aa-status
command -v getenforce
```

Si existe `aa-status`, puedes consultarlo sin cambiar perfiles.

Si existe `getenforce`, puedes consultar el estado de SELinux.

No ejecutes herramientas que cambien el modo.

## 34. Práctica C — identificar firewall sin modificar

```bash
command -v ufw
command -v firewall-cmd
command -v nft
```

El objetivo es reconocer herramientas presentes.

**No ejecutes comandos para habilitar, deshabilitar, abrir puertos, cambiar zonas o recargar reglas.**

## 35. Práctica D — clasificar comandos por distribución

Clasifica:

```text
apt-cache policy bash
dpkg-query -W bash
dnf info bash
rpm -q bash
aa-status
getenforce
firewall-cmd
ufw
```

No todos son exclusivos de una sola distribución, pero debes asociarlos con el ecosistema donde este manual los estudia principalmente.

## 36. Práctica E — detectar una guía incorrecta

Supón:

```text
Sistema: Ubuntu
Guía: sudo dnf install paquete
```

Problema:

> se copió una instrucción de otra familia sin verificar.

Ahora:

```text
Sistema: RHEL
Guía: sudo apt install paquete
```

mismo error conceptual.

La solución no es traducir comandos al azar: es buscar la documentación de la distribución y versión.

## 37. Práctica F — versión y soporte

Responde sin modificar nada:

1. ¿tu distribución tiene una versión estable/LTS/major específica?
2. ¿esa versión sigue soportada?
3. ¿qué fuente oficial lo confirma?

No confíes solo en el número de versión que recuerdes.

## 38. Errores frecuentes

| Error | Problema | Corrección |
|---|---|---|
| “Ubuntu = Debian” | Comparten raíces y DEB, pero políticas y repositorios difieren | Trátalos como distribuciones distintas |
| “Fedora = RHEL” | Comparten tecnologías, no ciclo ni repositorios | Verifica distribución concreta |
| Mezclas repositorios | Riesgo de dependencias incompatibles | Usa repositorios de tu distribución |
| Paquete DEB/RPM parece compatible | Extensión no garantiza compatibilidad | Verifica distro, versión y arquitectura |
| Asumes UFW en Debian | Generalización desde Ubuntu | Inspecciona el sistema real |
| Deshabilitas SELinux/AppArmor ante un error | Eliminas control de seguridad sin diagnosticar | Investiga política y etiquetas/perfiles |
| Copias un nombre de servicio | Puede variar | Consulta unidades instaladas |
| “Versión vieja = vulnerable” | Puede haber backports | Consulta avisos oficiales |
| Usas instrucciones de otra release | Defaults y sintaxis pueden cambiar | Verifica versión |

## 39. Método antes de seguir una guía Linux

Antes de copiar una orden:

1. identifica distribución;
2. identifica versión;
3. identifica variante/edición;
4. comprueba arquitectura si aplica;
5. identifica gestor de paquetes;
6. revisa la fuente de la guía;
7. verifica que la documentación corresponda a tu versión;
8. entiende si la orden consulta o modifica;
9. revisa privilegios;
10. solo entonces ejecuta.

## 40. Práctica independiente

Sin modificar tu sistema:

1. identifica distro y versión;
2. clasifícala como Debian/Ubuntu/Fedora/RHEL u otra;
3. identifica el gestor de paquetes disponible;
4. identifica formato DEB o RPM cuando corresponda;
5. consulta qué mecanismo MAC está disponible;
6. comprueba qué herramientas de firewall existen;
7. busca en documentación oficial el ciclo de soporte de tu versión;
8. explica por qué no mezclarías repositorios de otra distribución.

## 41. Mini evaluación

1. ¿Debian y Ubuntu usan normalmente paquetes DEB?
   - A) Sí.
   - B) No.

2. ¿Eso los hace intercambiables?
   - A) Sí.
   - B) No.

3. ¿Fedora tradicional y RHEL usan RPM/DNF?
   - A) Sí.
   - B) No.

4. ¿Eso permite instalar cualquier RPM de Fedora en RHEL sin revisar?
   - A) Sí.
   - B) No.

5. ¿Ubuntu documenta AppArmor cargado por defecto?
   - A) Sí.
   - B) No.

6. ¿RHEL 10 documenta SELinux?
   - A) Sí.
   - B) No.

7. ¿Debemos asumir UFW en Debian solo porque Ubuntu lo usa?
   - A) Sí.
   - B) No.

8. ¿Una variante Fedora image-based puede usar rpm-ostree?
   - A) Sí.
   - B) No.

9. ¿Un número de versión de paquete aparentemente antiguo demuestra por sí solo que falta un parche?
   - A) Sí.
   - B) No.

10. ¿Qué debes identificar antes de copiar un comando administrativo?
   - A) Distribución y versión.
   - B) Solo que sea Linux.

## 42. Registro de aprendizaje

Puedes responder:

```text
Debian se caracteriza por:
Ubuntu se caracteriza por:
Fedora se caracteriza por:
RHEL se caracteriza por:
DEB se relaciona con:
RPM se relaciona con:
APT se relaciona con:
DNF se relaciona con:
Ubuntu documenta como MAC:
RHEL documenta como MAC:
¿Por qué no debo mezclar repositorios?:
Algo que todavía confundo:
Estado: EN APRENDIZAJE / PRACTICADO
```

## 43. Fuentes y límites

Clasificación y estado de los enlaces de esta sección: [catálogo de fuentes](auditorias/06-catalogo-fuentes.md) (jerarquía E04, comprobación del 9 de octubre de 2026).

Fuentes principales verificadas para esta edición:

**Corte de versiones: 8 de octubre de 2026.** Debian 13 «trixie» es la rama estable (actualización puntual 13.7 del 12 de septiembre de 2026); Ubuntu 26.04 LTS se publicó el 23 de abril de 2026; Red Hat documenta la rama RHEL 10, incluida la versión 10.2 publicada en mayo de 2026. Estos datos deben revisarse antes de reutilizar la guía en otra fecha. La versión mayor, la actualización puntual y el estado de soporte no son equivalentes.

- Debian Releases:
  https://www.debian.org/releases/
- Debian — anuncio de 13.7:
  https://lists.debian.org/debian-announce/2026/msg00009.html
- Ubuntu 26.04 LTS — notas oficiales:
  https://documentation.ubuntu.com/release-notes/26.04/
- Red Hat — fechas de versiones RHEL:
  https://access.redhat.com/articles/red-hat-enterprise-linux-release-dates
- Debian Reference:
  https://www.debian.org/doc/manuals/debian-reference/
- Ubuntu Releases:
  https://ubuntu.com/project/docs/release-team/ubuntu-releases/
- Ubuntu Package Management:
  https://ubuntu.com/server/docs/how-to/software/package-management/
- Ubuntu AppArmor:
  https://ubuntu.com/server/docs/security-apparmor/
- Fedora Documentation:
  https://docs.fedoraproject.org/
- Fedora software/package documentation:
  https://docs.fedoraproject.org/
- RHEL 10 Documentation:
  https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10
- RHEL 10 SELinux:
  https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_selinux/
- RHEL lifecycle:
  https://access.redhat.com/support/policy/updates/errata

Se posponen:

- migraciones entre distribuciones;
- conversiones DEB/RPM;
- pinning;
- repositorios de terceros;
- SELinux práctico;
- AppArmor práctico;
- firewall práctico;
- rpm-ostree administrativo;
- soporte empresarial y suscripciones en profundidad.

**Estado de la lección:** redactada y revisada documentalmente. Las prácticas son de identificación y consulta; no modifican configuración.

---

**Siguiente:** [Módulo 17 — systemd, unidades y servicios; otros sistemas init en contexto](modulo-17-systemd-unidades-servicios-init.md) · [Volver al índice](README.md)
