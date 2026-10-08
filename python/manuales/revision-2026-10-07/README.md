# Revisión del Manual Maestro de Python — Edición 2026

Fecha local de trabajo: 7 de octubre de 2026 (America/Monterrey).
Estado: **EN REVISIÓN. No certificado para publicación.**

## Resultado concreto

Se creó una copia nativa en la misma carpeta de Drive y se aplicaron 80 reemplazos puntuales de texto, una corrección de estilo de párrafo y una bibliografía con 15 fuentes oficiales enlazadas. Estos números cuentan operaciones de edición, no 80 errores independientes. La lectura posterior confirmó los textos corregidos y las 15 fuentes. Se conserva una pestaña y las 15 partes.

- [Original conservado](https://docs.google.com/document/d/1bnq3aU8OckimfOvLyH3jTcramXy5hbL5Krj59jOXiUM/edit)
- [Copia de trabajo En revisión](https://docs.google.com/document/d/1TnvoZFzpM-nQSQbeDGhZhLNLJE_ir_WNzqJm4JJIDhQ/edit)

La revisión del original antes y después coincide: no se sobrescribió. El texto completo de la copia se guarda en manual-en-revision.txt como instantánea para comparar cambios; no sustituye el formato nativo de Google Docs y no es un programa ejecutable.

## Alcance y límites

Se contrastaron los hallazgos concretos de los dos informes proporcionados con los fragmentos actuales del original. Se verificaron fuentes oficiales y se ejecutaron pruebas focalizadas. **No se afirma una auditoría independiente exhaustiva, línea por línea, de los 15 capítulos ni la ejecución de todos sus ejemplos.**

Las pruebas se ejecutaron en **CPython 3.12.14, Linux**. Las afirmaciones sobre Python 3.14/3.15 e instalación en Windows/macOS se contrastaron documentalmente; no se ejecutaron instaladores ni se probaron en esos sistemas.

La exportación de control previa a la bibliografía produjo 115 páginas. Se inspeccionaron visualmente las páginas 2, 3, 4, 81 y 91. Esto es una muestra, no una aprobación visual completa. La bibliografía agregada posteriormente todavía requiere comprobación en la exportación final.

## Lista maestra consolidada

| Grupo | Ubicación | Estado y acción |
|---|---|---|
| Instalación y comandos | I, XI | Corregidos por plataforma. Python Install Manager también admite python: no se presenta py como única opción válida. |
| Ejecución y sintaxis | I, X | Corregida la explicación de CPython y el repaso; precisado el alcance de except. |
| Nombres, referencias y alcance | II, VII, XIII | Corregidas afirmaciones de destrucción automática y ámbito global. |
| bool y división entera | II–III | Añadidos casos de cadena no vacía, negativos y resultado float de //. |
| Edad y clasificación de signo | II, IV | Edad aproximada identificada; solución con positivo, negativo y cero. |
| Tuplas | V | Coma, tupla unitaria y mutabilidad de objetos contenidos. |
| capitalize y float | VIII | Corregido comentario; formato .2f y explicación de representación aproximada. |
| Línea convertida en título | VIII, §19 | Cambiada de HEADING_2 a NORMAL_TEXT y tipografía de código. |
| Archivos y rutas | IX | Cierre, w frente a write, CWD, rutas ilustrativas por plataforma y __file__. |
| UTF-8 | IX | Explicación condicionada por versión y configuración, con PEP 686. |
| Descuento | X, §4 | Fórmula corregida y operaciones explicadas; el ejemplo incorrecto permanece identificado como error didáctico. |
| Importación | XI | Eliminada justificación de memoria; corregido sombreado y descripción de búsqueda. |
| venv | XI | Base, copia/enlace, activación opcional, comprobación de intérprete y opción PowerShell. |
| POO | XII | return de Perro y llamada actualizada; objeto clase, atributos y self. |
| Iterable / iterador | XIII | Diferenciados iter(), next() y agotamiento. |
| deepcopy y tiempo | XIV | Eliminada promesa de independencia total; perf_counter para intervalos. |
| Progresión | XIV–XV | Marcadas como opcionales/avanzadas, sin adelantar las clases. |
| Idioma y numeración | X, XI, XIII | naturally, calculated, anidades y salto de comentario corregidos. |
| 130 marcadores U+E907 | XIII–XV | Preservados. El lector los identifica como controles opacos; no establece su semántica. No es válido concluir solo por el carácter que sean residuos eliminables. Las páginas avanzadas muestreadas muestran bloques de código nativos. |
| Barras y asteriscos señalados en primer informe | V, I, XII | No se hizo eliminación global: los fragmentos leídos no justifican borrar esos símbolos, que además tienen significado en Python. |
| Recordatorio ético con Markdown visible | XV | Pendiente de ajuste visual localizado; conservar contenido. |
| Temas mencionados sin desarrollo | XIV–XV | Se señalaron requisitos y carácter introductorio; siguen pendientes ejemplos/ejercicios adicionales donde falten. |
| Videos y procedencia original | Todo el manual | No se inventaron videos ni atribuciones. La bibliografía añadida documenta esta corrección, no todas las fuentes históricas. |

## Prioridad y dictamen

Los errores conceptuales corregidos se tratan como IMPORTANTES por su efecto en el aprendizaje; no se infló su clasificación como peligros críticos. La tipografía y el ejemplo neutral alternativo son decisiones editoriales, salvo que impidan leer o ejecutar el código.
No se emite un conteo global de hallazgos críticos/importantes del manual: requeriría la auditoría exhaustiva aún pendiente.

La copia contiene correcciones verificadas, pero **no es una edición final ni apta para publicación certificada** por esta revisión parcial.

## Pruebas reproducibles

Desde esta carpeta, ejecutar:
- Windows: py comprobar_correcciones.py
- macOS/Linux: python3 comprobar_correcciones.py

Resultado observado: **12 pruebas, todas correctas**. Cubren división, bool, tuplas, descuento, float, capitalize, polimorfismo, atributos, iteradores, deepcopy, archivos/rutas y sintaxis antes de ejecución.
Además se ejecutaron los bloques corregidos de clasificación (-5, 0 y 5) y censura, con sus salidas esperadas.
No se ejecutó código de red, intrusión ni instalaciones de paquetes extraídos del manual.

## Registro de cambios y fuentes

cambios.json contiene fragmento original, reemplazo, motivo, fuente y posición de origen para cada una de las 80 ediciones. Las posiciones corresponden a la copia antes de editar: no son índices reutilizables sobre la versión actual.
La conversión posterior de URLs a etiquetas enlazadas y la bibliografía son modificaciones de presentación adicionales.

- [Instalación de Python en Windows](https://docs.python.org/3.14/using/windows.html)
- [Uso de Python en macOS](https://docs.python.org/3.14/using/mac.html)
- [Tipos incorporados, bool y operadores](https://docs.python.org/3.14/library/stdtypes.html)
- [Modelo de datos y referencias](https://docs.python.org/3.14/reference/datamodel.html)
- [Tuplas y estructuras de datos](https://docs.python.org/3.14/tutorial/datastructures.html)
- [Errores y excepciones](https://docs.python.org/3.14/tutorial/errors.html)
- [Representación de punto flotante](https://docs.python.org/3.14/tutorial/floatingpoint.html)
- [Lectura, escritura y cierre de archivos](https://docs.python.org/3.14/tutorial/inputoutput.html)
- [Rutas con pathlib](https://docs.python.org/3.14/library/pathlib.html)
- [PEP 686: modo UTF-8 predeterminado](https://peps.python.org/pep-0686/)
- [Módulos y búsqueda de importaciones](https://docs.python.org/3.14/tutorial/modules.html)
- [Entornos virtuales con venv](https://docs.python.org/3.14/library/venv.html)
- [Clases, ámbitos e iteradores](https://docs.python.org/3.14/tutorial/classes.html)
- [Copia superficial y profunda](https://docs.python.org/3.14/library/copy.html)
- [Medición de intervalos con time](https://docs.python.org/3.14/library/time.html)

## Cierre pendiente

1. Revisar todos los ejemplos y soluciones, diferenciando errores deliberados de errores accidentales.
2. Comprobar el resultado en Python 3.14 y los comandos de Windows/macOS en sus plataformas.
3. Identificar los controles opacos antes de cualquier eliminación; conservar el original siempre.
4. Revisar visualmente todas las páginas de la exportación final, en especial sangría, corte de bloques, títulos, tablas y bibliografía.
5. Completar ejercicios de temas avanzados donde falten, conservando el contenido previo.
6. Registrar cualquier nuevo cambio y volver a verificar los puntos afectados.

Las clases conservan su secuencia actual. Esta revisión no acredita que el estudiante haya estudiado los temas avanzados.
