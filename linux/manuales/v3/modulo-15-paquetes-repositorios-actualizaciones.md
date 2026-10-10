# Módulo 15 — Paquetes, repositorios y actualizaciones

Manual Maestro de Linux y Shell Scripting — Edición 2026 · v3 · Decimoquinta entrega.

[Índice del manual](README.md) · [← Módulo 14](modulo-14-jobs-fg-bg-senales-kill.md) · [Arquitectura](00-indice-arquitectura.md) · [Módulo 16 →](modulo-16-debian-ubuntu-fedora-rhel.md)

## 1. Qué aprenderás

Al terminar este módulo podrás:

- explicar qué es un paquete;
- explicar qué es un repositorio;
- distinguir paquete instalado, paquete disponible y actualización;
- comprender qué son dependencias y metadatos;
- distinguir APT de dpkg en Debian/Ubuntu;
- distinguir DNF de RPM en Fedora/RHEL;
- identificar qué familia de herramientas corresponde a tu distribución;
- explicar la diferencia entre actualizar el índice y actualizar paquetes;
- consultar información de paquetes sin modificar el sistema;
- reconocer por qué añadir repositorios de terceros requiere revisión;
- diferenciar una actualización normal de paquetes de una actualización mayor de distribución.

Conocimientos previos:
- distribución y versión;
- usuarios y privilegios;
- archivos y rutas;
- procesos;
- lectura de documentación.

**Seguridad:** instalar, eliminar o actualizar paquetes modifica el sistema. En esta lección las prácticas obligatorias son de consulta. Los comandos administrativos se muestran para comprender su propósito, pero no deben ejecutarse hasta confirmar distribución, versión, respaldo apropiado, energía estable y el impacto previsto. No añadas `sudo` automáticamente.

## 2. Qué es un paquete

Un **paquete** es una unidad de distribución de software preparada para que el sistema pueda instalarla, actualizarla o retirarla de forma controlada.

Puede incluir:

- programas;
- bibliotecas;
- documentación;
- archivos de configuración;
- metadatos;
- scripts de mantenimiento.

Dos formatos importantes en las familias que estudiaremos son:

```text
.deb → Debian, Ubuntu y derivadas
.rpm → RHEL, Fedora y otras distribuciones de la familia RPM
```

El formato del paquete y la herramienta de alto nivel no son exactamente lo mismo.

## 3. Qué es un repositorio

Un **repositorio** es una fuente organizada de paquetes y metadatos.

Modelo simplificado:

```text
repositorio
├── paquetes
├── versiones
├── dependencias
└── metadatos
```

El gestor de paquetes consulta repositorios configurados para saber:

- qué software existe;
- qué versiones están disponibles;
- qué dependencias necesita;
- qué actualizaciones hay.

No confundas repositorio de paquetes con repositorio Git. Ambos almacenan contenido organizado, pero resuelven problemas diferentes.

## 4. Dependencias

Un paquete puede necesitar otros paquetes para funcionar.

Ejemplo conceptual:

```text
aplicación A
├── biblioteca B
└── biblioteca C
```

Un gestor de paquetes de alto nivel puede resolver dependencias automáticamente según los repositorios configurados.

Eso es una diferencia importante frente a copiar ejecutables manualmente sin comprender sus requisitos.

## 5. Metadatos

Los gestores no descargan siempre cada paquete completo solo para saber qué existe.

Utilizan **metadatos**, que pueden describir:

- nombres;
- versiones;
- arquitectura;
- dependencias;
- repositorio;
- descripción;
- firmas o datos relacionados con verificación.

Por eso existe una diferencia entre:

```text
actualizar información sobre paquetes
```

y:

```text
actualizar los paquetes instalados
```

## 6. Identifica primero tu distribución

Antes de copiar un comando de Internet:

```bash
cat /etc/os-release
```

Busca campos como:

```text
ID=
VERSION_ID=
PRETTY_NAME=
```

No publiques la salida completa si contiene personalizaciones privadas.

La herramienta correcta depende de la distribución y versión reales.

## 7. Familias que estudiaremos

