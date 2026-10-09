# Catálogo de fuentes — Manual v3

Fecha de comprobación: **9 de octubre de 2026**. Este documento aplica el hallazgo **E04** de la [auditoría transversal](03-auditoria-transversal-completa-v3-2026-10-08.md): reúne todos los enlaces externos de los 35 módulos y clasifica cada uno según la misma jerarquía de fuentes.

## Jerarquía de fuentes (E04)

Cuando dos fuentes digan cosas distintas, manda la de nivel más bajo (1 es la más fuerte).

| Nivel | Tipo | Ejemplos en este manual |
|---|---|---|
| 1 | Proyecto original (*upstream*) | Manuales de GNU, systemd, OpenSSH (man.openbsd.org), kernel.org, Git, rsync |
| 2 | Documentación oficial de distribución o proveedor | Red Hat (RHEL 10), Debian, Ubuntu, Fedora, GitHub Docs |
| 3 | Estándar o especificación | RFC 1918, POSIX (Open Group), FHS 3.0 |
| 4 | Copia consultable o espejo de páginas man | man7.org, vimhelp.org, el espejo de iproute2 en GitHub |
| 5 | Fuente secundaria (solo si aporta contexto) | Ninguna en los módulos actuales |

**Regla sobre man7.org:** se clasifica como nivel 4 porque publica copias HTML de páginas de muchos proyectos (util-linux, procps-ng, systemd, cronie…). La página sirve para leer, pero para contrastar un cambio de versión se consulta el proyecto original.

## Cómo se comprobó

- Cada enlace se abrió desde un servicio externo (Firecrawl) y se anotó el código de respuesta y el título de la página. Este entorno de trabajo no tiene acceso directo a esos sitios.
- **"Funciona" significa que la página existe y responde.** No significa que se haya releído todo su contenido ni que respalde cada frase del módulo.
- Las afirmaciones con fecha (hallazgo **E05**) sí se contrastaron con el texto de la fuente: ver la [auditoría post-corrección](04-auditoria-postcorreccion-parcial-2026-10-08.md), séptima pasada.

## Límites de esta comprobación

- **55 enlaces quedaron sin verificar**, todos de los manuales de GNU (Bash, Coreutils, tar, grep, findutils). La verificación se detuvo porque el servicio externo agotó sus créditos. Están marcados como *No verificado*; no se presume que funcionen ni que estén rotos.
- Un enlace se comprueba en una fecha concreta. Puede romperse después.

## Correcciones hechas a partir de esta comprobación

| Módulo | Problema | Corrección |
|---|---|---|
| M22 | `vimhelp.org/reference_toc.txt.html` devolvía **404** | Sustituido por `https://vimhelp.org/#reference_toc`, el enlace que publica el propio sitio |
| M35 | El enlace «Checking integrity with AIDE» abría la portada general de *Security hardening* | Sustituido por el capítulo 7, `…/security_hardening/checking-integrity-with-aide` |
| M16 | `docs.fedoraproject.org/en-US/fedora-silverblue/` redirige | Sustituido por el destino actual, `…/en-US/atomic-desktops/` |

## Nivel 1 — Proyecto original (upstream)

108 enlaces.

