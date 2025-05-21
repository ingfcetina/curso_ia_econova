# Plantilla de Análisis de Mercado - DeepSeek

## Estructura de Datos

### Hoja 1: Datos de Mercado
| Campo | Descripción | Ejemplo | Consulta Sugerida |
|-------|-------------|---------|------------------|
| Mercado | Segmento | "Turismo" | "SELECT mercado, COUNT(*) FROM datos_mercado GROUP BY mercado" |
| Tamaño | Volumen | "1000M€" | "SELECT SUM(tamano) FROM datos_mercado WHERE periodo = [PERIODO]" |
| Crecimiento | Tasa | "5%" | "SELECT AVG(crecimiento) FROM datos_mercado WHERE mercado = [MERCADO]" |
| Estacionalidad | Índice | "1.2" | "SELECT AVG(estacionalidad) FROM datos_mercado GROUP BY mes" |
| Tendencia | Dirección | "Alza" | "SELECT tendencia, COUNT(*) FROM datos_mercado GROUP BY tendencia" |

### Hoja 2: Análisis Competitivo
| Campo | Descripción | Ejemplo | Consulta Sugerida |
|-------|-------------|---------|------------------|
| Competidor | Nombre | "Hotel A" | "SELECT competidor, COUNT(*) FROM competencia GROUP BY competidor" |
| Cuota | Mercado | "15%" | "SELECT AVG(cuota) FROM competencia WHERE mercado = [MERCADO]" |
| Productos | Oferta | "Hotel" | "SELECT producto, COUNT(*) FROM competencia GROUP BY producto" |
| Precios | Rango | "100-200€" | "SELECT AVG(precio) FROM competencia WHERE producto = [PRODUCTO]" |
| Diferenciación | Factor | "Servicio" | "SELECT factor, COUNT(*) FROM competencia GROUP BY factor" |

### Hoja 3: Oportunidades
| Campo | Descripción | Ejemplo | Consulta Sugerida |
|-------|-------------|---------|------------------|
| Área | Mercado | "Digital" | "SELECT area, COUNT(*) FROM oportunidades GROUP BY area" |
| Potencial | Valor | "500M€" | "SELECT SUM(potencial) FROM oportunidades WHERE area = [AREA]" |
| Viabilidad | Índice | "0.8" | "SELECT AVG(viabilidad) FROM oportunidades WHERE tipo = [TIPO]" |
| Tiempo | Horizonte | "1 año" | "SELECT AVG(tiempo) FROM oportunidades WHERE area = [AREA]" |
| Recursos | Necesarios | "100K€" | "SELECT SUM(recursos) FROM oportunidades WHERE viabilidad > 0.7" |

### Hoja 4: Amenazas
| Campo | Descripción | Ejemplo | Consulta Sugerida |
|-------|-------------|---------|------------------|
| Tipo | Categoría | "Competitiva" | "SELECT tipo, COUNT(*) FROM amenazas GROUP BY tipo" |
| Impacto | Nivel | "Alto" | "SELECT AVG(impacto) FROM amenazas WHERE tipo = [TIPO]" |
| Probabilidad | Tasa | "30%" | "SELECT AVG(probabilidad) FROM amenazas WHERE area = [AREA]" |
| Tiempo | Horizonte | "6 meses" | "SELECT AVG(tiempo) FROM amenazas WHERE impacto > 0.7" |
| Mitigación | Acción | "Diversificación" | "SELECT accion, COUNT(*) FROM amenazas GROUP BY accion" |

## Instrucciones
1. Recopilar datos de mercado
2. Analizar competencia
3. Identificar oportunidades
4. Evaluar amenazas
5. Generar insights

## Métricas
| Métrica | Descripción | Fórmula | Objetivo |
|---------|-------------|---------|----------|
| Cuota de Mercado | Participación | Ventas / Total mercado | >20% |
| Tasa de Crecimiento | Evolución | (Actual - Anterior) / Anterior | >5% |
| Rentabilidad | Margen | Beneficio / Ventas | >15% |
| Eficiencia | Operativa | Output / Input | >90% |
| Posicionamiento | Ranking | Posición / Total | Top 3 |

## Consultas Avanzadas

### 1. Análisis de Mercado
```sql
SELECT 
    mercado,
    SUM(tamano) as tamano_total,
    AVG(crecimiento) as crecimiento_medio,
    AVG(estacionalidad) as estacionalidad_media,
    COUNT(*) as numero_registros
FROM datos_mercado
WHERE periodo >= DATE_SUB(NOW(), INTERVAL 1 YEAR)
GROUP BY mercado
ORDER BY tamano_total DESC
```

### 2. Análisis Competitivo
```sql
SELECT 
    competidor,
    AVG(cuota) as cuota_media,
    COUNT(DISTINCT producto) as numero_productos,
    AVG(precio) as precio_medio,
    COUNT(DISTINCT factor) as factores_diferenciacion
FROM competencia
WHERE mercado = [MERCADO]
GROUP BY competidor
ORDER BY cuota_media DESC
```

### 3. Análisis de Oportunidades
```sql
SELECT 
    area,
    SUM(potencial) as potencial_total,
    AVG(viabilidad) as viabilidad_media,
    AVG(tiempo) as tiempo_medio,
    SUM(recursos) as recursos_necesarios
FROM oportunidades
WHERE viabilidad > 0.7
GROUP BY area
ORDER BY potencial_total DESC
```

### 4. Análisis de Amenazas
```sql
SELECT 
    tipo,
    AVG(impacto) as impacto_medio,
    AVG(probabilidad) as probabilidad_media,
    AVG(tiempo) as tiempo_medio,
    COUNT(DISTINCT accion) as acciones_mitigacion
FROM amenazas
WHERE impacto > 0.7 OR probabilidad > 0.7
GROUP BY tipo
ORDER BY impacto_medio DESC
```

## Registro de Análisis
| Fecha | Tipo | Alcance | Hallazgos | Acciones |
|-------|------|---------|-----------|----------|
| [FECHA] | Mensual | Mercado | [HALLAZGOS] | [ACCIONES] |
| [FECHA] | Trimestral | Competencia | [HALLAZGOS] | [ACCIONES] |
| [FECHA] | Anual | Estrategia | [HALLAZGOS] | [ACCIONES] |

## Mejores Prácticas

### 1. Recopilación de Datos
- Validar fuentes
- Actualizar periódicamente
- Normalizar formatos
- Documentar procesos

### 2. Análisis
- Usar métricas relevantes
- Comparar períodos
- Validar resultados
- Documentar hallazgos

### 3. Estrategia
- Definir objetivos claros
- Priorizar acciones
- Asignar recursos
- Medir resultados

### 4. Implementación
- Planificar acciones
- Asignar responsables
- Establecer plazos
- Monitorear avances

## Recursos

### 1. Fuentes de Datos
- Estudios de mercado
- Informes sectoriales
- Datos internos
- Competencia
- Regulaciones

### 2. Herramientas
- DeepSeek
- Excel
- Power BI
- Tableau
- Python/R

### 3. Plantillas
- Análisis de mercado
- Estudios competitivos
- Planes estratégicos
- Reportes

### 4. Contactos
- Equipo de análisis
- Marketing
- Ventas
- Gestión
- Consultores 