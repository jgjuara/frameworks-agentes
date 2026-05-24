# Marco operativo: Codex para informes abiertos de investigación

**Resumen:** Este marco traduce la revisión de literatura en un proceso operativo para un equipo de investigación que usa Codex para redactar informes sin una lista fija de fuentes. Define capas de contexto, clases de tarea, reglas de fuentes, puertas de revisión y patrones reutilizables de prompt.

## Principio operativo

No debería pedirse a Codex que produzca un informe final de investigación en un solo paso salvo que la tarea sea de bajo riesgo y la persona usuaria ya haya proporcionado material fuente confiable.

Para informes abiertos, Codex debería producir artefactos intermedios:

1. inventario de fuentes;
2. matriz de evidencia;
3. outline del informe;
4. borrador;
5. claim ledger;
6. markdown final.

## Clases de tarea

| Clase | Ejemplo | Autonomía de Codex | Controles requeridos |
|---|---|---:|---|
| R0: solo estilo | Reescribir un informe existente. | Alta | Preservar afirmaciones; no nuevas fuentes. |
| R1: resumen acotado a fuentes | Resumir 3 papers provistos. | Alta | Citar solo fuentes provistas; extraer citas primero. |
| R2: memo de investigación acotado | Informe usando fuentes revisadas por pares y oficiales. | Media | Inventario de fuentes y matriz de evidencia. |
| R3: informe de decisión | Informe informa estrategia, política, financiamiento o publicación. | Media-baja | Claim ledger, log de contradicciones, signoff de reviewer. |
| R4: dominio de alto riesgo | Médico, legal, financiero, seguridad, población sensible. | Baja | Revisión experta humana, índice estricto de fuentes, sin afirmaciones finales sin supervisión. |

## Capas de contexto

### Capa 1: contexto duradero del equipo

Poner en `AGENTS.md` o en un archivo de estrategia específico de tarea:

- idioma preferido y estándares de documentación;
- jerarquía de fuentes por dominio;
- política de citas;
- restricciones de privacidad y datos;
- definición de "done";
- expectativas de revisión.

Mantenerlo breve. Si crece, mover flujos detallados a archivos Markdown separados o skills de Codex.

### Capa 2: brief de tarea

Toda solicitud de informe no trivial debería especificar:

- objetivo;
- pregunta de investigación;
- audiencia;
- alcance;
- exclusiones;
- jerarquía de fuentes;
- formato de salida;
- criterios de aceptación;
- clase de riesgo;
- método de validación.

### Capa 3: contexto de evidencia

Codex debería construir esto durante la tarea:

- título de fuente, autor, año, organización, URL/DOI;
- tipo de fuente y nivel de confianza;
- razón de inclusión;
- hallazgos clave;
- limitaciones;
- contradicciones;
- afirmaciones respaldadas por la fuente.

## Política de fuentes

Jerarquía default de fuentes:

1. papers revisados por pares, revisiones sistemáticas y papers de conferencias importantes;
2. fuentes oficiales gubernamentales, estadísticas, de estándares o institucionales;
3. publicaciones primarias de investigación e ingeniería empresarial de laboratorios importantes;
4. blogs técnicos de alta calidad solo cuando no haya fuentes primarias disponibles;
5. noticias y comentarios solo para eventos recientes o contexto de ecosistema.

Reglas:

- No citar una fuente salvo que haya sido abierta o proporcionada.
- Preferir papers originales antes que resúmenes de blog.
- Usar documentación oficial para comportamiento actual de producto.
- Separar resultados empíricos de opinión experta.
- Registrar fecha de fuente y fecha de acceso cuando el tema sea sensible al tiempo.
- Ante evidencia contradictoria, reportar la contradicción en lugar de forzar consenso.

## Artefactos intermedios requeridos

### Inventario de fuentes

| Fuente | Tipo | Por qué se incluye | Nivel de confianza | Notas |
|---|---|---|---:|---|

