# Revisión de evidencia: contexto, supervisión y confiabilidad agentic

**Resumen:** Este archivo revisa evidencia confiable relevante para la adopción de Codex por un equipo de investigación. La evidencia rechaza dos extremos: la supervisión human-in-the-loop totalmente manual es demasiado lenta y a menudo débil, mientras que la autonomía sin controles es insegura cuando las tareas son ambiguas, irreversibles o con consecuencias externas. El patrón más defendible es autonomía acotada: fuerte encuadre inicial de tarea, controles automatizados durante la ejecución y revisión final rigurosa con escalamiento selectivo.

## 1. Evidencia específica de Codex

La documentación de buenas prácticas de OpenAI Codex afirma que la confiabilidad mejora cuando el usuario le pide crear o actualizar pruebas, ejecutar controles, confirmar comportamiento y revisar el trabajo antes de aceptar. Crucialmente, la documentación dice que Codex solo puede hacer ese bucle si sabe cómo se ve "bueno", y esa guía puede venir del prompt o de `AGENTS.md`.

Implicancia: el prompt inicial y las instrucciones persistentes del repo no son cosméticas. Definen el objetivo de evaluación del agente.

Fuente: OpenAI Codex best practices, "Improve reliability with testing and review"  
https://developers.openai.com/codex/learn/best-practices#improve-reliability-with-testing-and-review

OpenAI también recomienda convertir trabajo repetible en Skills en lugar de depender de prompts largos o idas y vueltas repetidas. Las Skills empaquetan instrucciones, contexto y lógica de soporte para que Codex las aplique de forma consistente entre superficies.

Implicancia: para un equipo de investigación, escalar Codex significa convertir patrones repetidos de interacción en activos del equipo.

Fuente: OpenAI Codex best practices, "Turn repeatable work into skills"  
https://developers.openai.com/codex/learn/best-practices#turn-repeatable-work-into-skills

Los slash commands de Codex también respaldan este modelo operativo: `/init` crea instrucciones persistentes `AGENTS.md`, `/mention` adjunta archivos específicos, `/plan` pide un plan antes de implementar, `/goal` fija un objetivo persistente de tarea, `/diff` apoya la revisión antes de pruebas o commit, y `/review` pide a Codex revisar cambios no committeados, commits o diffs tipo PR.

Fuente: OpenAI Codex CLI slash commands  
https://developers.openai.com/codex/cli/slash-commands#built-in-slash-commands

La configuración de Codex admite `.codex/config.toml` local al proyecto, políticas de aprobación, modos de sandbox, ajustes de modelo de revisión, límites relacionados con AGENTS y confianza de proyecto. Esto indica que el uso escalable de Codex es un problema de configuración y gobernanza, no solo de prompting.

Fuente: OpenAI Codex configuration reference  
https://developers.openai.com/codex/config-reference#configtoml

## 2. Evidencia de que human-in-the-loop continuo es débil a escala

La investigación sobre automation bias muestra que las personas pueden sobreconfiar en recomendaciones automatizadas, especialmente en entornos presionados por tiempo o complejos. Esto debilita la idea de que las aprobaciones humanas frecuentes crean automáticamente control significativo.

Fuente: Goddard, Roudsari, Wyatt, "Automation bias: a systematic review..."  
https://pmc.ncbi.nlm.nih.gov/articles/PMC3240751/

El modelo clásico de Parasuraman, Sheridan y Wickens sobre automatización describe niveles y tipos de interacción humana con automatización. La lección práctica es que la "participación humana" no es un control binario. La calidad de supervisión depende de la función automatizada, la autoridad asignada a la máquina y la capacidad real de intervención de la persona.

Fuente: Parasuraman, Sheridan, Wickens, "A model for types and levels of human interaction with automation"  
https://dblp.org/rec/journals/tsmc/ParasuramanSW00.html

Trabajo reciente del sector público y gobernanza repite este punto: la supervisión humana puede fallar cuando reviewers carecen de contexto, autoridad, tiempo u observabilidad. Esto respalda reemplazar aprobaciones ad hoc por puntos de control diseñados, logs y reglas de escalamiento.

Fuente: Human-AI interactions in public-sector decision making, automation bias and selective adherence  
https://academic.oup.com/jpart/article/33/1/153/6524536

## 3. La guía de diseño humano-IA favorece control calibrado, no interrupción constante

Las 18 Guidelines for Human-AI Interaction de Microsoft Research, validadas con practicantes, enfatizan aclarar qué puede hacer el sistema, mostrar información contextualmente relevante, apoyar correcciones eficientes y manejar fallas con gracia. El patrón no es "preguntar al humano constantemente"; es "hacer que el sistema sea observable y controlable".

Fuente: Microsoft Research, Amershi et al., CHI 2019  
https://www.microsoft.com/en-us/research/publication/guidelines-for-human-ai-interaction/

Google People + AI Guidebook recomienda definir éxito, establecer expectativas de usuario, diseñar mecanismos de feedback y control, explicar comportamiento de IA y planificar errores y fallas elegantes. Esto refuerza la necesidad de encuadre inicial y evaluación final.

Fuente: Google PAIR, People + AI Guidebook  
https://pair.withgoogle.com/old-gb/

## 4. La guía empresarial agentic favorece límites, evals y supervisión

"Building Effective Agents" de Anthropic distingue workflows de agents y sostiene que los sistemas agentic efectivos necesitan criterios claros de éxito, bucles de feedback, supervisión humana significativa y buenas interfaces agente-computadora. También recomienda patrones simples antes que autonomía compleja.

Fuente: Anthropic, Building Effective Agents  
https://www.anthropic.com/engineering/building-effective-agents

La guía de agent evals de Anthropic enmarca la evaluación como un problema multi-turno y consciente del entorno. Para equipos de investigación, el punto importante es que los resultados finales solos son insuficientes; los equipos necesitan logs, rúbricas y revisión calibrada contra juicio experto.

Fuente: Anthropic, Demystifying Evals for AI Agents  
https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents

La guía de gobernanza agentic de IBM sostiene que escalar no es "más agentes autónomos"; es insertar autonomía con control definido, visibilidad, accountability, gobernanza de ciclo de vida, monitoreo y optimización de prompts. La guía de context engineering de IBM también enfatiza interfaces gobernadas y machine-callable en lugar de volcados informales de contexto.

Fuentes:  
https://www.ibm.com/think/insights/agentic-ai-governance-playbook  
https://www.ibm.com/think/insights/context-engineering-foundation-trusted-ai

El NIST AI Risk Management Framework trata la gestión de riesgo de IA como un proceso de ciclo de vida: mapear contexto, medir riesgo, gestionar riesgo y gobernar el sistema completo. Para uso de Codex, esto implica que el contexto inicial debe incluir contexto de riesgo y la revisión final debe comprobar si los controles de riesgo operaron.

Fuente: NIST AI RMF  
https://www.nist.gov/itl/ai-risk-management-framework

## 5. La investigación sobre LLMs y agentes respalda descomposición y revisión estructuradas

La investigación sobre long-context muestra que ventanas de contexto mayores no garantizan uso confiable de toda la información suministrada. "Lost in the Middle" encontró que el rendimiento puede degradarse cuando la información relevante queda enterrada en contextos largos.

Implicancia: un buen intake de Codex debería priorizar, rankear y resumir contexto en lugar de volcar documentos indiscriminadamente.

Fuente: Liu et al., "Lost in the Middle"  
https://arxiv.org/abs/2307.03172

ReAct mostró que intercalar razonamiento y acción puede mejorar la resolución de tareas y la interpretabilidad al permitir que el modelo actualice planes desde observaciones.

Implicancia: el prompt inicial debería pedir a Codex planificar, actuar, observar, revisar y verificar, pero la persona usuaria debería revisar el artefacto final en lugar de cada paso intermedio.

Fuente: Yao et al., ReAct  
https://openreview.net/forum?id=WE_vluYUL-X

AI Chains encontró que descomponer trabajo de LLM en subtareas encadenadas mejoró transparencia, controlabilidad, colaboración y permitió a usuarios "unit-test" subcomponentes.

Implicancia: la alternativa escalable al human-in-every-loop es la descomposición de workflows con artefactos intermedios verificables.

Fuente: Wu et al., AI Chains  
https://arxiv.org/abs/2110.01691

Reflexion mostró que los agentes de lenguaje pueden mejorar incorporando feedback en intentos futuros. Para equipos, esto respalda un registro estructurado post-tarea que pueda convertirse en contexto futuro, skills o actualizaciones de `AGENTS.md`.

Fuente: Shinn et al., Reflexion  
https://arxiv.org/abs/2303.11366

SWE-bench Verified enfatiza tareas de software reales, validadas por humanos, para evaluar mejor agentes de código. Refuerza que el desempeño agentic debe medirse contra tareas realistas y conjuntos de evaluación confiables, no solo demos.

Fuentes:  
https://www.swebench.com/verified.html  
https://openai.com/index/introducing-swe-bench-verified/

## 6. Conclusión desde la evidencia

La evidencia respalda una versión fuerte de tu posición para el contexto de equipo de investigación:

- Poner el trabajo cognitivo humano principal en el intake de tarea y la aceptación final.
- Reemplazar aprobación manual durante la ejecución por controles automatizados, logs y reglas predefinidas de escalamiento.
- No depender del tamaño de la ventana de contexto como sustituto de context engineering.
- No depender de un checkbox humano como sustituto de observabilidad, autoridad y calidad de revisión.

La evidencia no respalda eliminar toda intervención humana durante la ejecución. Respalda **intervención disparada por riesgo**, no intervención default.

