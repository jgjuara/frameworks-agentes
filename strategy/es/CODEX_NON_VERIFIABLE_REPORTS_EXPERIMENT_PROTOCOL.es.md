# Protocolo experimental: medición de prompting de Codex para informes abiertos

**Resumen:** Este protocolo define un experimento pequeño y novedoso que un equipo de investigación puede ejecutar para comparar estrategias de prompting de Codex en tareas de generación de informes no verificables. Está diseñado para medir si el contexto estructurado y los flujos de evidencia por etapas superan prompts breves o grandes volcados de contexto en calidad de fuentes, factualidad, precisión de citas y esfuerzo de revisión.

## Propósito

La revisión de literatura respalda flujos de contexto estructurado y verificación, pero el mejor tamaño y proceso exacto de prompt variará por equipo. Este experimento permite que el equipo mida desempeño en sus propias tareas de informe.

## Pregunta de investigación

Para tareas abiertas de informes de investigación sin índice exhaustivo de fuentes, ¿qué estrategia de prompting de Codex produce el mejor balance entre factualidad, calidad de fuentes, utilidad de síntesis y esfuerzo de reviewer?

## Hipótesis

H1: Un brief estructurado más inventario de fuentes por etapas y claim ledger superará a un prompt breve one-shot.

H2: Un gran volcado indiferenciado de contexto no superará de forma confiable a un brief compacto estructurado más flujo de búsqueda de fuentes.

H3: Exigir verificación a nivel de afirmación reducirá afirmaciones sin soporte y errores de cita, pero aumentará runtime.

## Condiciones experimentales

Usar el mismo tema de informe en cuatro condiciones.

| Condición | Descripción |
|---|---|
| A: prompt mínimo | "Write a report on X using reliable sources." |
| B: brief estructurado | Objetivo, audiencia, alcance, jerarquía de fuentes, esquema de salida, criterios de done-when. |
| C: gran volcado de contexto | Brief estructurado más muchos documentos no filtrados o notas largas. |
| D: flujo por etapas | Brief estructurado más inventario de fuentes, matriz de evidencia, outline, borrador, claim ledger e informe final requeridos. |

## Temas sugeridos

Elegir 3-5 temas reales relevantes para el equipo. Cada tema debería ser suficientemente amplio para requerir selección de fuentes, pero suficientemente estrecho para poder revisarse.

Ejemplos:

- Uso de IA en análisis de política pública.
- Métodos de evaluación para revisiones de literatura asistidas por LLM.
- Automation bias en soporte experto a la decisión.
- Retrieval-augmented generation para sistemas de conocimiento institucional.
- Gobernanza de agentes de IA en organizaciones de investigación.

## Template de prompt para condición D

```markdown
# Tarea
Crear un informe de investigación sobre [tema] para [audiencia] que informe [decisión].

## Alcance
Incluir [límites]. Excluir [límites].

## Jerarquía de fuentes
1. Literatura revisada por pares.
2. Fuentes oficiales gubernamentales o de estándares.
3. Publicaciones primarias empresariales de investigación/ingeniería.
4. Otras fuentes solo como contexto y claramente etiquetadas.

## Workflow
1. Buscar fuentes confiables y crear un inventario de fuentes.
2. Crear una matriz de evidencia.
3. Redactar un outline.
4. Escribir el informe con citas inline.
5. Crear un claim ledger.
6. Revisar afirmaciones sin soporte antes de finalizar.

## Reglas
- No citar fuentes salvo que hayan sido abiertas o proporcionadas.
- Marcar evidencia faltante como not found.
- Separar evidencia empírica, guía oficial, práctica empresarial e inferencia.
- Reportar contradicciones.

## Salida
Informe Markdown con encabezado, resumen, métodos, síntesis, recomendaciones, limitaciones y lista de fuentes.
```

## Rúbrica de evaluación

Puntuar cada informe de 1 a 5.

