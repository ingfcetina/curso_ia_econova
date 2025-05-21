# Plantilla de Dashboard Operativo - DeepSeek

## Estructura de Datos

### Hoja 1: KPIs Operativos
| Campo | Descripción | Ejemplo | Consulta Sugerida |
|-------|-------------|---------|------------------|
| Eficiencia | Tasa | "85%" | "SELECT AVG(eficiencia) FROM operaciones WHERE fecha = [FECHA]" |
| Tiempo | Medio | "2.5h" | "SELECT AVG(tiempo) FROM operaciones WHERE tipo = [TIPO]" |
| Calidad | Índice | "4.8/5" | "SELECT AVG(calidad) FROM operaciones WHERE area = [AREA]" |
| Costo | Unitario | "150€" | "SELECT AVG(costo) FROM operaciones WHERE periodo = [PERIODO]" |
| Satisfacción | NPS | "80" | "SELECT AVG(satisfaccion) FROM operaciones WHERE servicio = [SERVICIO]" |

### Hoja 2: Análisis de Eficiencia
| Campo | Descripción | Ejemplo | Consulta Sugerida |
|-------|-------------|---------|------------------|
| Proceso | Nombre | "Check-in" | "SELECT proceso, AVG(eficiencia) FROM operaciones GROUP BY proceso" |
| Recurso | Tipo | "Personal" | "SELECT recurso, COUNT(*) FROM operaciones GROUP BY recurso" |
| Tiempo | Duración | "30min" | "SELECT AVG(tiempo) FROM operaciones WHERE proceso = [PROCESO]" |
| Costo | Unitario | "50€" | "SELECT AVG(costo) FROM operaciones WHERE recurso = [RECURSO]" |
| Mejora | Potencial | "15%" | "SELECT (max_eficiencia - AVG(eficiencia)) FROM operaciones" |

### Hoja 3: Gestión de Recursos
| Campo | Descripción | Ejemplo | Consulta Sugerida |
|-------|-------------|---------|------------------|
| Tipo | Recurso | "Humano" | "SELECT tipo, COUNT(*) FROM recursos GROUP BY tipo" |
| Disponibilidad | Tasa | "90%" | "SELECT AVG(disponibilidad) FROM recursos WHERE tipo = [TIPO]" |
| Utilización | Índice | "75%" | "SELECT AVG(utilizacion) FROM recursos WHERE periodo = [PERIODO]" |
| Costo | Total | "5000€" | "SELECT SUM(costo) FROM recursos WHERE tipo = [TIPO]" |
| Productividad | Ratio | "1.2" | "SELECT AVG(productividad) FROM recursos WHERE area = [AREA]" |

### Hoja 4: Análisis de Costos
| Campo | Descripción | Ejemplo | Consulta Sugerida |
|-------|-------------|---------|------------------|
| Categoría | Tipo | "Operativo" | "SELECT categoria, SUM(costo) FROM costos GROUP BY categoria" |
| Período | Mes | "2024-02" | "SELECT periodo, AVG(costo) FROM costos GROUP BY periodo" |
| Producto | Servicio | "Hotel" | "SELECT producto, SUM(costo) FROM costos GROUP BY producto" |
| Tendencia | Variación | "+5%" | "SELECT (costo_actual - costo_anterior)/costo_anterior FROM costos" |
| Presupuesto | Límite | "10000€" | "SELECT presupuesto FROM costos WHERE categoria = [CATEGORIA]" |

## Instrucciones
1. Cargar datos operativos
2. Validar métricas
3. Generar visualizaciones
4. Analizar tendencias
5. Identificar mejoras

## Métricas
| Métrica | Descripción | Fórmula | Objetivo |
|---------|-------------|---------|----------|
| Eficiencia | Operativa | Output / Input | >90% |
| Productividad | Laboral | Producción / Horas | >1.2 |
| Calidad | Servicio | Satisfacción / Total | >4.5/5 |
| Costo | Unitario | Costo total / Unidades | <100€ |
| Satisfacción | Cliente | NPS | >75 |

## Consultas Avanzadas

### 1. Análisis de Eficiencia
```sql
SELECT 
    proceso,
    AVG(eficiencia) as eficiencia_media,
    AVG(tiempo) as tiempo_medio,
    AVG(costo) as costo_medio,
    AVG(calidad) as calidad_media
FROM operaciones
WHERE fecha >= DATE_SUB(NOW(), INTERVAL 1 MONTH)
GROUP BY proceso
ORDER BY eficiencia_media DESC
```

### 2. Análisis de Recursos
```sql
SELECT 
    tipo_recurso,
    COUNT(*) as total_recursos,
    AVG(disponibilidad) as disponibilidad_media,
    AVG(utilizacion) as utilizacion_media,
    SUM(costo) as costo_total
FROM recursos
WHERE periodo = [PERIODO]
GROUP BY tipo_recurso
ORDER BY costo_total DESC
```

### 3. Análisis de Costos
```sql
SELECT 
    categoria,
    SUM(costo) as costo_total,
    AVG(costo) as costo_medio,
    MAX(costo) as costo_maximo,
    MIN(costo) as costo_minimo
FROM costos
WHERE fecha >= DATE_SUB(NOW(), INTERVAL 3 MONTHS)
GROUP BY categoria
ORDER BY costo_total DESC
```

### 4. Análisis de Rendimiento
```sql
SELECT 
    area,
    AVG(eficiencia) as eficiencia_media,
    AVG(productividad) as productividad_media,
    AVG(calidad) as calidad_media,
    AVG(satisfaccion) as satisfaccion_media
FROM operaciones
WHERE fecha >= DATE_SUB(NOW(), INTERVAL 1 MONTH)
GROUP BY area
ORDER BY eficiencia_media DESC
```

## Registro de Seguimiento
| Fecha | Área | Métrica | Valor | Acción |
|-------|------|---------|-------|--------|
| [FECHA] | Operaciones | Eficiencia | [VALOR] | [ACCION] |
| [FECHA] | Recursos | Utilización | [VALOR] | [ACCION] |
| [FECHA] | Costos | Variación | [VALOR] | [ACCION] |

## Mejores Prácticas

### 1. Monitoreo
- Actualizar datos en tiempo real
- Validar métricas
- Documentar anomalías
- Compartir alertas

### 2. Análisis
- Usar KPIs relevantes
- Comparar períodos
- Identificar tendencias
- Validar resultados

### 3. Optimización
- Automatizar procesos
- Reducir tiempos
- Mejorar calidad
- Controlar costos

### 4. Reportes
- Generar dashboards
- Programar actualizaciones
- Compartir insights
- Documentar acciones

## Recursos

### 1. Fuentes de Datos
- Sistema operativo
- CRM
- ERP
- Analytics
- Encuestas

### 2. Herramientas
- DeepSeek
- Excel
- Power BI
- Tableau
- Python/R

### 3. Plantillas
- Dashboards
- Gráficos
- Reportes
- Alertas

### 4. Contactos
- Equipo operativo
- Gestión
- IT
- Calidad 