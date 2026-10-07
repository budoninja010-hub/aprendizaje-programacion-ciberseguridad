# Clase 02 — División, división entera y módulo

## Objetivo

Distinguir tres operadores de Python que pueden parecer similares pero producen resultados distintos.

## División normal: `/`

Devuelve el resultado de la división y puede incluir decimales.

```python
14 / 4
# 3.5
```

## División entera: `//`

Devuelve cuántas veces cabe completamente el divisor.

```python
14 // 4
# 3
```

## Módulo: `%`

Devuelve el residuo de la división.

```python
14 % 4
# 2
```

## Ejemplo completo

```python
numero = 23

print(numero / 5)   # 4.6
print(numero // 5)  # 4
print(numero % 5)   # 3
```

## Par o impar

Si un número dividido entre 2 tiene residuo 0, es par.

```python
28 % 2
# 0 -> par
```

## Corrección importante

`19 / 2` es `9.5`, no `9`. Esta diferencia ayuda a distinguir `/` de `//`:

```python
19 / 2   # 9.5
19 // 2  # 9
```
