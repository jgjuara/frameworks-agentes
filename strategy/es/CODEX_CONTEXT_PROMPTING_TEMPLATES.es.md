# Templates: prompts de Codex para tareas de investigación verificables

**Resumen:** Este archivo ofrece templates reutilizables de prompt para equipos de investigación que usan Codex en tareas computables. Los templates operacionalizan la recomendación del informe: mantener prompts compactos, hacer explícito el contexto, definir la verificación antes de ejecutar y exigir un paquete final de evidencia.

## 1. Tarea verificable estándar

~~~markdown
# Tarea de Codex

## Misión
[¿Construir/arreglar/analizar exactamente qué?]

## Contexto
- `[path]`: [por qué es relevante]
- `[path]`: [por qué es relevante]
- Falla o síntoma conocido: [comando/salida/comportamiento]

## Restricciones
- [Regla de alcance.]
- [Regla de arquitectura/datos/dependencias.]

## Acciones permitidas
- Leer archivos relevantes del repositorio.
- Editar archivos bajo `[paths]`.
- Ejecutar `[commands]`.

## Prohibido sin aprobación
- Modificar datos crudos.
- Instalar nuevas dependencias.
- Hacer push de commits, publicar salidas o llamar servicios externos.
- Eliminar archivos o ejecutar comandos destructivos.

## Terminado cuando
- [ ] `[validation command]` pasa.
- [ ] [El artefacto esperado existe o el comportamiento cambia.]
- [ ] [Supuestos y limitaciones están documentados.]

## Escalar si
- Los requisitos entran en conflicto.
- La validación no puede ejecutarse.
- La tarea requiere una acción prohibida.
- La procedencia de datos o interpretación no está clara.

## Respuesta final
Incluir archivos cambiados, comandos/resultados de validación, supuestos, limitaciones y riesgos residuales.
~~~

## 2. Tarea de análisis de investigación

~~~markdown
# Tarea de análisis de investigación

## Pregunta de investigación
[Pregunta.]

## Entregable computable
[Script, notebook, tabla, figura, salida de modelo, sección de informe.]

## Datos
- Fuente:
- Versión/fecha:
- Ubicación:
- Datos crudos inmutables: sí/no
- Campos sensibles:

## Restricciones metodológicas
- Método requerido:
- Método prohibido:
- Controles de robustez:
- Semilla aleatoria:

## Archivos relevantes
- `[path]`: [por qué es relevante]

## Reproducibilidad
Ejecutar:

```bash
[command]
```

Salidas esperadas:
- `[path]`

## Terminado cuando
- [ ] El análisis corre end-to-end.
- [ ] Las salidas son reproducibles desde comandos documentados.
- [ ] La nota metodológica indica datos, muestra, modelo, exclusiones, supuestos y limitaciones.
- [ ] Las afirmaciones están respaldadas por artefactos generados.
- [ ] No se copia información sensible en docs generadas.

## Respuesta final
Mapear cada hallazgo a evidencia, distinguir hallazgos de interpretación y listar supuestos no resueltos.
~~~

## 3. Bug fix con prueba fallida

~~~markdown
# Bug Fix

## Misión
Arreglar la falla en `[test file or command]`.

## Falla
Comando:

```bash
[failing command]
```

Salida observada:

```text
[short failure excerpt]
```

## Restricciones
- Mantener la API pública sin cambios salvo que la prueba demuestre que está mal.
- Preferir el cambio mantenible más pequeño.
- Agregar o actualizar pruebas solo si hace falta capturar el comportamiento.

## Terminado cuando
- [ ] El comando fallido pasa.
- [ ] Pasan pruebas relacionadas: `[command]`.
- [ ] La respuesta final explica causa raíz y arreglo.
~~~

## 4. Revisión de literatura para una decisión técnica

~~~markdown
# Tarea de revisión de literatura

## Decisión que debe informar
[Decisión.]

## Alcance
- Tema:
- Incluir:
- Excluir:
- Rango de fechas:

## Prioridad de fuentes
1. Papers revisados por pares.
2. Fuentes oficiales de estándares/gobierno.
3. Publicaciones técnicas o de investigación empresariales destacadas.
4. Otras fuentes solo si no hay fuentes primarias disponibles.

## Requisitos de evidencia
- Buscar fuentes actuales.
- Separar hallazgos empíricos de opinión experta.
- Identificar contradicciones y limitaciones.
- Proveer links de fuentes.

## Salida
Crear Markdown con:
- Resumen.
- Resumen ejecutivo.
- Tabla de evidencia.
- Recomendación.
- Riesgos y preguntas abiertas.
- Referencias.
~~~

## 5. Prompt plan-first

~~~markdown
# Plan First

Inspecciona el repositorio y produce un plan breve de implementación antes de editar.

No edites archivos todavía.

El plan debe incluir:
- Archivos relevantes encontrados.
- Supuestos.
- Cambios propuestos.
- Comandos de validación.
- Riesgos o preguntas.

Procede a la implementación solo después de que el plan sea aceptado o si las instrucciones de tarea permiten explícitamente continuar tras presentar el plan.
~~~

## 6. Prompt de revisión final

~~~markdown
# Revisión final

Revisa el trabajo completado contra el brief original de tarea.

Priorizar:
1. Comportamiento incorrecto o criterios de aceptación fallidos.
2. Validación débil o faltante.
3. Riesgos de filtración de datos, reproducibilidad o integridad de investigación.
4. Desvío de alcance.
5. Problemas de mantenibilidad.

Primero informar hallazgos. Para cada hallazgo, incluir severidad, archivo/línea si aplica, evidencia y arreglo recomendado.

Luego incluir:
- Estado de criterios de aceptación.
- Comandos revisados.
- Riesgos residuales.
- Decisión: aceptar, aceptar con notas, revisar o escalar.
~~~

## 7. Prompts compactos de una línea

Usarlos solo cuando `AGENTS.md` ya contiene los estándares del equipo.

```text
Fix `[failing command]`; keep changes minimal; run the targeted test; report root cause, changed files, and residual risks.
```

```text
Inspect `[path]` and explain how it works with file references; do not edit files.
```

```text
Make `[artifact]` reproducible from `[command]`; preserve raw data; document assumptions and validation results.
```

```text
Review the uncommitted diff for bugs, missing tests, scope drift, and research-integrity risks; findings first.
```

