# Informe: contexto y prompting para tareas verificables con Codex

**Resumen:** Este informe responde cuánto contexto y prompting debería dar un equipo de investigación a Codex cuando la tarea es verificable, computable y se espera una solución concreta. La evidencia respalda un flujo con contexto mínimo y alta verificación: dar a Codex suficiente contexto curado para identificar objetivo, restricciones y criterios de éxito; mover reglas duraderas a `AGENTS.md` o skills; dejar que el agente recupere más contexto del repositorio según sea necesario; y exigir validación ejecutable. Más contexto no es automáticamente mejor. La investigación sobre long-context, los resultados de SWE-bench y la guía empresarial para agentes apuntan al mismo principio operativo: Codex funciona mejor cuando el prompt define el contrato del problema y el entorno aporta pruebas, herramientas y artefactos revisables.

## 1. Pregunta de investigación

Para un equipo de investigación que usa Codex en tareas como análisis computacional, notebooks reproducibles, arreglos de research-code, simulaciones, pipelines de datos e informes técnicos:

> ¿Cuánto contexto y prompting debería proporcionarse al inicio para una tarea verificable cuya salida esperada es una solución computable?

La respuesta práctica es:

- Usar un **contrato breve de tarea** como prompt, normalmente 200-800 palabras para tareas ordinarias y 800-1.500 palabras para tareas de alto riesgo o multiarchivo.
- Incluir **contexto de alta señal**, no volcados de fondo: objetivo, archivos, restricciones, comandos, fallas conocidas, criterios de aceptación y disparadores de escalamiento.
- Poner reglas persistentes del equipo en `AGENTS.md`, no en cada prompt. OpenAI documenta que Codex carga `AGENTS.md` automáticamente y que el límite combinado predeterminado de instrucciones de proyecto es 32 KiB salvo configuración distinta.
- Usar **un hilo por tarea coherente**. OpenAI advierte explícitamente que usar un hilo por proyecto infla el contexto y empeora resultados con el tiempo.
- Hacer que la tarea sea **verificable antes de ejecutar**: pruebas, comandos de reproducibilidad, artefactos esperados, pasos para reproducir issues o una rúbrica de revisión.
- Pedir a Codex que inspeccione, planifique, implemente, ejecute controles y reporte evidencia. No pedir generación libre e ininterrumpida en trabajo de investigación no trivial.

## 2. Base de evidencia

Este informe usa tres clases de fuentes:

1. Documentación oficial de OpenAI Codex y notas de producto.
2. Papers y benchmarks académicos sobre agentes de código, long context, recuperación y bucles de razonamiento/acción.
3. Guía empresarial de GitHub y Anthropic sobre agentes de código, instrucciones personalizadas, contexto y validación.

Las fuentes más importantes están listadas en `CODEX_CONTEXT_PROMPTING_EVIDENCE.es.md`.

## 3. Hallazgo central

El patrón central no es "darle todo al modelo". El patrón central es:

```text
instrucciones duraderas pequeñas
+ prompt de tarea curado
+ recuperación de contexto guiada por el agente
+ verificación ejecutable
+ revisión humana final
```

Esto encaja con la evidencia más fuerte:

- OpenAI Codex recomienda prompts con objetivo, contexto, restricciones y criterios de "done when", y recomienda pruebas, controles y revisión antes de la aceptación.
- La guía de `AGENTS.md` de OpenAI Codex trata la orientación duradera de repositorio como contexto cargado automáticamente, con archivos más cercanos que prevalecen sobre los más amplios.
- SWE-bench enmarca el trabajo real de software como codebase + issue + patch + evaluación de pruebas ejecutables. El benchmark muestra que las tareas reales requieren razonamiento multiarchivo, entornos de ejecución y uso complejo del contexto, no solo completado aislado de código.
- "Lost in the Middle" muestra que las ventanas largas no garantizan uso robusto de todo el contexto; la información relevante puede subutilizarse si queda enterrada en el medio.
- SWE-agent muestra que la interfaz y el diseño de herramientas mejoran el desempeño de agentes de código.
- Agentless muestra que localización, reparación y validación simples pueden competir con andamiajes autónomos complejos, lo que va contra la orquestación innecesaria.
- La guía de GitHub Copilot dice que las tareas de agentes deberían ser claras, bien acotadas, incluir criterios de aceptación e identificar archivos cuando se conocen.
- La guía de Anthropic Claude Code llega al mismo punto operativo: las ventanas de contexto se llenan de contenido irrelevante, los archivos persistentes de instrucciones deben podarse y probarse, y permisos/sandboxing reducen fatiga de aprobación.

