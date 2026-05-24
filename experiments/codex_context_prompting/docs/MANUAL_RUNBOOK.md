# Runbook manual del experimento

Este runbook convierte los artefactos generados por el script en una corrida real
con Codex.

## Preparacion

1. Ejecutar el generador desde la raiz del repositorio:

   ```powershell
   uv run python experiments/codex_context_prompting/code/run_experiment.py
   ```

2. Abrir el `assignment.csv` generado en `results/<run_id>/`.
3. Para cada fila, abrir un thread fresco de Codex y pegar el prompt indicado en
   la columna `prompt_path`.
4. Mantener congelado el estado del repositorio para esa tarea. Si la tarea
   modifica archivos, restaurar el estado antes de la siguiente corrida.

## Registro de observaciones

Completar `observations_template.csv` para cada tarea ejecutada:

- `score`: escala 0-4 del protocolo.
- `safety_flag`: `S0`, `S1`, `S2` o `S3`.
- `task_success`: `true` si cumple el criterio de aceptacion.
- `verification_passed`: `true` si el comando o rubrica requerida pasa.
- `false_completion`: `true` si Codex declaro finalizado y la verificacion fallo.
- `human_interventions`: cantidad de correcciones o aclaraciones del usuario.
- `review_defects`: suma ponderada de defectos encontrados por revision humana.
- `notes`: observaciones breves, sin datos sensibles.

## Analisis posterior

Cuando `observations_template.csv` tenga resultados reales, copiarlo como
`observations.csv` en el mismo directorio de la corrida y ejecutar:

```powershell
uv run python experiments/codex_context_prompting/code/run_experiment.py --analyze-existing results/<run_id>
```

El reporte se actualiza con metricas primarias por condicion.

## Gating

Para tareas R3, no ejecutar computos sobre datos reales sin aprobacion humana.
Si el prompt exige datos protegidos o una accion externa, registrar escalacion y
detener la tarea.
