# Estructura del Proyecto de Demostración

```
05_proyecto_practico/
├── demo/                      # Archivos de demostración
│   ├── notebook.ipynb        # Notebook principal con la demo
│   │   ├── 1_chatgpt_analisis.ipynb    # Análisis de reseñas
│   │   ├── 2_claude_tendencias.ipynb   # Análisis de tendencias
│   │   └── 3_deepseek_dashboard.ipynb  # Dashboard operativo
│   ├── dashboard.py          # Dashboard interactivo
│   └── data/                 # Datos de ejemplo
│       ├── reseñas.csv       # Dataset de reseñas
│       ├── metricas.csv      # Métricas operativas
│       └── tendencias.json   # Datos de tendencias
├── src/                      # Código fuente
│   ├── analysis/            # Scripts de análisis
│   │   ├── __init__.py
│   │   ├── chatgpt_analysis.py  # Análisis con ChatGPT
│   │   ├── claude_analysis.py   # Análisis con Claude
│   │   └── deepseek_analysis.py # Análisis con DeepSeek
│   └── visualization/       # Scripts de visualización
│       ├── __init__.py
│       └── dashboard.py     # Generación de dashboard
└── config/                  # Configuración
    └── settings.yaml        # Parámetros de la demo
```

## Descripción de Componentes

### 1. Demo (`demo/`)
- **notebook.ipynb**: Notebook principal que contiene:
  - Análisis de reseñas con ChatGPT (30 min)
  - Análisis de tendencias con Claude (30 min)
  - Dashboard operativo con DeepSeek (30 min)

- **dashboard.py**: Dashboard interactivo que muestra:
  - Métricas en tiempo real
  - Visualizaciones de análisis
  - KPIs principales
  - Recomendaciones

- **data/**: Datos de ejemplo pre-procesados
  - `reseñas.csv`: Dataset de reseñas de TripAdvisor
  - `metricas.csv`: Métricas operativas
  - `tendencias.json`: Datos de tendencias del mercado

### 2. Código Fuente (`src/`)
- **analysis/**: Scripts de análisis
  - `chatgpt_analysis.py`: Análisis de reseñas
  - `claude_analysis.py`: Análisis de tendencias
  - `deepseek_analysis.py`: Análisis operativo

- **visualization/**: Scripts de visualización
  - `dashboard.py`: Generación de dashboard

### 3. Configuración (`config/`)
- `settings.yaml`: Parámetros de la demostración
  - Configuración de APIs
  - Parámetros de análisis
  - Configuración de visualización

## Flujo de la Demostración

1. **Preparación (30 minutos)**
   - Cargar datos de ejemplo
   - Verificar conexión con APIs
   - Preparar notebook
   - Iniciar dashboard

2. **Demostración (90 minutos)**
   - Análisis de reseñas (30 min)
   - Análisis de tendencias (30 min)
   - Dashboard operativo (30 min)

3. **Cierre (15 minutos)**
   - Resumen de resultados
   - Q&A
   - Compartir materiales

## Notas para el Presentador
- Mantener el notebook organizado por secciones
- Tener los datos pre-cargados
- Preparar ejemplos de respaldo
- Mantener el dashboard actualizado
- Tener respuestas preparadas para preguntas comunes 