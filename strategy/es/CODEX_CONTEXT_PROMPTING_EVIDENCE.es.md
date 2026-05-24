# Matriz de evidencia: contexto, prompting y agentes de código verificables

**Resumen:** Esta matriz de evidencia sintetiza fuentes confiables usadas para diseñar el marco de contexto y prompting para Codex. La literatura revisada y la guía empresarial convergen en cuatro afirmaciones: los agentes de código necesitan criterios explícitos de éxito, el long context es frágil cuando no está curado, las interfaces de herramientas y la retroalimentación de ejecución importan, y las instrucciones duraderas del repositorio deben separarse de los prompts puntuales de cada tarea.

## 1. Reglas de calidad de fuentes

Orden de prioridad:

1. Papers revisados por pares o de conferencias.
2. Papers de arXiv de grupos de investigación importantes cuando la revisión por pares no está disponible o el tema es reciente.
3. Documentación oficial de OpenAI, GitHub, Anthropic, Microsoft, Google, IBM u organismos de estándares.
4. Blogs técnicos solo cuando son publicaciones de ingeniería empresarial de primera parte.

Esta matriz excluye afirmaciones de redes sociales, publicaciones de benchmarks con baja atribución y marketing de proveedores sin detalle técnico accionable.

## 2. Tabla de evidencia

| Fuente | Tipo | Hallazgo relevante | Implicancia para Codex |
|---|---|---|---|
| OpenAI Codex best practices | Docs oficiales | Un buen prompt incluye objetivo, contexto, restricciones y "done when"; la confiabilidad mejora cuando Codex puede probar, verificar y revisar el trabajo. | Usar contratos de tarea estructurados y exigir validación. |
| OpenAI Codex prompting | Docs oficiales | Codex reúne contexto desde contenidos de archivos, salida de herramientas y su registro de acciones en curso; toda la información del hilo debe caber en la ventana de contexto y puede compactarse. | No sobrecargar el prompt inicial. Dejar que Codex inspeccione y resuma. |
| Guía OpenAI `AGENTS.md` | Docs oficiales | Codex lee automáticamente archivos `AGENTS.md` en capas; el descubrimiento de instrucciones de proyecto tiene un límite combinado predeterminado de 32 KiB. | Poner reglas duraderas del equipo en `AGENTS.md`, mantenerlas concisas y usar archivos anidados para reglas locales. |
| OpenAI SWE-bench Verified | Post oficial de producto/investigación | Un subconjunto de 500 muestras validado por humanos eliminó tareas ambiguas o problemáticas de SWE-bench; la evaluación confiable necesita pruebas acotadas y descripciones de issue. | Las tareas ambiguas deberían aclararse antes de que Codex empiece. |
| OpenAI GPT-5.3-Codex release | Post oficial de producto/investigación | OpenAI informa que GPT-5.3-Codex puede manejar investigación de larga duración, uso de herramientas y ejecución compleja, pero enfatiza dirección, actualizaciones y tareas benchmarkeadas. | Modelos más capaces todavía necesitan interfaces de supervisión y objetivos verificables. |
| SWE-bench, Jimenez et al. | ICLR 2024 / arXiv | Issues reales de GitHub requieren coordinar cambios entre múltiples funciones, clases y archivos, además de entornos de ejecución y razonamiento de long-context. | Usar tareas realistas y validación ejecutable, no demos aisladas de prompts. |
| SWE-agent, Yang et al. | NeurIPS 2024 / arXiv | Las interfaces agente-computadora mejoran la capacidad de un agente LM para editar código, navegar repositorios y correr pruebas. | Herramientas, acceso a shell y navegación de archivos son parte de la estrategia de prompt. |
| Agentless, Xia et al. | arXiv | Un pipeline simple de localización, reparación y validación tuvo buen desempeño en SWE-bench Lite a bajo costo. | Preferir flujos estructurados simples antes que orquestación multiagente compleja. |
| Lost in the Middle, Liu et al. | TACL / arXiv | El rendimiento del modelo puede degradarse cuando la información relevante queda enterrada en contextos largos. | Curar y ordenar el contexto; no pegar grandes fondos indiferenciados. |
| Evaluating LLMs Trained on Code, Chen et al. | Paper de OpenAI / arXiv | HumanEval introdujo corrección funcional mediante pruebas; el muestreo repetido mejoró tasas de resolución pero expuso límites en cadenas largas de operaciones y vinculación de variables. | La verificabilidad debería ser ejecutable; múltiples intentos ayudan solo si hay controles disponibles. |
| Chain-of-Thought Prompting, Wei et al. | NeurIPS / arXiv | El razonamiento intermedio mejora el desempeño en tareas complejas aritméticas, de sentido común y simbólicas para modelos suficientemente grandes. | Pedir planificación y descomposición, pero evaluar salidas en lugar de confiar en explicaciones. |
| Retrieval-Augmented Generation, Lewis et al. | NeurIPS 2020 / arXiv | Combinar modelos paramétricos con memoria externa recuperada mejora tareas intensivas en conocimiento y procedencia. | Preferir recuperación y referencias a fuentes antes que prompts inflados. |
| ReAct, Yao et al. | ICLR 2023 / arXiv | Intercalar razonamiento y acciones permite que los agentes actualicen planes a partir de observaciones y usen herramientas externas. | Codex debería inspeccionar, actuar, observar resultados de pruebas y revisar. |
| Reflexion, Shinn et al. | Workshop NeurIPS / arXiv | Los agentes de lenguaje pueden usar feedback como memoria textual para mejorar intentos futuros sin actualizar pesos. | Las retrospectivas post-tarea deberían convertirse en instrucciones o skills mejoradas. |
| Configuring Agentic AI Coding Tools, Galster et al. | AIware 2026 / arXiv | Los archivos de contexto a nivel repositorio dominan la configuración de herramientas de codificación agentic; `AGENTS.md` está emergiendo como estándar interoperable. | Versionar instrucciones de equipo y tratarlas como activos de ingeniería. |
| GitHub Copilot task guidance | Docs oficiales | Las tareas de agentes deberían ser claras, acotadas, incluir criterios de aceptación e identificar archivos cuando sea posible; las instrucciones personalizadas pueden guiar build/test/validation. | Los prompts de Codex deberían parecerse a issues bien acotados. |
| GitHub Copilot prompt guidance | Docs oficiales | Empezar amplio y luego específico, dar ejemplos, dividir tareas complejas, evitar ambigüedad, indicar código relevante y mantener el historial pertinente. | Usar prompts estructurados concisos y mantener la historia del chat relevante a la tarea. |
| Anthropic Claude Code best practices | Docs oficiales | Las ventanas de contexto se llenan con contenido irrelevante; los archivos largos de instrucciones deben podarse, probarse y tratarse como código. | Mantener `AGENTS.md` breve y mantenerlo empíricamente. |
| Anthropic Claude prompting best practices | Docs oficiales | Fomentar criterios claros de éxito, verificación de fuentes, investigación estructurada, notas de progreso y cautela ante acciones irreversibles o de sistemas compartidos. | Usar reglas explícitas de escalamiento y estado de progreso para tareas de investigación. |