| Dimensión | Definición |
|---|---|
| Calidad de fuentes | Usa fuentes revisadas por pares, oficiales o empresariales primarias apropiadas para la afirmación. |
| Precisión de citas | Las citas son reales, están correctamente descriptas y respaldan afirmaciones cercanas. |
| Soporte de afirmaciones | Las afirmaciones principales están respaldadas por evidencia o claramente matizadas. |
| Cobertura | Cubre subtemas importantes dentro del alcance declarado. |
| Calidad de síntesis | Compara, resuelve o explica evidencia en lugar de listar fuentes. |
| Manejo de incertidumbre | Declara límites, contradicciones y brechas de evidencia. |
| Utilidad | Ayuda a la audiencia prevista a tomar la decisión objetivo. |
| Esfuerzo de revisión | Tiempo requerido para que un reviewer humano verifique y mejore el informe. Menor esfuerzo puntúa más alto. |

## Procedimiento de medición

1. Elegir 3-5 temas.
2. Ejecutar cada tema bajo las cuatro condiciones de prompt.
3. Guardar cada transcript y salida de Codex.
4. Asignar reviewers ciegos si es posible.
5. Los reviewers puntúan cada salida con la rúbrica.
6. Registrar tiempo de revisión en minutos.
7. Auditar citas:
   - la fuente existe;
   - la fuente fue abierta o proporcionada;
   - los detalles bibliográficos bastan para recuperarla;
   - la fuente citada respalda la afirmación.
8. Contar afirmaciones sin soporte:
   - afirmación factual sin soporte;
   - afirmación sobregeneralizada;
   - cita no correspondiente;
   - cita fabricada o no verificable.

## Métricas de salida

| Métrica | Cálculo |
|---|---|
| Tasa de error de citas | citas erróneas / citas totales |
| Tasa de afirmaciones sin soporte | afirmaciones principales sin soporte / afirmaciones principales totales |
| Puntaje medio de rúbrica | promedio entre dimensiones salvo esfuerzo de revisión |
| Minutos de reviewer | mediana de minutos hasta borrador final aceptable |
| Carga de revisión | cantidad de afirmaciones eliminadas, matizadas o reemplazadas |
| Proporción de fuentes confiables | fuentes de alta confianza / fuentes totales |

## Umbrales de aceptación

Una estrategia de prompting es aceptable como default del equipo si:

- la tasa de error de citas es menor a 5%;
- no sobreviven citas fabricadas a la revisión final;
- la tasa de afirmaciones principales sin soporte es menor a 10%;
- el puntaje medio de rúbrica es al menos 4;
- reviewers coinciden en que la salida es usable tras edición normal.

Para publicación externa o decisiones de alto riesgo, los umbrales deberían ser más estrictos e incluir revisión experta.

## Plan de análisis

Comparar condiciones usando:

- puntaje promedio de rúbrica por condición;
- tasa de error de citas por condición;
- tasa de afirmaciones sin soporte por condición;
- tiempo de revisión por condición;
- notas cualitativas de reviewers.

Resultado esperado:

- La condición D debería rendir mejor en factualidad y revisabilidad.
- La condición B debería ser el mejor default de bajo costo para memos internos de bajo riesgo.
- La condición C puede rendir peor si el contexto adicional no está estructurado.
- La condición A debería ser la más rápida pero la más riesgosa.

## Limitaciones

- Los resultados dependerán de la versión del modelo.
- Reviewers pueden discrepar sobre calidad de síntesis.
- Algunos temas tienen ecosistemas de fuentes más fáciles que otros.
- Chequear citas consume tiempo pero es necesario para informes confiables.
- El experimento mide calidad de informes, no todos los workflows posibles con Codex.

## Siguiente paso recomendado

Ejecutar el experimento con al menos tres temas del trabajo real del equipo. Si la condición D gana como se espera, convertirla en una skill de Codex y mantener la condición B como template más liviano para memos internos de bajo riesgo.

