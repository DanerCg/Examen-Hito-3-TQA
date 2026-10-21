# Registro de defectos

Los defectos se registran únicamente cuando un caso de prueba termina en **FAIL** y el comportamiento es reproducible. Si la prueba pasa, se registra PASS y no se reporta ningún defecto.

Los cinco casos de caja negra (TC-001 a TC-005) resultaron **PASS**, porque el comportamiento observado coincidió con el esperado en cada uno. Por lo tanto, **no se registran defectos reproducibles** en esta ejecución.

| Caso | Título | Estado | Defecto |
| --- | --- | --- | --- |
| TC-001 | Inicio de sesión exitoso con usuario válido | PASS | N/A |
| TC-002 | Inicio de sesión con credenciales inválidas | PASS | N/A |
| TC-003 | Agregar un producto al carrito | PASS | N/A |
| TC-004 | Validación de campos obligatorios en el checkout | PASS | N/A |
| TC-005 | Completar una compra de extremo a extremo | PASS | N/A |

## Plantilla para futuros reportes

Si en una nueva ejecución un caso termina en FAIL, usar esta estructura (y abrir un Issue con la etiqueta `bug`):

```markdown
### BUG-001 · <título descriptivo>
- **Descripción:**
- **Precondiciones y datos:**
- **Pasos para reproducirlo:**
- **Resultado esperado:**
- **Resultado actual:**
- **Evidencia:** ../evidencias/capturas/<archivo>.png
- **Severidad / prioridad:**
- **Caso relacionado:** TC-00X
```
