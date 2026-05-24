# Playbook de revisión final para trabajo con Codex

**Resumen:** Este playbook define cómo un equipo de investigación debería revisar salidas de Codex al final del trabajo agentic. Asume que el reviewer humano no debería inspeccionar cada paso intermedio. En cambio, la revisión final debe basarse en evidencia, estar guiada por rúbrica y apoyarse en comandos reproducibles, diffs, logs y notas de riesgo.

## Propósito

La revisión final es donde la persona decide si acepta, rechaza, pide revisión o escala el trabajo. No es una revisión por intuición. Es una adjudicación contra el contrato de Start-Gate.

## Paquete final de revisión requerido

Codex debería proporcionar:

1. **Artefactos cambiados:** archivos creados, modificados o eliminados.
2. **Resumen de intención:** qué se cambió y por qué.
3. **Mapeo de aceptación:** cada criterio de aceptación y si se cumplió.
4. **Evidencia de validación:** comandos ejecutados, pruebas pasadas/fallidas, lint/type checks, capturas si aplica.
5. **Log de supuestos:** supuestos hechos porque el brief estaba incompleto.
6. **Log de riesgos:** riesgos de datos, seguridad, estadística, publicación u operación.
7. **Incertidumbre residual:** qué queda sin verificar.
8. **Decisiones humanas necesarias:** solo decisiones concretas sí/no o elegir una opción.

## Secuencia de revisión

### 1. Revisión de alcance

Preguntar:

- ¿Codex resolvió la tarea solicitada y nada materialmente no relacionado?
- ¿Los cambios se limitan a archivos esperados?
- ¿Evitó acciones prohibidas?
- ¿Preservó trabajo de usuario o equipo ya existente en el repo?

Rechazar o pedir revisión si la salida incluye features no solicitadas, refactors amplios, cambios ocultos de dependencias o cambios de datos sin explicación.

### 2. Revisión de evidencia

Preguntar:

- ¿Las afirmaciones están respaldadas por archivos, pruebas, salidas o fuentes citadas?
- ¿Los comandos son reproducibles?
- ¿Los resultados son trazables a insumos crudos?
- ¿Las fallas se reportan claramente?

Para trabajo de investigación, exigir:

- Procedencia de datos.
- Definición de muestra.
- Criterios de exclusión.
- Especificación de modelo o método.
- Controles de sensibilidad o robustez cuando sean relevantes.
- Distinción clara entre hallazgos e interpretación.

### 3. Revisión de código

Usar una postura de code-review:

- Corrección antes que estilo.
- Reproducibilidad antes que conveniencia.
- Explicitud antes que ingenio.
- Minimalidad antes que abstracción.

Revisar:

- Edge cases.
- Manejo de errores.
- Rutas de archivo y supuestos de sistema operativo.
- Cambios de dependencias.
- Determinismo y semillas aleatorias.
- Cobertura de pruebas proporcional al riesgo.
- Si el código generado sigue patrones existentes del proyecto.

### 4. Revisión de datos e integridad de investigación

Revisar:

- Que no se filtren datos crudos sensibles en logs, docs, prompts, ejemplos generados o commits.
- Que no haya mutación accidental de datos crudos.
- Que no se hayan usado APIs externas no aprobadas con datos protegidos.
- Que las afirmaciones no sean más fuertes que la evidencia.
- Que no haya p-hacking, filtrado silencioso ni grados de libertad analíticos no declarados.
- Que las limitaciones sean explícitas.

### 5. Revisión de riesgo

Mapear la salida final contra la clase de riesgo del intake.

| Riesgo | Acción de revisión |
|---|---|
| R0 | Leer salida final; verificar referencias a fuentes. |
| R1 | Inspeccionar diff y pruebas. |
| R2 | Inspeccionar métodos, reproducibilidad e interpretación. |
| R3 | Exigir segundo reviewer o aprobación del owner de dominio. |
| R4 | No aceptar mediante revisión solo de Codex; usar gobernanza formal. |

### 6. Decisión

Usar uno de cuatro resultados:

- **Aceptar:** todos los criterios materiales se cumplieron, riesgo residual aceptable.
- **Aceptar con notas:** limitaciones menores documentadas y no bloqueantes.
- **Revisar:** defectos concretos o validación faltante.
- **Escalar:** la decisión requiere autoridad de dominio, ética, legal, seguridad o publicación.

## Checklist de revisión final

```text
[ ] La salida final coincide con la misión original.
[ ] Todos los archivos cambiados son esperados.
[ ] No se tomó ninguna acción prohibida.
[ ] Los criterios de aceptación están mapeados uno por uno.
[ ] Se ejecutaron pruebas/controles o la razón de no ejecutarlos es explícita.
[ ] Las afirmaciones están respaldadas por evidencia.
[ ] Los supuestos están listados.
[ ] Los riesgos residuales están listados.
[ ] El manejo de datos sensibles es aceptable.
[ ] La interpretación de investigación no está sobredimensionada.
[ ] El reviewer puede reproducir el resultado central.
[ ] La decisión está registrada: aceptar, aceptar con notas, revisar o escalar.
```

## Revisión final asistida por Codex

Usar Codex como reviewer de segunda pasada, pero no convertirlo en aprobador responsable.

Prompts recomendados:

```text
Review the working tree against `code_review.md` and the original task brief.
Lead with bugs, regressions, missing tests, and research-integrity risks.
Do not summarize until after findings.
```

```text
Map this final output to the acceptance criteria.
Return a table with criterion, evidence, status, and residual uncertainty.
```

```text
Search the diff for accidental data leakage, hidden dependency changes, broad refactors, and claims not supported by tests or citations.
```

## Métricas para el equipo

Medir la calidad de revisión en el tiempo:

- Tasa de aceptación sin revisión.
- Defectos encontrados después de aceptar.
- Cantidad promedio de idas y vueltas por tarea.
- Porcentaje de tareas con briefs de intake completos.
- Porcentaje de tareas con validación reproducible.
- Frecuencia de escalamiento por clase de riesgo.
- Categorías comunes de contexto faltante.
- Tiempo desde Start-Gate hasta Final-Gate.

El objetivo no es cero escalamiento. El objetivo es menos interrupciones innecesarias y mejor detección de las pocas decisiones que realmente necesitan autoridad humana.
