#!/usr/bin/env python3
"""Genera el PDF del Manual v3 a partir de los archivos Markdown de esta carpeta.

Uso: python3 generar_pdf.py
Requisitos: pandoc y Node.js con Playwright (Chromium).
Salida: manual-maestro-linux-shell-scripting-v3.pdf en esta carpeta.
"""
import pathlib
import re
import subprocess

AQUI = pathlib.Path(__file__).resolve().parent
V3 = AQUI.parent
REPO = "https://github.com/budoninja010-hub/aprendizaje-programacion-ciberseguridad/blob/main"
NOMBRE = "manual-maestro-linux-shell-scripting-v3"


def enlace(destino):
    """Convierte un enlace relativo del repositorio en uno válido dentro del PDF."""
    ruta, _, ancla = destino.partition("#")
    m = re.match(r"modulo-(\d+)-", ruta)
    if m:
        return f"#modulo-{m.group(1)}"
    if ruta == "00-indice-arquitectura.md":
        return "#arquitectura"
    if ruta == "README.md":
        return "#TOC"
    absoluta = (V3 / ruta).resolve().relative_to(V3.parents[2])
    return f"{REPO}/{absoluta.as_posix()}" + (f"#{ancla}" if ancla else "")


def preparar(archivo, ident):
    lineas = archivo.read_text(encoding="utf-8").splitlines()
    lineas[0] = f"{lineas[0]} {{#{ident}}}"
    salida = []
    for linea in lineas:
        # La navegación entre archivos no tiene sentido en un único documento.
        if linea.startswith("[Índice del manual](README.md)") or linea.startswith("**Siguiente:**"):
            continue
        linea = re.sub(r"\]\(((?!https?:|mailto:|#)[^)\s]+)\)",
                       lambda m: f"]({enlace(m.group(1))})", linea)
        salida.append(linea)
    return "\n".join(salida) + "\n"


def main():
    partes = [preparar(V3 / "00-indice-arquitectura.md", "arquitectura")]
    for modulo in sorted(V3.glob("modulo-*.md")):
        numero = re.match(r"modulo-(\d+)-", modulo.name).group(1)
        partes.append(preparar(modulo, f"modulo-{numero}"))
    fuente = AQUI / f"{NOMBRE}.md"
    fuente.write_text("\n\n".join(partes), encoding="utf-8")
    html = AQUI / f"{NOMBRE}.html"
    subprocess.run(["pandoc", str(fuente), "-f", "markdown-implicit_figures-tex_math_dollars-tex_math_single_backslash-smart-subscript-superscript", "-s",
                    "--toc", "--toc-depth=1", "--embed-resources", "--css", str(AQUI / "estilo.css"),
                    "--metadata", "title=Manual Maestro de Linux y Shell Scripting",
                    "--metadata", "subtitle=Edición 2026 · v3 · 35 módulos",
                    "--metadata", "lang=es", "--metadata", "toc-title=Índice",
                    "-o", str(html)], check=True)
    fuente.unlink()
    subprocess.run(["node", str(AQUI / "imprimir.js"), str(html), str(AQUI / f"{NOMBRE}.pdf")], check=True)
    html.unlink()


if __name__ == "__main__":
    main()