## 4. Recomendación de presupuesto de contexto

Usar estos presupuestos iniciales para tareas de Codex en repositorios de investigación.

| Clase de tarea | Prompt inicial | Contexto inicial | ¿Dejar que Codex descubra? | Verificación requerida |
|---|---:|---|---|---|
| R0 explicación read-only | 100-300 palabras | 0-3 archivos o rutas | Sí | citas de fuentes o referencias de archivo |
| R1 arreglo local de código/docs | 200-600 palabras | comando fallido, rutas relevantes, comportamiento esperado | Sí | pruebas/lint/type checks focalizados |
| R2 cómputo de investigación | 500-1.200 palabras | fuente de datos, restricciones de método, scripts/notebooks relevantes, formato de salida | Sí, dentro del alcance permitido de datos | comando reproducible y revisión de artefacto |
| R3 trabajo sensible o con consecuencias externas | 800-1.500 palabras | límites explícitos de riesgo, reglas de datos, puertas de aprobación, rúbrica de validación | Limitado | revisión humana más controles automatizados |
| R4 legal/médico/financiero/seguridad/publicación de política pública | Codex puede asistir solo dentro de un flujo gobernado | paquete de gobernanza requerido | Restringido | aprobación experta fuera de Codex |

La variable importante no es la cantidad de palabras. Es la **densidad del contexto**: cada párrafo debería cambiar lo que Codex hará.

## 5. Contrato de prompt

Toda tarea computable no trivial debería incluir estos campos:

1. **Misión:** artefacto o comportamiento concreto que debe existir.
2. **Contexto autoritativo:** archivos, datasets, links de issues, estándares o ejemplos.
3. **Restricciones:** arquitectura, manejo de datos, dependencias, seguridad y límites de alcance.
4. **Acciones permitidas:** qué puede leer, editar, ejecutar e instalar Codex.
5. **Acciones prohibidas:** acciones destructivas, externas, sensibles o costosas que requieren aprobación.
6. **Criterios de aceptación:** pruebas, métricas, archivos de salida, criterios de reproducibilidad y checklist de revisión.
7. **Disparadores de escalamiento:** contradicciones, datos faltantes, ambigüedad de pruebas, riesgo de privacidad o acción irreversible.
8. **Paquete final de evidencia:** archivos cambiados, comandos ejecutados, resultado de validación, supuestos y riesgos residuales.

Para una tarea verificable, los criterios de aceptación importan más que el detalle en prosa. Un prompt corto con una prueba fallida ejecutable es mejor que uno largo sin pruebas.

## 6. Qué no poner en el prompt

Evitar poner esto en prompts puntuales:

- Convenciones estables del repositorio que pertenecen a `AGENTS.md`.
- Instrucciones de flujos repetidos que deberían convertirse en una skill.
- Documentos completos cuando solo una sección o afirmación es relevante.
- Extractos grandes de datos cuando Codex puede inspeccionar archivos localmente.
- Historias largas de discusión previa salvo que una decisión deba preservarse.
- Preferencias vagas como "alta calidad" sin un criterio observable.

El prompt no debería convertirse en un segundo repositorio. Debería apuntar a Codex hacia la evidencia correcta del repositorio.

## 7. Patrón de tarea verificable

Para tareas que deberían crear una solución computable, usar este ciclo:

