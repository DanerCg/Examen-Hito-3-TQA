# Pruebas de caja blanca

## 1. Código analizado

Función en Python que valida si una compra puede realizarse (también en [`../codigo/validar_compra.py`](../codigo/validar_compra.py)):

```python
def validar_compra(edad, cuenta_activa, saldo, monto):
    if edad < 18:
        return "Compra no permitida: edad"
    if not cuenta_activa:
        return "Compra no permitida: cuenta"
    if saldo >= monto and monto > 0:
        return "Compra aprobada"
    return "Compra rechazada"
```

**Entradas:** `edad`, `cuenta_activa`, `saldo`, `monto`.  
**Salidas posibles:** Compra no permitida (por edad o por cuenta), Compra aprobada y Compra rechazada.

## 2. Decisiones y condiciones simples

| Decisión | Expresión | Condiciones simples | Resultado si es verdadera |
| --- | --- | --- | --- |
| D1 | `edad < 18` | C1: `edad < 18` | Compra no permitida: edad |
| D2 | `not cuenta_activa` | C2: `not cuenta_activa` | Compra no permitida: cuenta |
| D3 | `saldo >= monto and monto > 0` | C3: `saldo >= monto`<br>C4: `monto > 0` | Compra aprobada |

El código tiene **3 decisiones, 4 condiciones simples y 4 sentencias `return`**. D3 es una decisión compuesta. Como Python evalúa el operador `and` en cortocircuito, C4 solo se evalúa cuando C3 es verdadera. Si D3 es falsa, la función devuelve *Compra rechazada*.

## 3. Criterio de cobertura y mínimo de casos

**Criterio utilizado: cobertura de decisiones.** Exige que cada decisión (D1, D2 y D3) tome tanto el resultado verdadero como el falso al menos una vez. Se eligió porque es más exigente que la cobertura de sentencias y porque permite distinguirla claramente de la cobertura de condiciones, que evalúa cada condición simple por separado.

**Mínimo de casos: 4.** Cada caso de prueba recorre un único camino de ejecución, y el código tiene cuatro caminos posibles:

| Camino | Resultado de las decisiones | Salida |
| --- | --- | --- |
| P1 | D1 = verdadero | Compra no permitida: edad |
| P2 | D1 = falso, D2 = verdadero | Compra no permitida: cuenta |
| P3 | D1 = falso, D2 = falso, D3 = verdadero | Compra aprobada |
| P4 | D1 = falso, D2 = falso, D3 = falso | Compra rechazada |

D1 = verdadero solo ocurre en P1, que termina de inmediato; D2 = verdadero solo ocurre en P2; D3 = verdadero solo ocurre en P3 y D3 = falso solo ocurre en P4. Como ningún caso puede cubrir dos de estos resultados a la vez, se necesitan 4 casos. Los resultados D1 = falso y D2 = falso quedan cubiertos por P3 y P4.

Para contrastar los criterios, mínimo de casos que exige cada uno en este código:

| Criterio | Mínimo | Justificación |
| --- | --- | --- |
| Sentencias | 4 | Cada `return` está en un camino distinto, por lo que se necesita un caso por cada uno. |
| Decisiones | 4 | Se necesitan los caminos P1, P2, P3 y P4, como se explicó anteriormente. |
| Condiciones | 5 | Además de P1 y P2, C3 y C4 requieren tres casos: uno con C3 falsa, otro con C3 y C4 verdaderas, y otro con C3 verdadera y C4 falsa (monto menor o igual a 0). Por el cortocircuito, C4 falsa exige que C3 sea verdadera. |

## 4. Casos diseñados

Se diseñaron tres casos con valores de entrada concretos. Los resultados esperados se verificaron ejecutando la función en Python.

| Caso | edad | cuenta_activa | saldo | monto | Resultado esperado | Cobertura |
| --- | --- | --- | --- | --- | --- | --- |
| CB-01 | 17 | True | 100 | 50 | Compra no permitida: edad | D1 = verdadero (C1 verdadera) |
| CB-02 | 25 | False | 100 | 50 | Compra no permitida: cuenta | D1 = falso (C1 falsa); D2 = verdadero (C2 verdadera) |
| CB-03 | 30 | True | 100 | 50 | Compra aprobada | D1 = falso; D2 = falso; D3 = verdadero (C3 y C4 verdaderas) |

## 5. Evaluación de la cobertura y ajuste necesario

| Decisión | Resultado verdadero | Resultado falso | Estado |
| --- | --- | --- | --- |
| D1 | CB-01 | CB-02, CB-03 | Cubierta |
| D2 | CB-02 | CB-03 | Cubierta |
| D3 | CB-03 | No cubierto | Incompleta |

Los tres casos **no alcanzan** el criterio de cobertura de decisiones: se cubren 5 de los 6 resultados posibles de las decisiones (83 %) y queda sin ejecutar la sentencia `return "Compra rechazada"` (3 de 4 sentencias). Falta el resultado falso de D3.

**Ajuste necesario:** agregar un cuarto caso en el que el saldo sea menor que el monto, de modo que D3 sea falsa:

| Caso | edad | cuenta_activa | saldo | monto | Resultado esperado | Cobertura |
| --- | --- | --- | --- | --- | --- | --- |
| CB-04 | 30 | True | 20 | 50 | Compra rechazada | D1 = falso; D2 = falso; D3 = falso (C3 falsa) |

Con CB-01, CB-02, CB-03 y CB-04 se logra el 100 % de cobertura de decisiones y de sentencias. Si el criterio exigido fuera la cobertura de condiciones, se necesitaría además un quinto caso, **CB-05**, con edad 30, cuenta_activa True, saldo 100 y monto 0, cuyo resultado esperado es *Compra rechazada* y en el que C3 es verdadera y C4 es falsa.

## 6. Verificación en Python

Los casos CB-01 a CB-05 están automatizados en [`../codigo/test_validar_compra.py`](../codigo/test_validar_compra.py):

```bash
cd codigo
python -m unittest -v
```