| Enlace | Módulos | Estado |
|---|---|---|
| <https://aide.github.io/> | M35 | Funciona |
| <https://dnf.readthedocs.io/en/latest/command_ref.html#check-update-command> | M15, M25, M35 | Funciona |
| <https://dnf5.readthedocs.io/en/latest/commands/check-upgrade.8.html> | M15 | Funciona |
| <https://docs.kernel.org/> | M1, M2, M3, M4 | Funciona |
| <https://docs.kernel.org/filesystems/proc.html> | M5, M13 | Funciona |
| <https://docs.kernel.org/filesystems/sysfs.html> | M5 | Funciona |
| <https://firewalld.org/documentation/> | M21 | Funciona |
| <https://git-scm.com/docs/git-add> | M33 | Funciona |
| <https://git-scm.com/docs/git-commit> | M33 | Funciona |
| <https://git-scm.com/docs/git-restore> | M33 | Funciona |
| <https://git-scm.com/docs/git-status> | M33 | Funciona |
| <https://git-scm.com/docs/gitignore> | M33 | Funciona |
| <https://git.kernel.org/pub/scm/network/iproute2/iproute2.git/> | M19, M35 | Funciona |
| <https://github.com/cronie-crond/cronie> | M30 | Funciona |
| <https://github.com/systemd/systemd/blob/main/man/systemd.time.xml> | M30 | Funciona |
| <https://github.com/systemd/systemd/blob/main/man/systemd.timer.xml> | M30 | Funciona |
| <https://github.com/systemd/systemd/tree/main/man> | M30, M35 | Funciona |
| <https://github.com/util-linux/util-linux> | M34 | Funciona |
| <https://gitlab.com/procps-ng/procps/-/blob/master/man/top.1> | M13 | Funciona |
| <https://htop.dev/> | M13 | Funciona |
| <https://lists.samba.org/archive/rsync/2026-September/033395.html> | M32 | Funciona |
| <https://man.openbsd.org/ssh> | M20 | Funciona |
| <https://man.openbsd.org/ssh-keygen> | M20 | Funciona |
| <https://man.openbsd.org/ssh_config> | M20 | Funciona |
| <https://man.openbsd.org/sshd> | M20 | Funciona |
| <https://man.openbsd.org/sshd_config> | M20 | Funciona |
| <https://plocate.sesse.net/> | M10 | Funciona |
| <https://rsync.samba.org/> | M32 | Funciona |
| <https://rsync.samba.org/ftp/rsync/rsync.1> | M32 | Funciona |
| <https://tukaani.org/xz/man/xz.1.html> | M31 | Funciona |
| <https://wiki.nftables.org/> | M21 | Funciona |
| <https://www.freedesktop.org/software/systemd/man/latest/> | M35 | Funciona |
| <https://www.freedesktop.org/software/systemd/man/latest/journalctl.html> | M18 | Funciona |
| <https://www.freedesktop.org/software/systemd/man/latest/os-release.html> | M1 | Funciona |
| <https://www.freedesktop.org/software/systemd/man/latest/resolvectl.html> | M19 | Funciona |
| <https://www.freedesktop.org/software/systemd/man/latest/systemctl.html> | M17 | Funciona |
| <https://www.freedesktop.org/software/systemd/man/latest/systemd-journald.service.html> | M18 | Funciona |
| <https://www.freedesktop.org/software/systemd/man/latest/systemd.unit.html> | M17 | Funciona |
| <https://www.gnu.org/prep/maintain/html_node/GNU-and-Linux.html> | M1 | Funciona |
| <https://www.gnu.org/s/bash/manual/html_node/Bash-Builtins.html> | M2 | Funciona |
| <https://www.gnu.org/s/bash/manual/html_node/Double-Quotes.html> | M4 | Funciona |
| <https://www.gnu.org/s/bash/manual/html_node/Tilde-Expansion.html> | M1, M4 | No verificado |
| <https://www.gnu.org/s/coreutils/manual/html_node/pwd-invocation.html> | M3 | No verificado |
| <https://www.gnu.org/software/bash/manual/> | M1, M2, M3, M4, M23 | Funciona |
| <https://www.gnu.org/software/bash/manual/html_node/Bash-Builtins.html> | M28 | Funciona |
| <https://www.gnu.org/software/bash/manual/html_node/Bash-Conditional-Expressions.html> | M26 | No verificado |
| <https://www.gnu.org/software/bash/manual/html_node/Bourne-Shell-Builtins.html> | M2, M3, M4, M12, M24, M25, M26, M27, M28, M29 | No verificado |
| <https://www.gnu.org/software/bash/manual/html_node/Command-Execution-Environment.html> | M29 | No verificado |
| <https://www.gnu.org/software/bash/manual/html_node/Command-Substitution.html> | M24, M28 | No verificado |
| <https://www.gnu.org/software/bash/manual/html_node/Conditional-Constructs.html> | M26 | No verificado |
| <https://www.gnu.org/software/bash/manual/html_node/Exit-Status.html> | M25 | No verificado |
| <https://www.gnu.org/software/bash/manual/html_node/Filename-Expansion.html> | M27 | No verificado |
| <https://www.gnu.org/software/bash/manual/html_node/Interactive-Shell-Behavior.html> | M2 | No verificado |
| <https://www.gnu.org/software/bash/manual/html_node/Invoking-Bash.html> | M2, M23 | No verificado |
| <https://www.gnu.org/software/bash/manual/html_node/Job-Control-Builtins.html> | M14 | No verificado |
| <https://www.gnu.org/software/bash/manual/html_node/Job-Control.html> | M14 | No verificado |
| <https://www.gnu.org/software/bash/manual/html_node/Lists.html> | M25 | No verificado |
| <https://www.gnu.org/software/bash/manual/html_node/Looping-Constructs.html> | M27 | No verificado |
| <https://www.gnu.org/software/bash/manual/html_node/Pipelines.html> | M9, M25, M27, M29 | No verificado |
| <https://www.gnu.org/software/bash/manual/html_node/Positional-Parameters.html> | M28 | No verificado |
| <https://www.gnu.org/software/bash/manual/html_node/Process-Substitution.html> | M27 | No verificado |
| <https://www.gnu.org/software/bash/manual/html_node/Quoting.html> | M4, M24 | No verificado |
| <https://www.gnu.org/software/bash/manual/html_node/Redirections.html> | M8, M9 | No verificado |
| <https://www.gnu.org/software/bash/manual/html_node/Shell-Arithmetic.html> | M26 | No verificado |
| <https://www.gnu.org/software/bash/manual/html_node/Shell-Functions.html> | M28 | No verificado |
| <https://www.gnu.org/software/bash/manual/html_node/Shell-Operation.html> | M8 | No verificado |
| <https://www.gnu.org/software/bash/manual/html_node/Shell-Parameter-Expansion.html> | M24 | No verificado |
| <https://www.gnu.org/software/bash/manual/html_node/Shell-Parameters.html> | M24 | No verificado |
| <https://www.gnu.org/software/bash/manual/html_node/Shell-Scripts.html> | M23 | No verificado |
| <https://www.gnu.org/software/bash/manual/html_node/Signals.html> | M2 | No verificado |
| <https://www.gnu.org/software/bash/manual/html_node/The-Set-Builtin.html> | M29 | No verificado |
| <https://www.gnu.org/software/bash/manual/html_node/What-is-a-shell_003f.html> | M2 | No verificado |
| <https://www.gnu.org/software/coreutils/manual/> | M1, M2, M3, M4 | No verificado |
| <https://www.gnu.org/software/coreutils/manual/coreutils.html> | M34, M35 | Funciona |
| <https://www.gnu.org/software/coreutils/manual/html_node/Common-options.html> | M2 | No verificado |
| <https://www.gnu.org/software/coreutils/manual/html_node/File-permissions.html> | M12 | No verificado |
| <https://www.gnu.org/software/coreutils/manual/html_node/What-information-is-listed.html> | M3 | No verificado |
| <https://www.gnu.org/software/coreutils/manual/html_node/Which-files-are-listed.html> | M3 | No verificado |
| <https://www.gnu.org/software/coreutils/manual/html_node/cat-invocation.html> | M7 | No verificado |
| <https://www.gnu.org/software/coreutils/manual/html_node/chmod-invocation.html> | M12, M23 | No verificado |
| <https://www.gnu.org/software/coreutils/manual/html_node/chown-invocation.html> | M12 | No verificado |
| <https://www.gnu.org/software/coreutils/manual/html_node/cp-invocation.html> | M6 | No verificado |
| <https://www.gnu.org/software/coreutils/manual/html_node/head-invocation.html> | M7, M9 | No verificado |
| <https://www.gnu.org/software/coreutils/manual/html_node/id-invocation.html> | M11 | No verificado |
| <https://www.gnu.org/software/coreutils/manual/html_node/mkdir-invocation.html> | M1 | No verificado |
| <https://www.gnu.org/software/coreutils/manual/html_node/mktemp-invocation.html> | M29 | No verificado |
| <https://www.gnu.org/software/coreutils/manual/html_node/mv-invocation.html> | M6 | No verificado |
| <https://www.gnu.org/software/coreutils/manual/html_node/rm-invocation.html> | M6 | No verificado |
| <https://www.gnu.org/software/coreutils/manual/html_node/rmdir-invocation.html> | M6 | No verificado |
| <https://www.gnu.org/software/coreutils/manual/html_node/tail-invocation.html> | M7, M9 | No verificado |
| <https://www.gnu.org/software/coreutils/manual/html_node/touch-invocation.html> | M6 | No verificado |
| <https://www.gnu.org/software/coreutils/manual/html_node/uname-invocation.html> | M1 | No verificado |
| <https://www.gnu.org/software/coreutils/manual/html_node/wc-invocation.html> | M9 | No verificado |
| <https://www.gnu.org/software/coreutils/manual/html_node/whoami-invocation.html> | M11 | No verificado |
| <https://www.gnu.org/software/findutils/manual/html_mono/find.html> | M10 | No verificado |
| <https://www.gnu.org/software/grep/manual/grep.html> | M10 | No verificado |
| <https://www.gnu.org/software/gzip/manual/gzip.html> | M31 | Funciona |
| <https://www.gnu.org/software/tar/manual/html_chapter/Reliability-and-security.html> | M31 | No verificado |
| <https://www.gnu.org/software/tar/manual/html_section/extract-options.html> | M31 | No verificado |
| <https://www.gnu.org/software/tar/manual/tar.html> | M31 | No verificado |
| <https://www.greenwoodsoftware.com/less/> | M7 | Funciona |
| <https://www.kernel.org/pub/linux/docs/man-pages/book/man-pages-6.17.pdf> | M13 | Funciona |
| <https://www.kernel.org/pub/linux/utils/util-linux/> | M34 | Funciona |
| <https://www.netfilter.org/projects/nftables/index.html> | M21 | Funciona |
| <https://www.shellcheck.net/> | M29 | Funciona |
| <https://www.shellcheck.net/wiki/> | M29 | Funciona |
| <https://www.sudo.ws/docs/man/sudo.man/> | M12 | Funciona |
| <https://www.vim.org/> | M22 | Funciona |