```text
Brief -> inspeccionar -> planificar -> implementar -> correr controles -> reparar -> resumir evidencia -> revisión humana
```

La persona usuaria aporta la primera y última puerta. Codex maneja el bucle intermedio, pero solo dentro de límites definidos.

Para trabajo de investigación, esto significa:

- Especificar ubicaciones de datos crudos y si son inmutables.
- Exigir comandos de reproducibilidad.
- Exigir notas metodológicas que separen datos, modelo, hallazgos, interpretación y limitaciones.
- Exigir que no haya datos sensibles en documentación generada.
- Exigir comandos exactos de prueba o validación cuando sea factible.

## 8. Respuesta a "cuánto contexto"

Dar **el mínimo contexto necesario para que el primer plan sea correcto**, más suficiente información de verificación para que Codex detecte fallas.

Eso suele significar:

- **Siempre incluir:** objetivo, criterios de finalización, comandos de validación y restricciones.
- **Usualmente incluir:** rutas relevantes, logs de falla, ejemplos de salida esperada y prioridad de fuentes.
- **A veces incluir:** racional de diseño, definiciones de dominio, decisiones previas y puertas de riesgo.
- **Rara vez incluir:** documentos completos, volcados enteros de datos, historiales completos de chat o lectura de fondo amplia.

Si Codex necesita más, indicarle que inspeccione el repositorio y pregunte solo cuando la información faltante no pueda descubrirse de forma segura.

## 9. Estándar recomendado para el equipo

Adoptar este estándar operativo:

1. Mantener un `AGENTS.md` conciso a nivel repo con reglas de setup, validación, manejo de datos y revisión.
2. Usar un brief de tarea para todas las tareas R1+.
3. Mantener un hilo de Codex por tarea coherente.
4. Promover flujos repetidos a skills.
5. Exigir verificación ejecutable para cualquier artefacto computable.
6. Registrar fallas y actualizar `AGENTS.md`, skills o templates solo después de fricción repetida.
7. Ejecutar un experimento mensual de ablación prompt/contexto usando `CODEX_CONTEXT_PROMPTING_EXPERIMENT.es.md`.

## 10. Referencias

- OpenAI, Codex best practices: https://developers.openai.com/codex/learn/best-practices
- OpenAI, Codex prompting: https://developers.openai.com/codex/prompting
- OpenAI, custom instructions with `AGENTS.md`: https://developers.openai.com/codex/guides/agents-md
- OpenAI, Introducing SWE-bench Verified: https://openai.com/index/introducing-swe-bench-verified/
- OpenAI, Introducing GPT-5.3-Codex: https://openai.com/index/introducing-gpt-5-3-codex/
- Jimenez et al., SWE-bench: https://arxiv.org/abs/2310.06770
- Yang et al., SWE-agent: https://arxiv.org/abs/2405.15793
- Xia et al., Agentless: https://arxiv.org/abs/2407.01489
- Liu et al., Lost in the Middle: https://arxiv.org/abs/2307.03172
- Chen et al., Evaluating Large Language Models Trained on Code: https://arxiv.org/abs/2107.03374
- Wei et al., Chain-of-Thought Prompting: https://arxiv.org/abs/2201.11903
- Lewis et al., Retrieval-Augmented Generation: https://arxiv.org/abs/2005.11401
- Yao et al., ReAct: https://arxiv.org/abs/2210.03629
- Shinn et al., Reflexion: https://arxiv.org/abs/2303.11366
- Galster et al., Configuring Agentic AI Coding Tools: https://arxiv.org/abs/2602.14690
- GitHub Docs, Best practices for using Copilot to work on tasks: https://docs.github.com/en/copilot/tutorials/cloud-agent/get-the-best-results
- GitHub Docs, Prompt engineering for Copilot: https://docs.github.com/en/copilot/concepts/prompting/prompt-engineering
- Anthropic, Claude Code best practices: https://code.claude.com/docs/en/best-practices
- Anthropic, Claude prompting best practices: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices

