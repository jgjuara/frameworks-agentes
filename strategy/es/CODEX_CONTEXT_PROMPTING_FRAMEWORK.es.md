# Marco: niveles de contexto y prompting para Codex

**Resumen:** Este marco convierte la revisión de evidencia en un modelo operativo para equipos de investigación. Define cinco niveles de contexto, cuándo usar cada nivel, qué poner en el prompt, qué pertenece a instrucciones persistentes y cómo decidir si una tarea de Codex está lista para ejecutarse. La regla principal es que la longitud del prompt debería escalar con riesgo y ambigüedad, mientras que la verificación debería ser obligatoria para toda salida computable.

## 1. Principio

Darle a Codex el **mínimo contexto de prompt que haga probable que el primer plan sea correcto**, y los **criterios de verificación más concretos disponibles**.

Esto separa dos preocupaciones:

- **Suficiencia de contexto:** Codex puede entender la tarea, encontrar los archivos relevantes y evitar acciones prohibidas.
- **Suficiencia de verificación:** Codex puede saber si la solución funciona.

Cuando entren en conflicto, preferir verificación más fuerte antes que explicación más larga.

## 2. Niveles de contexto

### Nivel 0: solo comando

Usar para acciones simples, reversibles y locales.

Tamaño del prompt: 1-3 oraciones.

Ejemplo:

```text
Run the existing test suite and summarize failures. Do not edit files.
```

Verificación requerida: salida del comando.

### Nivel 1: contrato mínimo de tarea

Usar para arreglos pequeños o explicaciones.

Tamaño del prompt: 100-300 palabras.

Incluir:

- Objetivo.
- Ruta o síntoma relevante.
- Condición de finalización.
- Cualquier acción prohibida.

Ejemplo:

```text
Find why `uv run pytest tests/test_parser.py` fails and fix only the parser code or the test if the test is stale. Keep the public API unchanged. Done when that test file passes and you summarize the cause.
```

### Nivel 2: tarea verificable estándar

Usar para la mayoría del trabajo de research-code.

Tamaño del prompt: 200-800 palabras.

Incluir:

- Misión.
- Archivos o directorios relevantes.
- Restricciones.
- Comando de validación.
- Respuesta final esperada.

Ejemplo:

```text
Implement a reproducible CSV cleaning step for the survey pipeline.

Relevant files:
- `src/cleaning/`
- `tests/test_cleaning.py`
- `data/schema/survey_schema.yml`

Constraints:
- Do not modify raw data.
- Keep transformations explicit and logged.
- Use existing project patterns.

Done when:
- `uv run pytest tests/test_cleaning.py` passes.
- The output schema matches `data/schema/survey_schema.yml`.
- The final response lists assumptions and any dropped rows.
```

### Nivel 3: tarea de investigación de alto contexto

Usar para cambios multiarchivo, análisis sensibles al método o tareas que pueden afectar hallazgos.

Tamaño del prompt: 800-1.500 palabras.

Incluir:

- Pregunta de investigación.
- Hipótesis u objetivo de análisis.
- Procedencia de datos.
- Restricciones de métodos.
- Artefactos de salida.
- Requisitos de reproducibilidad.
- Clase de riesgo y disparadores de escalamiento.

Verificación requerida:

- Comando end-to-end.
- Inspección de artefactos.
- Nota metodológica.
- Revisión de fuerza de afirmaciones.

### Nivel 4: paquete gobernado de tarea

Usar para datos sensibles, sistemas externos, publicación pública, seguridad, legal, medicina, finanzas o trabajo con impacto en política pública.

Tamaño del prompt: el necesario, pero dividido entre:

- `AGENTS.md` para reglas estables.
- Brief de tarea para misión y criterios de aceptación.
- Protocolo o archivo de gobernanza separado para política.
- Revisión humana fuera de Codex.

Codex no debería ser el único decisor para Nivel 4.

## 3. Qué va dónde

