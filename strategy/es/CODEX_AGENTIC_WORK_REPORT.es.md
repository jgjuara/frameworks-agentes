# Marco de trabajo agentic de Codex para equipos de investigación

**Resumen:** Este informe evalúa si un equipo de investigación que usa Codex debería concentrar la revisión humana al comienzo y al final del trabajo agentic, en lugar de depender de controles continuos de human-in-the-loop. La evidencia respalda la intuición central para flujos de investigación y software de riesgo bajo y medio, pero con una corrección importante: la supervisión escalable no debería significar "sin controles durante la ejecución". Debería significar intención, contexto, restricciones y criterios de evaluación definidos al inicio; controles automatizados durante la ejecución; puertas humanas obligatorias solo para acciones de alto riesgo, irreversibles o materialmente ambiguas; y una revisión final estructurada antes de aceptar el resultado.

## Conclusión central

Tu tesis es mayormente correcta para ingeniería de investigación basada en Codex: los controles manuales frecuentes no escalan y a menudo se convierten en aprobaciones de baja calidad. El mejor modelo operativo es **especificación inicial más adjudicación final**, respaldado por validación automatizada, trazas de auditoría y escalamiento disparado por riesgo.

La parte que necesita corrección es evitar de forma absoluta la intervención humana durante la ejecución. Para trabajo agentic, especialmente cuando las herramientas pueden modificar archivos, llamar sistemas externos, acceder a datos sensibles o publicar salidas, el equipo todavía necesita **puertas selectivas**. Esas puertas deben declararse al inicio y vincularse a clases de riesgo, no improvisarse cada pocos minutos.

## Dónde el análisis te da la razón

- La atención humana es el recurso escaso. Gastarla en aprobaciones frecuentes con poco contexto suele ser ineficiente.
- El comienzo de la tarea es el punto de mayor apalancamiento porque define objetivo, evidencia, restricciones, herramientas y criterios de revisión.
- El final de la tarea es el punto de rendición de cuentas porque la persona puede inspeccionar el artefacto completo, la evidencia de validación y los riesgos residuales.
- Para trabajo acotado con Codex, los controles manuales deberían ser la excepción, no la regla.

## Dónde el análisis muestra que tienes razón solo en parte

- "Sin humano en el loop" es demasiado amplio. Algunas decisiones no deben delegarse al agente una vez iniciada la ejecución.
- La revisión final por sí sola llega demasiado tarde para acciones irreversibles, visibles externamente, sensibles o de alto impacto.
- Un prompt no es gobernanza. El brief inicial debe estar respaldado por sandboxing, permisos, pruebas automatizadas, logs y reglas claras de escalamiento.
- Más contexto no es automáticamente mejor. El contexto debe curarse, priorizarse y vincularse a criterios de aceptación.

## Evaluación de afirmaciones

| Afirmación | Evaluación | Motivo |
|---|---:|---|
| Human-in-the-loop en cada decisión no escala. | Respaldada | La investigación sobre automation bias y la guía de gobernanza empresarial muestran que las aprobaciones no estructuradas pueden convertirse en sellos automáticos, especialmente bajo presión de tiempo. |
| La revisión del usuario debería concentrarse al inicio y al final. | Respaldada con límites de alcance | Funciona bien para tareas acotadas de investigación/código cuando las herramientas están en sandbox y los criterios de éxito son medibles. |
| No se necesita ninguna decisión humana durante la ejecución. | No respaldada | Acciones de alto impacto, irreversibles, visibles externamente, con datos sensibles o ambiguas requieren escalamiento predeclarado. |
| Mejor contexto inicial es la palanca principal para mejores resultados con Codex. | Fuertemente respaldada | La guía de OpenAI Codex dice que el comportamiento de revisión/prueba depende de que Codex sepa cómo se ve "bueno" mediante el prompt o `AGENTS.md`; la investigación sobre long-context también advierte que volcar contexto no alcanza. |

## Modelo operativo recomendado

Adoptar un proceso **Start-Gate / Autonomous Work / Final-Gate**:

1. **Start-Gate:** La persona usuaria proporciona un brief compacto de misión, contexto autoritativo, criterios de aceptación, herramientas permitidas, acciones prohibidas, clase de riesgo y rúbrica de revisión.
2. **Autonomous Work:** Codex planifica, edita, prueba, se autorevisa y registra supuestos. Se evita la interrupción humana salvo que se active un disparador de escalamiento predefinido.
3. **Final-Gate:** La persona usuaria revisa el diff, la evidencia, las pruebas, los riesgos no resueltos y la rúbrica de aceptación antes de mergear, publicar o usar operativamente.

Para detalles de implementación, usar:

- [CODEX_EVIDENCE_REVIEW.es.md](CODEX_EVIDENCE_REVIEW.es.md)
- [CODEX_INITIAL_CONDITIONS_FRAMEWORK.es.md](CODEX_INITIAL_CONDITIONS_FRAMEWORK.es.md)
- [CODEX_FINAL_REVIEW_PLAYBOOK.es.md](CODEX_FINAL_REVIEW_PLAYBOOK.es.md)
- [CODEX_TEMPLATES.es.md](CODEX_TEMPLATES.es.md)

## Implicancias estratégicas

Los equipos de investigación deberían dejar de tratar el prompting como una artesanía individual y convertirlo en una interfaz operativa. La unidad escalable no es "un buen prompt de usuario"; es un **artefacto de intake de tarea** que puede reutilizarse, revisarse, probarse y mejorarse.

Eso implica invertir en:

- Un `AGENTS.md` de nivel repositorio que codifique reglas estables de ingeniería.
- Templates de prompt específicos por tarea para flujos comunes de investigación.
- `code_review.md` y rúbricas de revisión final referenciadas por `AGENTS.md`.
- Skills para flujos repetibles, en lugar de prompts largos a medida.
- Controles automatizados que Codex pueda ejecutar sin pedir juicio humano.
- Reglas de clase de riesgo que definan cuándo Codex debe detenerse y preguntar.

## Fuentes usadas

La base de evidencia prioriza documentación oficial de proveedores, trabajo académico revisado por pares o establecido y material importante de gobernanza empresarial:

- Documentación de buenas prácticas y configuración de OpenAI Codex.
- Guías de interacción humano-IA de Microsoft Research HAX / CHI 2019.
- Google PAIR People + AI Guidebook.
- NIST AI Risk Management Framework.
- Guía de ingeniería de Anthropic sobre agentes efectivos y agent evals.
- Guía de IBM sobre gobernanza de agentic AI empresarial y context engineering.
- Trabajos académicos sobre automation bias, supervisión humana, límites de long-context, ReAct, Reflexion, AI Chains y SWE-bench.

