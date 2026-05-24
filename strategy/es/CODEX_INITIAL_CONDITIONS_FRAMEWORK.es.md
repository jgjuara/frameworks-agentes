# Marco: definición de condiciones iniciales para trabajo agentic con Codex

**Resumen:** Este marco define el Start-Gate para trabajo con Codex en equipos de investigación. Su propósito es hacer explícitos misión, contexto, restricciones, criterios de éxito, herramientas y rúbrica de revisión del agente antes de que comience la ejecución. El objetivo es concentrar el juicio humano en el momento de mayor apalancamiento: antes de que Codex empiece a actuar.

## Principio

El primer prompt no debería ser una solicitud. Debería ser un **contrato de tarea**.

Un Start-Gate de alta calidad para Codex responde siete preguntas:

1. ¿Qué resultado debe existir cuando la tarea esté terminada?
2. ¿Qué fuentes son autoritativas?
3. ¿Qué restricciones no pueden violarse?
4. ¿Qué herramientas y archivos están permitidos?
5. ¿Qué cuenta como evidencia de éxito?
6. ¿Qué debería disparar un stop-and-ask?
7. ¿Qué debería contener el paquete final de revisión?

## El artefacto Start-Gate

Cada tarea no trivial de Codex debería empezar con un brief estructurado que contenga estas secciones.

### 1. Misión

Definir el entregable, no solo la actividad.

Malo:

```text
Analyze this dataset and improve the report.
```

Mejor:

```text
Produce a reproducible analysis notebook and a 2-page methods note explaining whether variable X predicts outcome Y, using only the approved dataset and existing project conventions.
```

### 2. Paquete de contexto

Proporcionar solo el contexto que Codex necesita para actuar correctamente.

Orden recomendado:

1. Propósito del repositorio o proyecto.
2. Objetivo actual de la tarea.
3. Archivos o carpetas relevantes.
4. Definiciones de dominio.
5. Restricciones conocidas.
6. Decisiones previas que no deben reabrirse.
7. Ejemplos de salida aceptable.

Evitar:

- Volcados grandes e indiferenciados de documentos.
- Instrucciones contradictorias sin prioridad.
- Contexto interesante pero no relevante para actuar.

### 3. Jerarquía de autoridad

Indicar qué fuente gana si las instrucciones entran en conflicto.

Jerarquía recomendada:

1. Políticas de sistema y seguridad.
2. `AGENTS.md` del repositorio.
3. Brief de tarea.
4. Issue o protocolo de investigación enlazado.
5. Convenciones existentes del código.
6. Preferencias de usuario indicadas durante la sesión.

Para equipos de investigación, agregar:

- El protocolo de ética vence a la conveniencia.
- El acuerdo de uso de datos vence a la velocidad de análisis.
- La reproducibilidad vence a atajos ingeniosos.

### 4. Acciones permitidas y prohibidas

Definir límites de autonomía antes de que empiece el trabajo.

Ejemplo:

```text
Allowed:
- Read repository files.
- Modify files under `analysis/` and `docs/`.
- Add focused tests or reproducibility checks.
- Run local tests and linters.

Forbidden without explicit approval:
- Deleting source data.
- Changing raw data files.
- Installing new dependencies.
- Pushing commits or opening PRs.
- Calling external APIs with project data.
- Publishing or emailing outputs.
```

### 5. Criterios de éxito

Hacer que "terminado" sea verificable.

Un criterio de aceptación útil es observable, no aspiracional.

Ejemplos:

- `uv run pytest` pasa.
- La nota metodológica incluye fuente de datos, exclusiones de muestra, especificación de modelo, limitaciones y pasos de reproducibilidad.
- La respuesta final lista archivos cambiados, comandos ejecutados, supuestos no resueltos y riesgos residuales.
- No se copia información personalmente identificable cruda en docs generadas.

### 6. Clase de riesgo

Asignar una clase de riesgo a la tarea en el intake.