| Información | Poner en prompt | Poner en `AGENTS.md` | Poner en skill | Dejar que Codex descubra |
|---|---|---|---|---|
| Objetivo puntual de tarea | Sí | No | No | No |
| Comandos de setup del repositorio | Usualmente no | Sí | Quizás | Sí |
| Salida actual de prueba fallida | Sí | No | No | No |
| Reglas estables de manejo de datos | No | Sí | Quizás | No |
| Flujo repetido de revisión de literatura | No | Quizás | Sí | No |
| Detalles del issue actual | Sí | No | No | Quizás |
| Contenido de archivos | Solo si es pequeño y crítico | No | No | Sí |
| Documentos grandes | Link o sección citada | No | Quizás | Sí |
| Datos externos vivos | No, usar conector/herramienta si está aprobado | No | Quizás | Sí |
| Criterios de aceptación | Sí | Quizás, como estándar general | Quizás | No |

## 4. Rúbrica de preparación del prompt

Puntuar cada tarea de 0 a 2.

| Criterio | 0 | 1 | 2 |
|---|---|---|---|
| Objetivo | actividad vaga | artefacto nombrado | artefacto y uso nombrados |
| Contexto | ausente o volcado | algunas rutas relevantes | rutas/fuentes curadas y priorizadas |
| Restricciones | ninguna | amplias | acciones permitidas/prohibidas explícitas |
| Verificación | ausente | genérica | comando ejecutable o rúbrica verificable |
| Riesgo | ignorado | implícito | clase explícita y disparadores de escalamiento |
| Alcance | abierto | algo acotado | acotado por archivos, comportamiento o artefacto |
| Evidencia final | no solicitada | resumen solicitado | paquete de evidencia especificado |

Puntaje mínimo:

- R0: 6/14.
- R1: 8/14.
- R2: 10/14.
- R3: 12/14.
- R4: revisión gobernada requerida.

## 5. Reglas de orden para el contexto

El orden importa porque el uso de long-context puede ser sensible a la posición.

Orden recomendado:

1. Misión.
2. Criterios de aceptación.
3. Rutas relevantes y prioridad de fuentes.
4. Restricciones y acciones prohibidas.
5. Fallas conocidas o ejemplos.
6. Disparadores de escalamiento.
7. Requisitos de respuesta final.

Si un detalle es crucial, no enterrarlo en el medio de un párrafo largo. Ponerlo cerca del inicio o en una sección etiquetada.

## 6. Esqueleto default de prompt

```markdown
# Tarea de Codex

## Misión
[Entregable concreto.]

## Contexto
- `[path]`: [por qué importa]
- `[path]`: [por qué importa]

## Restricciones
- [Regla de arquitectura, datos, dependencias, privacidad o alcance.]

## Acciones permitidas
- [Permisos de lectura/edición/ejecución.]

## Prohibido sin aprobación
- [Acción destructiva, externa, irreversible, sensible o de alto costo.]

## Terminado cuando
- [ ] [Criterio ejecutable u observable.]
- [ ] [Criterio ejecutable u observable.]

## Escalar si
- [Conflicto, ambigüedad, dato faltante o acción insegura.]

## Respuesta final
Reportar archivos cambiados, comandos de validación y resultados, supuestos y riesgos residuales.
```

## 7. Defaults del equipo

Para este contexto de equipo de investigación, usar estos defaults salvo que el brief de tarea diga lo contrario:

- Usar `uv` para ejecución y gestión de dependencias Python.
- Preservar datos crudos.
- Preferir scripts reproducibles antes que estado manual de notebooks.
- Declarar supuestos y limitaciones.
- No introducir nuevas dependencias de producción sin aprobación.
- No publicar, enviar emails, hacer push ni llamar servicios externos sin aprobación.
- Usar un hilo de Codex por tarea.
- Compactar o bifurcar cuando el contexto se vuelva mayormente histórico.

## 8. Regla de decisión

Al decidir si agregar más contexto, preguntar:

1. ¿Esto cambiará el plan de implementación?
2. ¿Esto evitará un error previsible?
3. ¿Esto hará la validación más objetiva?
4. ¿Codex puede recuperar esto de forma segura?

Agregar el contexto solo si la respuesta a 1, 2 o 3 es sí y a 4 es no.

## 9. Base de fuentes

Este marco se basa en buenas prácticas de OpenAI Codex, documentación de OpenAI Codex prompting y `AGENTS.md`, evidencia de SWE-bench/SWE-agent/Agentless, investigación sobre long-context y guía oficial de GitHub y Anthropic para agentes de código. Las citas completas están en `CODEX_CONTEXT_PROMPTING_EVIDENCE.es.md`.