En esta edición:

```text
Debian / Ubuntu → APT + dpkg
Fedora / RHEL   → DNF + RPM
```

Esto es una guía curricular, no una afirmación de que solo existan esas familias.

Otras distribuciones pueden usar gestores como:

- pacman;
- zypper;
- apk;
- emerge.

No mezclaremos instrucciones entre familias.

## 8. APT en Debian y Ubuntu

APT significa **Advanced Package Tool**.

En Ubuntu, la documentación oficial recomienda APT para administrar paquetes Debian y repositorios configurados.

Comandos conceptuales frecuentes:

```text
apt update
apt install
apt remove
apt upgrade
apt search
apt show
```

No todos modifican el sistema de la misma manera.

## 9. apt update NO actualiza los programas instalados

Este punto es fundamental.

```text
sudo apt update
```

actualiza el **índice local de paquetes** consultando los repositorios configurados.

No significa:

> “instala automáticamente todas las versiones nuevas de mis programas”.

Después de actualizar el índice, APT puede saber qué actualizaciones están disponibles.

**En este módulo no ejecutamos `sudo apt update` como práctica obligatoria**, porque escribe metadatos locales y requiere acceso administrativo en configuraciones habituales.

## 10. apt upgrade sí modifica paquetes instalados

Ejemplo administrativo:

```text
sudo apt upgrade
```

puede descargar e instalar versiones nuevas de paquetes instalados según la resolución de APT.

Eso cambia software del sistema.

Antes de hacerlo en un equipo real se debe considerar:

- qué paquetes cambiarán;
- cuánto se descargará;
- servicios que podrían reiniciarse;
- espacio disponible;
- energía y conectividad;
- necesidad de reinicio;
- respaldo y recuperación cuando corresponda.

No se ejecuta como práctica inicial.

## 11. apt install

Ejemplo conceptual:

```text
sudo apt install NOMBRE_PAQUETE
```

Instala un paquete y las dependencias necesarias según la resolución del gestor.

No copies nombres de paquetes al azar.

Antes de instalar:

1. identifica el paquete;
2. comprueba su origen;
3. revisa la descripción;
4. confirma qué dependencias propone;
5. verifica que corresponde a tu distribución y versión.

## 12. apt remove y purge

`apt remove` retira paquetes según las reglas de APT.

Una opción como `--purge` puede retirar también archivos de configuración administrados por el paquete.

Por eso **no debe tratarse como una limpieza inocua**.

En este módulo no eliminamos software.

## 13. apt search y apt show

Estas operaciones son útiles para investigación.

Ejemplo:

```bash
apt search bash
```

Busca paquetes relacionados con el término.

Para información de un paquete:

```bash
apt show bash
```

Dependiendo del estado de los índices, los resultados reflejan la información disponible localmente.

Estas consultas no instalan el paquete.

## 14. apt-cache

`apt-cache` permite consultar información del caché de APT.

Ejemplo seguro:

```bash
apt-cache policy bash
```

Puede mostrar:

- versión instalada;
- versión candidata;
- orígenes conocidos.

Es una buena herramienta para aprender sin modificar paquetes.

## 15. dpkg — nivel más bajo en sistemas Debian

`dpkg` administra paquetes Debian a nivel local.

Puede:

- consultar la base de paquetes;
- instalar un archivo `.deb`;
- retirar paquetes;
- listar archivos de un paquete.

Pero por sí solo no ofrece la misma resolución automática de repositorios y dependencias que APT.

Modelo:

```text
APT  → gestión de alto nivel, repositorios y dependencias
dpkg → gestión local de paquetes .deb y base instalada
```

## 16. Consultas seguras con dpkg

Puedes comprobar si `bash` aparece en la base de paquetes:

```bash
dpkg-query -W bash
```

Otra consulta:

```bash
dpkg-query -W -f='${Package}\t${Version}\n' bash
```

No necesitas memorizar todavía el formato `-f`; se muestra para distinguir nombre y versión.

Si tu sistema no es Debian/Ubuntu, no uses esta sección como práctica.

