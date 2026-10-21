# Examen-Hito-3-TQA

**Examen práctico · Hito 3 — Testing & Quality Assurance (TQA)**

- **Estudiante:** Daner Coaquira García
- **Docente:** [Nombre del docente]
- **Aplicación bajo prueba:** Swag Labs (SauceDemo) — https://www.saucedemo.com/
- **Fecha:** 20 de octubre de 2026

## Propósito

Aplicar técnicas de prueba (caja negra y caja blanca), redactar escenarios Gherkin, registrar defectos y organizar todo el trabajo en un repositorio versionado con Git.

## Resumen de resultados

| Caso | Título | Tipo | Estado |
| --- | --- | --- | --- |
| [TC-001](docs/casos_caja_negra.md) | Inicio de sesión exitoso con usuario válido | Funcional | PASS |
| [TC-002](docs/casos_caja_negra.md) | Inicio de sesión con credenciales inválidas | Negativa | PASS |
| [TC-003](docs/casos_caja_negra.md) | Agregar un producto al carrito | Funcional | PASS |
| [TC-004](docs/casos_caja_negra.md) | Validación de campos obligatorios en el checkout | Negativa | PASS |
| [TC-005](docs/casos_caja_negra.md) | Completar una compra de extremo a extremo | Funcional | PASS |

- **Caja negra:** 5 casos ejecutados, **5 PASS**.
- **Defectos:** ninguno reproducible (ver [`bugs/bugs_encontrados.md`](bugs/bugs_encontrados.md)).
- **Caja blanca:** función `validar_compra` con 3 decisiones y 4 condiciones simples; criterio de **cobertura de decisiones**, mínimo **4 casos** (CB-01 a CB-04; CB-05 solo para cobertura de condiciones).
- **Gherkin:** 2 funcionalidades, 5 escenarios.

## Estructura del repositorio

```text
Examen-Hito-3-TQA/
├── README.md
├── docs/
│   ├── casos_caja_negra.md
│   ├── analisis_caja_blanca.md
│   ├── escenarios_gherkin.md
│   └── conclusiones.md
├── bugs/
│   └── bugs_encontrados.md
├── codigo/
│   ├── validar_compra.py
│   └── test_validar_compra.py
├── evidencias/
│   └── capturas/
│       └── evidencia_TC00X_01.png   (5 capturas)
└── entregable/
    └── informe_hito3.pdf
```

## Documentos

| Documento | Contenido |
| --- | --- |
| [`docs/casos_caja_negra.md`](docs/casos_caja_negra.md) | Los 5 casos de caja negra con plantilla de diseño y ejecución |
| [`docs/analisis_caja_blanca.md`](docs/analisis_caja_blanca.md) | Análisis de cobertura y casos CB-01 a CB-05 |
| [`docs/escenarios_gherkin.md`](docs/escenarios_gherkin.md) | Escenarios BDD (Feature / Scenario / Given / When / Then) |
| [`bugs/bugs_encontrados.md`](bugs/bugs_encontrados.md) | Registro de defectos y plantilla de reporte |
| [`entregable/informe_hito3.pdf`](entregable/informe_hito3.pdf) | Informe final consolidado |

## Ejecutar las pruebas de caja blanca

```bash
cd codigo
python -m unittest -v
```