## Nivel 2 — Documentación oficial de distribución o proveedor

41 enlaces.

| Enlace | Módulos | Estado |
|---|---|---|
| <https://access.redhat.com/articles/red-hat-enterprise-linux-release-dates> | M16 | Funciona |
| <https://access.redhat.com/support/policy/updates/errata> | M16 | Funciona |
| <https://docs.fedoraproject.org/> | M16 | Funciona |
| <https://docs.fedoraproject.org/en-US/atomic-desktops/> | M16 | Funciona |
| <https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens> | M33 | Funciona |
| <https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository> | M33 | Funciona |
| <https://docs.github.com/en/code-security/concepts/secret-security/push-protection> | M33 | Funciona |
| <https://docs.github.com/en/code-security/tutorials/remediate-leaked-secrets/remediating-a-leaked-secret> | M33 | Funciona |
| <https://docs.github.com/en/migrations/importing-source-code/using-the-command-line-to-import-source-code/adding-locally-hosted-code-to-github> | M33 | Funciona |
| <https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10> | M16 | Funciona |
| <https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/automating_system_administration_by_using_rhel_system_roles/configuring-the-systemd-journal-by-using-rhel-system-roles> | M18 | Funciona |
| <https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/configuring_firewalls_and_packet_filters/> | M21 | Funciona |
| <https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/configuring_firewalls_and_packet_filters/getting-started-with-nftables> | M21 | Funciona |
| <https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_file_systems/mounting-file-systems> | M34 | Funciona |
| <https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_file_systems/persistently-mounting-file-systems> | M34 | Funciona |
| <https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_software_with_the_dnf_tool/dnf-commands-list> | M15 | Funciona |
| <https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_software_with_the_dnf_tool/index> | M15 | Funciona |
| <https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_software_with_the_dnf_tool/updating-rhel-content> | M35 | Funciona |
| <https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/risk_reduction_and_recovery_operations/managing-and-monitoring-security-updates> | M35 | Funciona |
| <https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/risk_reduction_and_recovery_operations/troubleshooting-problems-by-using-log-files> | M18 | Funciona |
| <https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/security_hardening/> | M35 | Funciona |
| <https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/security_hardening/checking-integrity-with-aide> | M35 | Funciona |
| <https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/security_hardening/managing-sudo-access> | M35 | Funciona |
| <https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_selinux/> | M16 | Funciona |
| <https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_systemd_unit_files_to_customize_and_optimize_your_system/> | M30 | Funciona |
| <https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_systemd_unit_files_to_customize_and_optimize_your_system/managing-system-services-with-systemctl> | M17 | Funciona |
| <https://documentation.ubuntu.com/release-notes/26.04/> | M16 | Funciona |
| <https://documentation.ubuntu.com/security/security-features/network/firewall/> | M21 | Funciona |
| <https://fedoraproject.org/wiki/Changes/SwitchToDnf5> | M15 | Funciona |
| <https://lists.debian.org/debian-announce/2026/msg00009.html> | M16 | Funciona |
| <https://ubuntu.com/project/docs/release-team/ubuntu-releases/> | M16 | Funciona |
| <https://ubuntu.com/server/docs/firewalls/> | M21 | Funciona |
| <https://ubuntu.com/server/docs/how-to/software/package-management/> | M15, M16 | Funciona |
| <https://ubuntu.com/server/docs/security-apparmor/> | M16 | Funciona |
| <https://wiki.debian.org/AppArmor/HowToUse> | M16 | Funciona |
| <https://wiki.debian.org/systemd/> | M17 | Funciona |
| <https://wiki.debian.org/systemd/documentation> | M17 | Funciona |
| <https://www.debian.org/doc/manuals/debian-reference/> | M1, M2, M3, M4, M16 | Funciona |
| <https://www.debian.org/doc/user-manuals> | M15 | Funciona |
| <https://www.debian.org/intro/about> | M1 | Funciona |
| <https://www.debian.org/releases/> | M16 | Funciona |

