# Conclusiones

Se diseñaron y ejecutaron cinco casos de prueba de caja negra sobre SauceDemo, que cubren inicio de sesión, carrito de compras y checkout, con flujos exitosos y negativos. Los cinco casos resultaron PASS, cada uno con su captura como evidencia, y no se encontraron defectos reproducibles.

En el análisis de caja blanca se identificaron 3 decisiones y 4 condiciones simples en la función `validar_compra`. El criterio de cobertura de decisiones requiere un mínimo de 4 casos, por lo que los 3 casos iniciales resultan insuficientes y se necesita el caso adicional CB-04 para cubrir el resultado falso de D3.

Los escenarios Gherkin describen el comportamiento esperado de la aplicación en un lenguaje claro y verificable, y sirven de base para una posible automatización posterior.