| Clase | Descripción | Participación humana default |
|---|---|---|
| R0 | Exploración, resumen o planificación read-only | Solo inicio y final |
| R1 | Ediciones locales de código/docs con pruebas, sin datos sensibles | Solo inicio y final |
| R2 | Análisis de investigación que puede afectar hallazgos publicados | Inicio, controles automatizados, revisión final |
| R3 | Datos sensibles, sistemas externos, cambios irreversibles, impacto en política pública | Inicio, puertas predefinidas durante ejecución, revisión final |
| R4 | Legal, médico, financiero, safety-critical o publicación pública | Gobernanza humana fuera de Codex requerida |

### 7. Disparadores de escalamiento

El escalamiento debería ser raro, explícito y ligado al riesgo.

Codex debe detenerse y preguntar si:

- Los requisitos entran en conflicto.
- La tarea requiere una acción prohibida.
- Una falla de prueba no puede explicarse tras depuración razonable.
- Los resultados contradicen materialmente la hipótesis del usuario.
- La procedencia de datos no está clara.
- Aparecen datos sensibles en un archivo que podría commitearse o compartirse.
- El agente necesita elegir entre interpretaciones de investigación incompatibles.
- La siguiente acción es irreversible o visible externamente.

### 8. Requisitos de revisión final

Definir el paquete de revisión antes de empezar el trabajo.

Paquete final mínimo:

- Archivos cambiados.
- Resumen de cambios de comportamiento o análisis.
- Comandos ejecutados y resultados.
- Evidencia mapeada a criterios de aceptación.
- Limitaciones conocidas.
- Riesgos residuales.
- Controles siguientes recomendados.

## Activos persistentes del equipo

### `AGENTS.md`

Usar `AGENTS.md` para política estable del repositorio:

- Rol y tono.
- Arquitectura del proyecto.
- Comandos de prueba y validación.
- Reglas de manejo de datos.
- Política de dependencias.
- Idioma de documentación.
- Expectativas de revisión.

### `code_review.md`

Usar `code_review.md` para estándares de revisión final:

- Corrección.
- Reproducibilidad.
- Filtración de datos.
- Seguridad.
- Rendimiento.
- Validez estadística.
- Claridad documental.

Referenciarlo desde `AGENTS.md` para que Codex pueda aplicarlo durante `/review`.

### Skills

Promover flujos repetidos a Skills:

- Síntesis de revisión de literatura.
- Auditoría de dataset.
- Limpieza de notebook reproducible.
- Revisión de PR contra checklist de research-code.
- Redacción de nota metodológica.
- QA de instrumento de encuesta.
- Revisión de robustez estadística.

Cada skill debería tener disparadores estrechos, inputs claros y outputs explícitos.

## Rúbrica de calidad de intake

Puntuar cada brief de tarea de 0 a 2.

| Criterio | 0 | 1 | 2 |
|---|---|---|---|
| Claridad de misión | Actividad vaga | Salida nombrada | Salida y uso nombrados |
| Relevancia de contexto | Volcado o ausente | Parcialmente curado | Priorizado y enlazado |
| Restricciones | Ausentes | Algunas restricciones | Acciones permitidas/prohibidas explícitas |
| Criterios de éxito | Subjetivos | Parcialmente verificables | Totalmente verificables |
| Clase de riesgo | Ausente | Implícita | Explícita con puertas |
| Verificación | Ausente | Genérica | Comandos/rúbrica concretos |
| Revisión final | Ausente | Resumen solicitado | Paquete de revisión especificado |

Regla recomendada: no iniciar trabajo R2+ por debajo de 10/14.

## Patrón central de prompt

```text
You are working as a senior research software engineer in this repository.

Mission:
[Concrete deliverable.]

Authoritative context:
[Files, docs, assumptions, source priority.]

Allowed actions:
[Read/edit/run permissions.]

Forbidden actions:
[Actions requiring explicit approval.]

Risk class:
[R0-R4 plus reason.]

Acceptance criteria:
[Checkable criteria.]

Escalate before continuing if:
[Triggers.]

Execution requirements:
- Inspect context before editing.
- Present a short plan for non-trivial work.
- Make focused changes only.
- Run relevant validation.
- Keep an assumptions log.
- End with a final review package mapped to the acceptance criteria.
```