## 17. DNF en Fedora y RHEL

DNF es la herramienta de alto nivel que estudiaremos para la familia Fedora/RHEL.

La documentación oficial de RHEL 10 utiliza DNF para:

- buscar paquetes;
- consultar repositorios;
- instalar software;
- comprobar actualizaciones;
- actualizar paquetes.

Ejemplos conceptuales:

```text
dnf search
dnf info
dnf list
dnf repolist
dnf check-update
dnf install
dnf upgrade
dnf remove
```

**Nota sobre versiones:** RHEL 10 documenta DNF, mientras que Fedora 41 y posteriores emplean DNF5 (cambio [SwitchToDnf5](https://fedoraproject.org/wiki/Changes/SwitchToDnf5), comprobado el 9 de octubre de 2026). La documentación de DNF5 denomina `check-upgrade` a la comprobación de actualizaciones; no presupongas que `check-update` es un alias compatible en todas las instalaciones. Antes de aplicar ejemplos, identifica la versión con `dnf --version` y consulta la ayuda de tu distribución. Referencia: [DNF5 check-upgrade](https://dnf5.readthedocs.io/en/latest/commands/check-upgrade.8.html).

## 18. dnf search

Consulta:

```bash
dnf search bash
```

Busca el término en metadatos de paquetes disponibles para DNF.

No instala el paquete.

Si DNF necesita consultar o refrescar metadatos, puede acceder a repositorios según su configuración.

## 19. dnf info

Ejemplo:

```bash
dnf info bash
```

Puede mostrar información de paquete, como:

- nombre;
- versión;
- arquitectura;
- repositorio;
- descripción.

El formato depende de la versión de DNF.

## 20. dnf repolist

Consulta:

```bash
dnf repolist
```

muestra repositorios habilitados según la configuración.

No añadas ni habilites repositorios solo para que la salida “se vea completa”.

El número y los nombres correctos dependen de la distribución, versión, suscripción y configuración.

## 21. dnf check-update

La documentación de RHEL 10 utiliza:

```text
dnf check-update
```

para comprobar actualizaciones disponibles.

Esta operación **consulta** actualizaciones; no las instala.

La documentación oficial de DNF define estos estados de salida para `check-update`:

```text
0   → no hay actualizaciones disponibles
100 → hay actualizaciones disponibles
1   → ocurrió un error
```

Por tanto, en este comando específico:

```text
estado distinto de 0 ≠ necesariamente error
```

El valor `100` es un resultado esperado cuando DNF encuentra actualizaciones. Esto conecta directamente con el **Módulo 25 — Códigos de salida**: siempre debes interpretar un estado según la documentación del programa que lo produjo.

Ejemplo de observación:

```bash
dnf check-update
estado=$?
printf 'Estado de dnf check-update: %s\n' "$estado"
```

No confundas “hay actualizaciones disponibles” con “ya fueron instaladas”.

## 22. dnf upgrade

Ejemplo administrativo:

```text
sudo dnf upgrade
```

actualiza paquetes instalados según los repositorios y la resolución de DNF.

Es una operación que modifica el sistema.

No se ejecuta en este módulo.

En RHEL, las actualizaciones del kernel tienen manejo específico: las versiones nuevas pueden instalarse junto a kernels anteriores según las reglas de paquetes `installonly`.

## 23. RPM — nivel de paquete local

RPM es tanto un formato de paquete como una herramienta/base de gestión en sistemas de la familia RPM.

Modelo simplificado:

```text
DNF → repositorios + dependencias + operaciones de alto nivel
RPM → paquete local y base RPM
```

No instalaremos archivos RPM manualmente en este módulo.

## 24. Consultas seguras con rpm

En un sistema RPM puedes consultar si un paquete está instalado:

```bash
rpm -q bash
```

Para mostrar información:

```bash
rpm -qi bash
```

Estas consultas no instalan ni eliminan paquetes.

## 25. Repositorios oficiales y de terceros

Los repositorios oficiales de una distribución forman parte de su modelo de mantenimiento.

Un repositorio de terceros puede ser legítimo, pero añade confianza adicional:

- quién publica el software;
- quién controla la clave de firma;
- qué paquetes puede sustituir;
- qué frecuencia de actualización tiene;
- qué soporte ofrece;
- si es compatible con tu versión.

No añadas un repositorio porque una página diga simplemente:

```text
copia y pega estos comandos
```

Primero investiga su procedencia.

## 26. Firmas y confianza

Los sistemas de paquetes modernos utilizan mecanismos criptográficos para verificar procedencia e integridad de metadatos o paquetes según el diseño de la distribución.

Pero una firma válida no significa automáticamente:

> “este software es seguro para cualquier propósito”.

Una firma ayuda a comprobar autenticidad/integridad respecto a una clave confiada; no sustituye revisar qué software instalas.

## 27. No uses curl | bash para instalar software sin revisar

Una instrucción de Internet del tipo:

```text
curl ... | bash
```

descarga contenido y lo entrega directamente a una shell.

Eso combina dos riesgos:

1. ejecutas contenido remoto;
2. puedes no revisarlo antes.

En este curso no se utiliza como método normal de instalación.

Prioriza:

- repositorios oficiales;
- documentación oficial;
- paquetes identificados;
- revisión antes de ejecución.

## 28. Actualización de paquetes vs actualización de distribución

No confundas:

```text
actualizar paquetes de la versión actual
```

con:

```text
migrar a una nueva versión de la distribución
```

Por ejemplo, pasar de una versión mayor de Ubuntu o RHEL a otra puede requerir procedimientos específicos de migración.

No se hace simplemente porque exista un comando `upgrade`.

## 29. Reinicios y servicios

Una actualización puede modificar:

- bibliotecas;
- servicios;
- kernel;
- componentes de seguridad.

Algunas actualizaciones pueden requerir:

- reiniciar servicios;
- cerrar aplicaciones;
- reiniciar el sistema.

Por eso una actualización en un servidor o equipo importante se planifica.

## 30. Preparar la práctica

Primero identifica tu entorno:

```bash
cat /etc/os-release
```

Después comprueba qué herramientas existen:

```bash
command -v apt
command -v dpkg-query
command -v dnf
command -v rpm
```

No significa que debas usar todas.

Registra solo:

```text
APT disponible: sí/no
dpkg-query disponible: sí/no
DNF disponible: sí/no
RPM disponible: sí/no
```

No pegues rutas personales ni datos innecesarios.

## 31. Práctica A — si usas Debian o Ubuntu

Solo si `/etc/os-release` confirma Debian, Ubuntu o una distribución compatible cuya documentación indique APT:

```bash
apt-cache policy bash
```

Después:

```bash
dpkg-query -W bash
```

Objetivo:

- identificar versión instalada;
- reconocer que son consultas;
- no modificar el sistema.

No ejecutes `sudo apt update`, `upgrade`, `install` o `remove` como parte de esta práctica.

## 32. Práctica B — búsqueda APT

En Debian/Ubuntu:

```bash
apt search bash
```

La salida puede ser larga.

Puedes limitarla para lectura:

```bash
apt search bash | head
```

Al enviar su salida a una tubería, `apt` puede mostrar el aviso `WARNING: apt does not have a stable CLI interface`. Es una advertencia para quien escribe scripts, no un error de tu práctica. Una alternativa pensada para este uso es `apt-cache search bash | head`.

No interpretes cada coincidencia como un paquete que debes instalar.

## 33. Práctica C — si usas Fedora o RHEL

Solo si tu distribución corresponde a esta familia:

```bash
dnf info bash
```

Después:

```bash
rpm -q bash
```

Objetivo:

- comparar información de alto nivel con la base RPM;
- no instalar ni actualizar nada.

## 34. Práctica D — repositorios DNF

En Fedora/RHEL:

```bash
dnf repolist
```

Solo observa los repositorios habilitados.

No ejecutes opciones para habilitar, deshabilitar o añadir repositorios.

## 35. Práctica E — identifica qué comando modificaría el sistema

Clasifica estos ejemplos:

```text
apt-cache policy bash
apt search bash
sudo apt install paquete
sudo apt upgrade
dnf info bash
dnf repolist
sudo dnf install paquete
sudo dnf upgrade
rpm -q bash
```

Debes separar:

- consultas;
- instalaciones;
- actualizaciones.

La meta no es ejecutar los comandos administrativos.

## 36. No mezcles gestores

Ejemplo incorrecto de razonamiento:

> “En una guía dice `apt install`, así que lo usaré en RHEL.”

No.

Primero identifica:

- distribución;
- versión;
- herramienta soportada;
- repositorio apropiado.

La sintaxis parecida entre gestores no implica compatibilidad.

## 37. No instales por resolver command not found automáticamente

Si aparece:

```text
command not found
```

no respondas inmediatamente con una instalación.

Pregunta:

1. ¿escribí bien el comando?
2. ¿debería existir en esta distribución?
3. ¿la herramienta ya tiene un equivalente instalado?
4. ¿necesito realmente ese programa?
5. ¿cuál es el paquete oficial?
6. ¿qué cambios producirá instalarlo?

Esto evita llenar el sistema de herramientas innecesarias.

## 38. Paquetes y seguridad

Mantener software soportado y actualizado es importante para seguridad.

Pero “actualizar todo inmediatamente sin revisar” tampoco es una política universal para sistemas críticos.

En un equipo personal sencillo el proceso puede ser directo.

En producción se consideran:

- compatibilidad;
- pruebas;
- ventanas de mantenimiento;
- respaldo;
- rollback;
- dependencia entre servicios.

Este manual enseñará administración de forma gradual.

## 39. Historial y registros

Los gestores pueden dejar registros de operaciones.

En Ubuntu, las acciones de paquetes se registran, entre otros lugares, en archivos relacionados con dpkg/APT.

No revisaremos logs completos todavía porque pueden contener información del sistema.

El módulo de registros enseñará cómo consultar fragmentos de forma segura.

## 40. Errores frecuentes

| Error | Problema | Corrección |
|---|---|---|
| Crees que `apt update` actualiza programas | Actualiza el índice | Distingue índice de paquetes instalados |
| Ejecutas `upgrade` sin revisar | Modifica muchos paquetes | Revisa transacción y contexto |
| Mezclas APT y DNF | Pertenecen a familias distintas | Identifica distribución primero |
| Instalas un paquete por nombre parecido | Puede ser otro software | Consulta descripción y origen |
| Añades repositorio de terceros sin verificar | Amplías la cadena de confianza | Investiga proveedor y compatibilidad |
| Copias `curl ... | bash` | Ejecutas contenido remoto sin revisión | Evita ejecución directa |
| Usas sudo para consultas | Privilegios innecesarios | Consulta como usuario normal |
| Confundes paquete con repositorio | Uno es software empaquetado; otro es fuente | Separa conceptos |
| Confundes actualización de paquetes con versión mayor de distribución | Son procesos distintos | Sigue procedimiento específico |

## 41. Método seguro antes de instalar o actualizar

Antes de una operación administrativa:

1. identifica distribución y versión;
2. identifica el gestor soportado;
3. confirma repositorios;
4. consulta el paquete;
5. revisa la transacción propuesta;
6. considera espacio, energía y conectividad;
7. considera reinicios y servicios;
8. confirma respaldo/recuperación si el impacto lo justifica;
9. ejecuta solo cuando comprendes el cambio;
10. verifica el resultado.

## 42. Práctica independiente

Sin modificar el sistema:

1. identifica tu distribución;
2. detecta si tienes APT o DNF;
3. consulta información del paquete Bash con la herramienta apropiada;
4. consulta si Bash está instalado mediante `dpkg-query` o `rpm -q`, según corresponda;
5. explica qué es un repositorio;
6. explica qué es una dependencia;
7. explica la diferencia entre actualizar metadatos y actualizar paquetes;
8. indica qué comandos del módulo requieren privilegios y por qué no los ejecutaste.

## 43. Mini evaluación

1. ¿Qué es un paquete?
   - A) Una unidad gestionable de software y metadatos.
   - B) Un usuario.
   - C) Un proceso.

2. ¿Qué es un repositorio?
   - A) Una fuente organizada de paquetes y metadatos.
   - B) Un permiso.
   - C) Un PID.

3. En Ubuntu, ¿qué herramienta de alto nivel se documenta para paquetes .deb?
   - A) APT.
   - B) DNF.
   - C) RPM.

4. En RHEL 10, ¿qué herramienta de alto nivel documenta Red Hat?
   - A) DNF.
   - B) APT.
   - C) pacman.

5. ¿`apt update` instala todas las actualizaciones disponibles?
   - A) Sí.
   - B) No.

6. ¿`apt upgrade` modifica paquetes instalados?
   - A) Sí.
   - B) No.

7. ¿`dnf check-update` es lo mismo que instalar actualizaciones?
   - A) Sí.
   - B) No.

8. Si `dnf check-update` devuelve `100`, ¿significa necesariamente un error?
   - A) Sí.
   - B) No; significa que hay actualizaciones disponibles.

9. Si `dnf check-update` devuelve `0`, ¿qué significa?
   - A) No hay actualizaciones disponibles.
   - B) La instalación falló.

10. Si `dnf check-update` devuelve `1`, ¿qué significa?
   - A) Ocurrió un error.
   - B) Hay actualizaciones disponibles.

11. ¿Debes añadir repositorios de terceros sin verificar su origen?
   - A) Sí.
   - B) No.

