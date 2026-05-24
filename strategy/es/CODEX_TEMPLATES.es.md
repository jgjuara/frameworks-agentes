# Templates para Start-Gates y revisiones finales de Codex

**Resumen:** Este archivo ofrece templates Markdown reutilizables para equipos de investigación que usan Codex. Están diseñados para reducir prompting no estructurado, mejorar la calidad del contexto inicial y hacer consistente la revisión final entre usuarios y proyectos.

## Template 1: brief de tarea Codex

```markdown
# Brief de tarea Codex

## Misión
[Describir el entregable concreto.]

## Antecedentes
[Incluir solo contexto necesario para completar la tarea.]

## Fuentes autoritativas
1. [Fuente de máxima prioridad.]
2. [Fuente de segunda prioridad.]
3. [Convenciones existentes de código/docs.]

## Archivos relevantes
- `[path]`: [por qué es relevante]
- `[path]`: [por qué es relevante]

## Acciones permitidas
- [Acción permitida.]
- [Acción permitida.]

## Acciones prohibidas sin aprobación
- [Acción prohibida.]
- [Acción prohibida.]

## Clase de riesgo
[R0/R1/R2/R3/R4] porque [motivo].

## Criterios de aceptación
- [ ] [Criterio verificable.]
- [ ] [Criterio verificable.]
- [ ] [Criterio verificable.]

## Validación requerida
- [Comando o control manual.]
- [Comando o control manual.]

## Disparadores de escalamiento
Codex debe detenerse y preguntar antes de continuar si:
- [Disparador.]
- [Disparador.]

## Requisitos de respuesta final
Incluir:
- Archivos cambiados.
- Validación ejecutada.
- Estado de criterios de aceptación.
- Supuestos.
- Riesgos residuales.
- Siguiente paso recomendado.
```

## Template 2: brief de análisis de investigación

```markdown
# Brief de análisis de investigación

## Pregunta de investigación
[Pregunta.]

## Hipótesis
[Hipótesis. Indicar si Codex debería intentar falsarla.]

## Dataset
- Fuente:
- Versión/fecha:
- Ubicación:
- Restricciones de uso de datos:
- Campos sensibles:

## Restricciones metodológicas
- Método requerido:
- Método prohibido:
- Controles de robustez requeridos:
- Formato de reporte requerido:

## Requisitos de reproducibilidad
- Entorno:
- Comandos:
- Semilla aleatoria:
- Ubicación de salida:

## Reglas de interpretación
- Distinguir asociación de causalidad.
- Reportar limitaciones.
- No hacer afirmaciones de política pública más allá de la evidencia.
- Señalar evidencia contradictoria.

## Criterios de aceptación
- [ ] El análisis corre end-to-end.
- [ ] Las salidas son reproducibles.
- [ ] La nota metodológica explica datos, muestra, modelo y limitaciones.
- [ ] Los hallazgos están respaldados por tablas/figuras/logs.
- [ ] No se expone información sensible en artefactos generados.
```

## Template 3: brief de revisión de literatura

```markdown
# Brief de revisión de literatura

## Objetivo
[Decisión que esta revisión debería informar.]

## Alcance
- Tema:
- Rango de fechas:
- Disciplinas:
- Geografías:
- Incluir:
- Excluir:

## Prioridad de fuentes
1. Papers revisados por pares.
2. Fuentes oficiales de estándares o gobierno.
3. Publicaciones top de ingeniería/investigación empresarial.
4. Blogs técnicos de alta calidad solo si no hay fuentes primarias disponibles.

## Tratamiento requerido de la evidencia
- Separar hallazgos empíricos de opinión experta.
- Declarar incertidumbre.
- Identificar contradicciones.
- Preferir revisiones sistemáticas y benchmarks cuando estén disponibles.
- Incluir links y fechas.

## Salida
- Resumen ejecutivo.
- Tabla de evidencia.
- Implicancias para nuestro equipo.
- Preguntas abiertas.
- Lista de fuentes.
```

## Template 4: solicitud de revisión final

```markdown
# Solicitud de revisión final

Revisar el trabajo completado de Codex contra el brief original de tarea.

## Prioridades de revisión
1. Bugs, regresiones y comportamiento incorrecto.
2. Validación faltante o débil.
3. Filtración de datos o riesgos de integridad de investigación.
4. Scope creep.
5. Brechas de documentación.

## Salida requerida
- Hallazgos primero, ordenados por severidad.
- Referencias a archivo y línea cuando sea posible.
- Tabla de estado de criterios de aceptación.
- Pruebas/controles revisados.
- Riesgos residuales.
- Recomendación de decisión: aceptar, aceptar con notas, revisar o escalar.
```

## Template 5: adenda de `AGENTS.md` para repositorios de investigación

```markdown
## Integridad de investigación
- Preservar datos crudos. No modificar archivos bajo `data/raw/` salvo pedido explícito.
- Hacer el análisis reproducible con comandos documentados.
- Distinguir hallazgos, interpretación y especulación.
- Declarar supuestos y limitaciones.
- No exponer datos sensibles en ejemplos, logs, docs generadas o commits.

## Workflow de Codex
- Para tareas no triviales, inspeccionar contexto primero y presentar un plan breve.
- Antes de editar, identificar archivos objetivo y comandos de validación.
- Mantener cambios acotados a la solicitud del usuario.
- Ejecutar controles relevantes cuando sea factible.
- Terminar con archivos cambiados, resultados de validación, supuestos y riesgos residuales.

## Revisión
- Usar `code_review.md` para estándares de revisión de código.
- Encabezar revisiones con defectos y riesgos, no resúmenes.
- Para salidas de investigación, revisar procedencia de datos, métodos, reproducibilidad y fuerza de afirmaciones.
```

## Template 6: `code_review.md` para código de investigación

```markdown
# Rúbrica de code review

## Corrección
- ¿El código implementa el comportamiento solicitado?
- ¿Se manejan edge cases?
- ¿Los errores son explícitos y accionables?

## Reproducibilidad
- ¿Los comandos están documentados?
- ¿Los inputs y outputs son estables?
- ¿Las semillas aleatorias están controladas cuando corresponde?

## Integridad de investigación
- ¿Se preservan los datos crudos?
- ¿Las transformaciones son trazables?
- ¿Las afirmaciones estadísticas están respaldadas?
- ¿Las limitaciones están documentadas?

## Seguridad y privacidad
- ¿Los secretos están excluidos?
- ¿Los datos sensibles están protegidos?
- ¿Las llamadas externas están aprobadas?

## Mantenibilidad
- ¿El código sigue patrones locales?
- ¿La complejidad está justificada?
- ¿Los comentarios son útiles y escasos?

## Pruebas
- ¿Las pruebas o controles son proporcionales al riesgo?
- ¿Las fallas se reportan honestamente?
```

