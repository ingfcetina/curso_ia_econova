# Plantilla de Análisis de Feedback - Claude

## Estructura de Datos

### Hoja 1: Recopilación de Reseñas
| Campo | Descripción | Ejemplo | Prompt Sugerido |
|-------|-------------|---------|-----------------|
| ID | Identificador | "REV001" | "Analiza la reseña [ID] y extrae los puntos clave de satisfacción e insatisfacción" |
| Fuente | Origen | "TripAdvisor" | "Identifica patrones comunes en las reseñas de [FUENTE]" |
| Fecha | Publicación | "2024-02" | "Analiza las tendencias de feedback para el período [FECHA]" |
| Contenido | Texto | "Excelente servicio..." | "Extrae los aspectos más mencionados en la reseña: [CONTENIDO]" |
| Valoración | Puntuación | "4.5/5" | "Evalúa la consistencia entre la valoración [VALORACION] y el contenido" |

### Hoja 2: Análisis de Sentimiento
| Campo | Descripción | Ejemplo | Prompt Sugerido |
|-------|-------------|---------|-----------------|
| Sentimiento | Tono | "Positivo" | "Determina el sentimiento general de la reseña: [CONTENIDO]" |
| Intensidad | Nivel | "Alto" | "Evalúa la intensidad del sentimiento en: [CONTENIDO]" |
| Aspectos | Elementos | "Servicio, Limpieza" | "Identifica los aspectos mencionados en: [CONTENIDO]" |
| Palabras | Clave | "amable, rápido" | "Extrae las palabras clave que indican sentimiento en: [CONTENIDO]" |
| Tono | Estilo | "Formal" | "Analiza el tono de comunicación en: [CONTENIDO]" |

### Hoja 3: Tendencias
| Campo | Descripción | Ejemplo | Prompt Sugerido |
|-------|-------------|---------|-----------------|
| Categoría | Tipo | "Servicio" | "Identifica tendencias en la categoría [CATEGORIA] durante [PERIODO]" |
| Frecuencia | Repetición | "Alta" | "Analiza la frecuencia de menciones sobre [CATEGORIA]" |
| Temporalidad | Patrón | "Estacional" | "Evalúa patrones temporales en las reseñas de [CATEGORIA]" |
| Correlación | Relación | "Servicio-Satisfacción" | "Busca correlaciones entre [CATEGORIA] y otros aspectos" |
| Cambios | Evolución | "Mejora" | "Analiza la evolución de [CATEGORIA] a lo largo del tiempo" |

### Hoja 4: Plan de Mejora
| Campo | Descripción | Ejemplo | Prompt Sugerido |
|-------|-------------|---------|-----------------|
| Área | Departamento | "Atención" | "Sugiere mejoras para el área [AREA] basadas en el feedback" |
| Prioridad | Nivel | "Alta" | "Evalúa la prioridad de implementar mejoras en [AREA]" |
| Acción | Medida | "Capacitación" | "Propón acciones específicas para mejorar [AREA]" |
| Responsable | Rol | "Supervisor" | "Asigna responsabilidades para implementar [ACCION]" |
| Seguimiento | Métrica | "NPS" | "Define métricas para medir el impacto de [ACCION]" |

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
| Tiempo Respuesta | Medio | Suma tiempos / Total | <24h |
| Mejora | Tasa | (Actual - Anterior) / Anterior | >5% |

## Plantillas de Prompt

### 1. Análisis Individual
```
Analiza la siguiente reseña:
ID: [ID]
Fuente: [FUENTE]
Fecha: [FECHA]
Contenido: [CONTENIDO]
Valoración: [VALORACION]

Proporciona:
- Sentimiento general
- Aspectos clave mencionados
- Puntos fuertes
- Áreas de mejora
- Recomendaciones específicas
```

### 2. Análisis de Tendencias
```
Analiza las tendencias en las reseñas con:
Período: [PERIODO]
Categoría: [CATEGORIA]
Fuente: [FUENTE]

Identifica:
- Patrones comunes
- Cambios temporales
- Correlaciones
- Insights clave
- Oportunidades de mejora
```

### 3. Generación de Insights
```
Genera insights basados en:
Conjunto de reseñas: [RESENAS]
Período: [PERIODO]
Área: [AREA]

Incluye:
- Hallazgos principales
- Tendencias significativas
- Causas raíz
- Impacto en negocio
- Recomendaciones estratégicas
```

### 4. Plan de Mejora
```
Desarrolla un plan de mejora para:
Área: [AREA]
Hallazgos: [HALLAZGOS]
Prioridad: [PRIORIDAD]

Detalla:
- Acciones específicas
- Responsables
- Plazos
- Métricas de seguimiento
- Recursos necesarios
```

## Registro de Análisis
| Fecha | Tipo | Alcance | Hallazgos | Acciones |
|-------|------|---------|-----------|----------|
| [FECHA] | Mensual | General | [HALLAZGOS] | [ACCIONES] |
| [FECHA] | Trimestral | Área | [HALLAZGOS] | [ACCIONES] |
| [FECHA] | Anual | Estratégico | [HALLAZGOS] | [ACCIONES] |

## Mejores Prácticas

### 1. Recopilación
- Monitorear fuentes
- Validar datos
- Normalizar formatos
- Documentar contexto
- Mantener historial

### 2. Análisis
- Usar métricas relevantes
- Considerar contexto
- Validar patrones
- Documentar hallazgos
- Compartir insights

### 3. Acción
- Priorizar mejoras
- Asignar recursos
- Establecer plazos
- Comunicar cambios
- Medir impacto

### 4. Seguimiento
- Monitorear métricas
- Evaluar efectividad
- Ajustar acciones
- Documentar resultados
- Compartir aprendizajes

## Recursos

### 1. Fuentes
- TripAdvisor
- Google Reviews
- Booking.com
- Redes sociales
- Encuestas

### 2. Herramientas
- Claude
- Analíticas
- CRM
- Dashboards
- Herramientas de texto

### 3. Plantillas
- Análisis de reseñas
- Reportes de tendencias
- Planes de mejora
- Dashboards

### 4. Contactos
- Equipo de análisis
- Atención al cliente
- Operaciones
- Gestión
- Marketing 