12. ¿Es recomendable ejecutar directamente código remoto con `curl ... | bash` sin revisión?
   - A) Sí.
   - B) No.

13. ¿Una actualización de paquetes equivale siempre a migrar de versión mayor de la distribución?
   - A) Sí.
   - B) No.

## 44. Registro de aprendizaje

Puedes responder:

```text
Un paquete es:
Un repositorio es:
Una dependencia es:
APT se usa principalmente en:
DNF se usa principalmente en:
dpkg se relaciona con:
RPM se relaciona con:
apt update hace:
apt upgrade hace:
dnf check-update hace:
Estado 0 de dnf check-update significa:
Estado 100 de dnf check-update significa:
Estado 1 de dnf check-update significa:
¿Por qué no debo tratar todo estado no-cero como error sin leer la documentación del comando?:
¿Por qué no debo instalar desde un repositorio desconocido?:
Algo que todavía confundo:
Estado: EN APRENDIZAJE / PRACTICADO
```

## 45. Fuentes y límites

Clasificación y estado de los enlaces de esta sección: [catálogo de fuentes](auditorias/06-catalogo-fuentes.md) (jerarquía E04, comprobación del 9 de octubre de 2026).

Fuentes principales verificadas para esta edición:

- Ubuntu Server — Install and manage packages:
  https://ubuntu.com/server/docs/how-to/software/package-management/
- Debian — APT User's Guide y manuales de usuario:
  https://www.debian.org/doc/user-manuals
- DNF Project — Command Reference, `check-update`:
  https://dnf.readthedocs.io/en/latest/command_ref.html#check-update-command
- Red Hat Enterprise Linux 10 — Managing software with the DNF tool:
  https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_software_with_the_dnf_tool/index
- Red Hat Enterprise Linux 10 — DNF commands list:
  https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_software_with_the_dnf_tool/dnf-commands-list

Se posponen:

- instalación real de paquetes;
- eliminación real de paquetes;
- actualizaciones del sistema;
- claves y firmas en profundidad;
- pinning y prioridades;
- repositorios personalizados;
- PPAs;
- módulos de DNF;
- snapshots y rollback;
- actualizaciones automáticas;
- migraciones de versión mayor.

**Estado de la lección:** redactada y revisada documentalmente. Las prácticas administrativas reales permanecen pendientes y deben realizarse únicamente cuando se conozca la distribución y el impacto.

---

**Siguiente:** [Módulo 16 — Diferencias entre Debian, Ubuntu, Fedora y RHEL](modulo-16-debian-ubuntu-fedora-rhel.md) · [Volver al índice](README.md)
