# Manual Maestro de Python: segunda pasada

Fecha: 8 de octubre de 2026.

[Documento de trabajo corregido](https://docs.google.com/document/d/1TnvoZFzpM-nQSQbeDGhZhLNLJE_ir_WNzqJm4JJIDhQ/edit).
[Original conservado](https://docs.google.com/document/d/1bnq3aU8OckimfOvLyH3jTcramXy5hbL5Krj59jOXiUM/edit).

Se completó la segunda pasada de maquetación y comprobación de ejemplos sobre la copia «En revisión». Las correcciones críticas registradas en la primera pasada permanecen. La copia es utilizable para continuar el estudio de las bases, con XIV y XV marcadas como avanzadas y opcionales. No se certifica que todos los programas sean robustos para cualquier entrada ni se presenta una validación multiplataforma ejecutada.

## Cambios de esta pasada

- Tabla comparativa: ancho total de 645 a 490 puntos, siete columnas preservadas, texto de 9.5 puntos y ajuste de márgenes internos. La tabla completa cabe en la página 24.
- Veinte párrafos explicativos de XI y XII recuperaron formato de prosa; dejaron de confundirse con instrucciones ejecutables.
- Se aplicó mantener con el siguiente a las líneas de los bloques cortos, conservando la sangría y los saltos de línea del código. Los proyectos largos pueden continuar en otra página.
- Se homogeneizó el formato de los primeros saludos, la llamada y salida de censurar_palabra y los dos ejemplos de atributos mutables de clase.
- Se corrigieron el título y la explicación de self para evitar llamarlo palabra reservada.
- import * explica nombres públicos y __all__, no solo funciones.
- La evaluación XIII distingue listas nuevas de los iteradores que devuelven map y filter.
- El proyecto de acceso por edad usa una actividad para adultos como contexto.
- Se corrigieron tamaño, estilo y paginación de los títulos bibliográficos.

Se preservaron los cambios ya presentes al reabrir el documento, incluida la bibliografía ampliada. La procedencia histórica declarada de los videos y NotebookLM no se volvió a auditar en esta pasada.

## Verificación de código

Entorno ejecutado: CPython 3.12.14, Linux. Referencia documental del manual: Python 3.14. Las instrucciones de instalación de Windows y macOS no se ejecutaron en esos sistemas.

Se inventariaron 254 bloques a partir de su formato y contexto:

- 235 se ejecutaron sin errores inesperados con entradas y archivos de prueba.
- 4 produjeron los errores didácticos previstos: TypeError, SyntaxError, IndexError y TypeError por omitir el parámetro de instancia.
- 14 son comandos de terminal, esquemas de carpetas o un comando mostrado incorrectamente dentro del intérprete; se clasificaron aparte y no se ejecutaron como programas Python.
- 1 es el bucle infinito intencional: se revisó y no se ejecutó sin límite.

Los ejemplos dependientes se ejecutaron con sus definiciones previas; los módulos de varios archivos se prepararon en carpetas temporales. El archivo de resultados conserva la salida y los errores observados. Una ejecución exitosa no equivale a verificar todas las ramas ni todas las entradas posibles.

Pasaron las 12 pruebas específicas de correcciones de la primera pasada y 10 pruebas adicionales de resultados/proyectos: saludos, atributos de clase e instancia, censura, análisis académico, generadores, argumentos, valores predeterminados, asyncio/decoradores, SHA-256 y persistencia/reporte JSON. Las pruebas adicionales incluyen fragmentos que no tenían formato monoespaciado en la extracción inicial. Los 254 bloques contrastados permanecen textualmente en la lectura final del Doc.

Para reproducir desde esta carpeta:

```sh
python ejecutar_ejemplos.py
python comprobar_correcciones.py
python comprobar_proyectos.py
```

## Revisión visual y preservación

Se inspeccionaron las 117 páginas de la primera exportación de esta pasada. Tras los últimos ajustes, se inspeccionaron las 50 páginas que cambiaron; las restantes se compararon por píxeles y eran idénticas. La exportación final tiene 116 páginas. Se comprobaron tabla completa, títulos, sangrías, continuidad de ejemplos, bibliografía y ausencia de símbolos extraños visibles en las partes avanzadas.

Permanecen 130 marcadores U+E907 en la estructura nativa. El conector los clasifica como controles opacos y no permite demostrar su semántica. No se eliminaron: la revisión renderizada no mostró esos caracteres como basura visible y se preservaron los bloques nativos. Esto no prueba qué representa internamente cada marcador.

El original conserva exactamente la revisión inicial. La copia mantiene su única pestaña, la tabla, los enlaces y los 130 marcadores.

Revisión final de la copia: `AHj4eMQbsS3AjHleFjFEasRafK9Jb7gINH6tZpc0dlTRIlXvfiAsdhRsmRM6odhs_equOba4ZvprPJBaKOJehE7URjEONn6MjjD4yBvhhRU`.

`manual-revisado.txt` es una instantánea de consulta, no un reemplazo de la maquetación nativa ni un archivo Python ejecutable. Contiene marcadores preservados.

## Fuentes contrastadas en esta pasada

- https://docs.python.org/3.14/tutorial/classes.html
- https://docs.python.org/3.14/tutorial/modules.html
- https://docs.python.org/3.14/library/functions.html

Las fuentes de la primera revisión y los materiales ya documentados se conservan dentro del Google Doc.
