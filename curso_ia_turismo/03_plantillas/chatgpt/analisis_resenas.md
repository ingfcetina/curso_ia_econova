# Plantilla de Análisis de Reseñas - ChatGPT

## Estructura de Datos

### Hoja 1: Recopilación de Reseñas
| Campo | Descripción | Ejemplo | Prompt Sugerido |
|-------|-------------|---------|-----------------|
| ID | Identificador | "REV001" | "Analiza la reseña [ID] y extrae los puntos clave y sentimiento" |
| Fuente | Plataforma | "TripAdvisor" | "Evalúa las reseñas de la fuente [FUENTE] y su impacto" |
| Fecha | Período | "2024-03" | "Analiza las reseñas del período [FECHA] y sus tendencias" |
| Contenido | Texto | "Excelente..." | "Extrae insights clave de la reseña [CONTENIDO]" |
| Valoración | Puntuación | "4.5/5" | "Evalúa la valoración [VALORACION] y su contexto" |

### Hoja 2: Análisis de Sentimiento
| Campo | Descripción | Ejemplo | Prompt Sugerido |
|-------|-------------|---------|-----------------|
| Sentimiento | Tono | "Positivo" | "Analiza el sentimiento general de [RESENA] y sus matices" |
| Intensidad | Nivel | "Alto" | "Evalúa la intensidad del sentimiento en [RESENA]" |
| Aspectos | Elementos | "Servicio" | "Identifica los aspectos clave mencionados en [RESENA]" |
| Palabras | Clave | "Excelente" | "Extrae las palabras clave de [RESENA] y su contexto" |
| Tono | Emocional | "Entusiasta" | "Analiza el tono emocional de [RESENA]" |

### Hoja 3: Tendencias
| Campo | Descripción | Ejemplo | Prompt Sugerido |
|-------|-------------|---------|-----------------|
| Categoría | Tipo | "Servicio" | "Analiza las tendencias en la categoría [CATEGORIA]" |
| Frecuencia | Repetición | "Alta" | "Evalúa la frecuencia de menciones de [TEMA]" |
| Temporalidad | Patrón | "Estacional" | "Identifica patrones temporales en [CATEGORIA]" |
| Correlación | Relación | "Precio-Calidad" | "Analiza correlaciones entre [ASPECTO1] y [ASPECTO2]" |
| Cambios | Evolución | "Mejora" | "Evalúa los cambios en [CATEGORIA] a lo largo del tiempo" |

### Hoja 4: Plan de Mejora
| Campo | Descripción | Ejemplo | Prompt Sugerido |
|-------|-------------|---------|-----------------|
| Área | Mejora | "Atención" | "Analiza las oportunidades de mejora en [AREA]" |
| Prioridad | Nivel | "Alta" | "Evalúa la prioridad de implementar [MEJORA]" |
| Acción | Propuesta | "Capacitación" | "Sugiere acciones específicas para [AREA]" |
| Responsable | Rol | "Supervisor" | "Identifica el responsable de implementar [ACCION]" |
| Seguimiento | Métrica | "Satisfacción" | "Propone métricas para medir el impacto de [ACCION]" |

## Instrucciones
1. Recopilar reseñas
2. Analizar sentimiento
3. Identificar tendencias
4. Generar insights
5. Planificar mejoras

## Métricas
| Métrica | Descripción | Fórmula | Objetivo |
|---------|-------------|---------|----------|
| NPS | Net Promoter Score | Promotores - Detractores | >50 |
| Satisfacción | Media | Suma valoraciones / Total | >4.5/5 |
| Volumen | Reseñas | Total reseñas / Período | >100/mes |
| Tiempo Respuesta | Atención | Tiempo respuesta / Total | <24h |
| Mejora | Evolución | (Actual - Anterior) / Anterior | >5% |

## Plantillas de Prompt

### 1. Análisis Individual
```
Analiza la reseña con:
ID: [ID]
Fuente: [FUENTE]
Fecha: [FECHA]

Proporciona:
- Sentimiento general
- Aspectos clave
- Puntos fuertes
- Áreas de mejora
- Recomendaciones
```

### 2. Análisis de Tendencias
```
Evalúa las tendencias con:
Categoría: [CATEGORIA]
Período: [PERIODO]
Métrica: [METRICA]

Identifica:
- Patrones principales
- Cambios significativos
- Factores de influencia
- Oportunidades
- Riesgos
```

### 3. Generación de Insights
```
Genera insights con:
Área: [AREA]
Período: [PERIODO]
Enfoque: [ENFOQUE]

Desarrolla:
- Hallazgos clave
- Tendencias
- Correlaciones
- Oportunidades
- Recomendaciones
```

### 4. Plan de Mejora
```
Desarrolla plan para:
Área: [AREA]
Objetivo: [OBJETIVO]
Período: [PERIODO]

Incluye:
- Acciones específicas
- Responsables
- Timeline
- Métricas
- Seguimiento
```

## Registro de Análisis
| Fecha | Tipo | Alcance | Hallazgos | Acciones |
|-------|------|---------|-----------|----------|
| [FECHA] | Mensual | General | [HALLAZGOS] | [ACCIONES] |
| [FECHA] | Trimestral | Tendencias | [HALLAZGOS] | [ACCIONES] |
| [FECHA] | Anual | Estratégico | [HALLAZGOS] | [ACCIONES] |

## Mejores Prácticas

### 1. Recopilación
- Monitorear fuentes
- Validar datos
- Normalizar formatos
- Documentar contexto
- Mantener historial

### 2. Análisis
- Usar NLP
- Considerar contexto
- Validar sentimiento
- Identificar patrones
- Documentar hallazgos

### 3. Acción
- Priorizar mejoras
- Asignar recursos
- Establecer plazos
- Monitorear resultados
- Ajustar según necesario

### 4. Seguimiento
- Medir impacto
- Evaluar cambios
- Actualizar métricas
- Compartir resultados
- Documentar aprendizajes

## Recursos

### 1. Fuentes
- TripAdvisor
- Google Reviews
- Booking
- Expedia
- Redes sociales

### 2. Herramientas
- ChatGPT
- Excel
- Power BI
- Tableau
- Python/R

### 3. Plantillas
- Análisis de reseñas
- Reportes
- Dashboards
- Presentaciones

### 4. Contactos
- Equipo de análisis
- Atención al cliente
- Marketing
- Gestión
- Operaciones 