## Nivel 3 — Estándar o especificación

3 enlaces.

| Enlace | Módulos | Estado |
|---|---|---|
| <https://pubs.opengroup.org/onlinepubs/9799919799/utilities/V3_chap02.html#tag_19_07> | M8 | Funciona |
| <https://refspecs.linuxfoundation.org/FHS_3.0/fhs/index.html> | M5 | Funciona |
| <https://www.rfc-editor.org/rfc/rfc1918.html> | M19 | Funciona |

## Nivel 4 — Copia consultable o espejo de páginas man

30 enlaces.

| Enlace | Módulos | Estado |
|---|---|---|
| <https://github.com/iproute2/iproute2> | M19 | Funciona |
| <https://man7.org/linux/man-pages/man1/getent.1.html> | M19 | Funciona |
| <https://man7.org/linux/man-pages/man1/kill.1.html> | M14 | Funciona |
| <https://man7.org/linux/man-pages/man1/man.1.html> | M2 | Funciona |
| <https://man7.org/linux/man-pages/man1/ps.1.html> | M13 | Funciona |
| <https://man7.org/linux/man-pages/man1/systemctl.1.html> | M30 | Funciona |
| <https://man7.org/linux/man-pages/man1/systemd-analyze.1.html> | M30 | Funciona |
| <https://man7.org/linux/man-pages/man2/execve.2.html> | M23 | Funciona |
| <https://man7.org/linux/man-pages/man2/kill.2.html> | M14 | Funciona |
| <https://man7.org/linux/man-pages/man5/acl.5.html> | M12 | Funciona |
| <https://man7.org/linux/man-pages/man5/crontab.5.html> | M30 | Funciona |
| <https://man7.org/linux/man-pages/man5/fstab.5.html> | M34 | Funciona |
| <https://man7.org/linux/man-pages/man5/group.5.html> | M11 | Funciona |
| <https://man7.org/linux/man-pages/man5/passwd.5.html> | M11 | Funciona |
| <https://man7.org/linux/man-pages/man5/proc.5.html> | M13 | Funciona |
| <https://man7.org/linux/man-pages/man7/credentials.7.html> | M11 | Funciona |
| <https://man7.org/linux/man-pages/man7/path_resolution.7.html> | M4, M5 | Funciona |
| <https://man7.org/linux/man-pages/man7/signal.7.html> | M14 | Funciona |
| <https://man7.org/linux/man-pages/man7/symlink.7.html> | M5 | Funciona |
| <https://man7.org/linux/man-pages/man8/crond.8.html> | M30 | Funciona |
| <https://man7.org/linux/man-pages/man8/findmnt.8.html> | M34 | Funciona |
| <https://man7.org/linux/man-pages/man8/ip-address.8.html> | M19 | Funciona |
| <https://man7.org/linux/man-pages/man8/ip-route.8.html> | M19 | Funciona |
| <https://man7.org/linux/man-pages/man8/ip.8.html> | M19 | Funciona |
| <https://man7.org/linux/man-pages/man8/lsblk.8.html> | M34 | Funciona |
| <https://man7.org/linux/man-pages/man8/mount.8.html> | M34 | Funciona |
| <https://man7.org/linux/man-pages/man8/ss.8.html> | M19, M35 | Funciona |
| <https://vimhelp.org/> | M22 | Funciona |
| <https://vimhelp.org/#reference_toc> | M22 | Funciona |
| <https://vimhelp.org/usr_toc.txt.html> | M22 | Funciona |