## 3. Síntesis

### 3.1 El prompt debería definir el contrato

OpenAI y GitHub describen los prompts eficaces para agentes de código como definiciones estructuradas de tarea. Deben indicar objetivo, contexto relevante, restricciones, criterios de aceptación y ruta de validación. Esto es más fuerte que un consejo genérico de prompt engineering: para software y cómputo de investigación, el prompt funciona como una especificación compacta de issue.

### 3.2 El long context es una herramienta, no un objetivo

La evidencia sobre long-context es mixta. Ventanas más largas hacen posibles tareas grandes, pero "Lost in the Middle" muestra que el material relevante puede ignorarse o recibir menos peso según su posición. La documentación de Codex también describe compactación para trabajos largos. Por lo tanto, el equipo debería optimizar relevancia, orden y recuperabilidad, no volumen bruto.

### 3.3 La verificabilidad supera la calidad de explicación

HumanEval, SWE-bench y SWE-bench Verified evalúan código ejecutando pruebas o comprobando parches contra issues reales. Eso importa para equipos de investigación: una explicación fluida no alcanza. El artefacto final debe correr, reproducirse o verificarse contra criterios explícitos.

### 3.4 Las interfaces de agente importan

SWE-agent muestra que la forma en que un agente ve archivos, edita código y ejecuta comandos afecta los resultados. Las guías de GitHub y Anthropic también enfatizan instrucciones personalizadas, comandos de build/test, herramientas CLI, configuración de permisos y preparación del entorno. El prompting no puede compensar un entorno de validación ausente.

### 3.5 Los flujos simples son una base fuerte

Agentless es importante porque cuestiona la suposición de que los andamiajes autónomos complejos siempre son superiores. Para un equipo de investigación, el default debería ser:

```text
localizar -> planificar -> editar -> validar -> revisar
```

Usar flujos multiagente solo después de medir una base simple y encontrarla insuficiente.

## 4. Conflictos y limitaciones

- La guía empresarial es parcialmente específica de producto. GitHub Copilot y Claude Code no son Codex, pero su guía es relevante porque aparecen las mismas presiones de diseño: tareas acotadas, instrucciones personalizadas, control de contexto, testeabilidad y permisos.
- Muchos puntajes de benchmarks de agentes envejecen rápido. Este informe usa la estructura de los benchmarks, no los rankings, como lección duradera.
- Los resultados de long-context varían por generación de modelo. La lección conservadora se mantiene: ventanas grandes reducen límites duros, pero no eliminan la necesidad de context engineering.
- Chain-of-thought mejora muchas tareas de razonamiento, pero las explicaciones pueden no ser fieles. Para Codex, pedir planes y estado, pero aceptar solo evidencia ejecutable.

## 5. Fuentes

- OpenAI Codex best practices: https://developers.openai.com/codex/learn/best-practices
- OpenAI Codex prompting: https://developers.openai.com/codex/prompting
- OpenAI `AGENTS.md` guide: https://developers.openai.com/codex/guides/agents-md
- OpenAI SWE-bench Verified: https://openai.com/index/introducing-swe-bench-verified/
- OpenAI GPT-5.3-Codex: https://openai.com/index/introducing-gpt-5-3-codex/
- SWE-bench: https://arxiv.org/abs/2310.06770
- SWE-agent: https://arxiv.org/abs/2405.15793
- Agentless: https://arxiv.org/abs/2407.01489
- Lost in the Middle: https://arxiv.org/abs/2307.03172
- Evaluating Large Language Models Trained on Code: https://arxiv.org/abs/2107.03374
- Chain-of-Thought Prompting: https://arxiv.org/abs/2201.11903
- Retrieval-Augmented Generation: https://arxiv.org/abs/2005.11401
- ReAct: https://arxiv.org/abs/2210.03629
- Reflexion: https://arxiv.org/abs/2303.11366
- Configuring Agentic AI Coding Tools: https://arxiv.org/abs/2602.14690
- GitHub Copilot cloud agent task guidance: https://docs.github.com/en/copilot/tutorials/cloud-agent/get-the-best-results
- GitHub Copilot prompt engineering: https://docs.github.com/en/copilot/concepts/prompting/prompt-engineering
- Claude Code best practices: https://code.claude.com/docs/en/best-practices
- Claude prompting best practices: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices

