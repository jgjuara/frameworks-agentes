# Experimento de contexto y prompting para Codex

Este directorio contiene una implementacion reproducible del protocolo definido en
`strategy/CODEX_CONTEXT_PROMPTING_EXPERIMENT.md`.

## Estructura

- `code/`: scripts Python ejecutables con `uv run python`.
- `data/`: tareas sinteticas/de-identificadas para el piloto.
- `docs/`: runbook operativo, plantilla de revision y notas de alcance.
- `prompts/`: prompts generados por corrida.
- `results/`: asignaciones, metricas de diseno, plantillas de observacion y reportes.

## Ejecucion

Desde la raiz del repositorio:

```powershell
uv run python experiments/codex_context_prompting/code/run_experiment.py
```

La corrida crea un subdirectorio en `results/` y un set de prompts en `prompts/`.

## Alcance

El script ejecuta el armado experimental y el analisis de calidad del paquete:
asignacion aleatorizada y balanceada, prompts por condicion, metricas de volumen
de contexto, readiness rubric y plantillas para registrar resultados reales.

No ejecuta multiples threads reales de Codex por si solo. Las metricas primarias
del protocolo, como exito de tarea o falsa finalizacion, requieren correr los
prompts generados en threads frescos y completar la plantilla de observaciones.