### Matriz de evidencia

| Afirmación/Tema | Fuente de soporte | Tipo de evidencia | Limitaciones |
|---|---|---|---|

### Claim ledger

| Afirmación del informe | Cita | Estado de soporte | Acción |
|---|---|---|---|
| [Afirmación] | [Fuente] | respaldada / parcial / sin soporte | mantener / matizar / eliminar |

## Patrón de prompt

```markdown
You are helping a research team produce a report. Treat this as a literature-review workflow, not a one-shot writing task.

First, build a source inventory from trusted sources. Prioritize peer-reviewed work, official sources, and primary enterprise research. Do not cite a source unless you opened it or it was provided.

Second, create an evidence matrix. Separate empirical findings, official guidance, enterprise practice, and inference.

Third, propose an outline. State assumptions and unresolved contradictions.

Fourth, draft the report with inline citations near the claims they support.

Fifth, create a claim ledger for major claims. Remove or qualify unsupported claims before finalizing.
```

## Checklist de review gate

Antes de aceptar un informe generado por Codex:

- [ ] ¿El resumen coincide con los hallazgos reales?
- [ ] ¿Los tipos de fuente son apropiados para la fuerza de las afirmaciones?
- [ ] ¿Las citas son reales y fueron abiertas/proporcionadas?
- [ ] ¿Las citas están cerca de las afirmaciones que respaldan?
- [ ] ¿Las afirmaciones sin soporte se eliminaron o matizaron?
- [ ] ¿Se declaran limitaciones de fuentes?
- [ ] ¿Se reportan contradicciones?
- [ ] ¿El informe distingue evidencia de recomendación?
- [ ] ¿La sección final indica qué no fue verificado?

## Activos de equipo recomendados

Crear estos archivos reutilizables:

- `AGENTS.md`: reglas duraderas de Codex.
- `strategy/RESEARCH_SOURCE_POLICY.md`: jerarquía de fuentes específica de dominio.
- `strategy/RESEARCH_REPORT_TEMPLATE.md`: formato de informe.
- `strategy/CLAIM_LEDGER_TEMPLATE.md`: tabla de verificación.
- `.codex/skills/research-report/SKILL.md`: skill opcional cuando el flujo se estabilice.

## Defaults prácticos

| Situación | Default de prompting |
|---|---|
| Usuario no tiene lista de fuentes | Exigir inventario de fuentes antes de redactar. |
| Usuario aporta muchas fuentes | Pedir a Codex extraer notas de fuente antes de sintetizar. |
| Tema actual | Navegar; incluir fechas de publicación y fecha de acceso. |
| Tema académico | Preferir revisiones sistemáticas y papers primarios. |
| Informe para publicación | Exigir auditoría manual de citas. |
| Informe para estrategia interna | Exigir matriz de evidencia y limitaciones. |
| Evidencia de fuentes es débil | Declarar incertidumbre; no elevar fuerza de afirmación. |

## Modos de falla y controles

| Modo de falla | Control |
|---|---|
| Citas fabricadas | Citar solo fuentes abiertas/proporcionadas; ejecutar auditoría de citas. |
| Source laundering | Registrar si la fuente es primaria, secundaria o comentario. |
| Contexto enterrado | Usar matriz de evidencia en lugar de volcados masivos de fuentes. |
| Síntesis sobreconfiada | Exigir secciones de incertidumbre y contradicción. |
| Brechas de fuente ocultas | Incluir términos de búsqueda y notas de exclusión. |
| Prompt inflado | Mover reglas duraderas a `AGENTS.md` o skills. |
| Aceptación vaga | Definir "done when" antes de redactar. |

## Recomendación final

Usar Codex como agente de workflow de investigación, no como generador aislado de informes. El mejor marco es un proceso por etapas, basado en evidencia, con contexto inicial compacto y artefactos explícitos de revisión.

