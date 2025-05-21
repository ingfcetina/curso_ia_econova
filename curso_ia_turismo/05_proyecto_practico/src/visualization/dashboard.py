import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import os

def generar_dashboard(df_metricas: pd.DataFrame, output_html: str = 'dashboard_operativo.html'):
    fig = make_subplots(
        rows=3, cols=2,
        subplot_titles=(
            'Ocupación y Satisfacción',
            'Ingresos y Gastos',
            'Tasa de Conversión',
            'Clientes Recurrentes',
            'Tiempo de Respuesta',
            'Margen Operativo'
        )
    )
    # Gráfico 1: Ocupación y Satisfacción
    fig.add_trace(
        go.Scatter(x=df_metricas['fecha'], y=df_metricas['ocupacion'], name='Ocupación'),
        row=1, col=1
    )
    fig.add_trace(
        go.Scatter(x=df_metricas['fecha'], y=df_metricas['satisfaccion'], name='Satisfacción'),
        row=1, col=1
    )
    # Gráfico 2: Ingresos y Gastos
    fig.add_trace(
        go.Bar(x=df_metricas['fecha'], y=df_metricas['ingresos'], name='Ingresos'),
        row=1, col=2
    )
    fig.add_trace(
        go.Bar(x=df_metricas['fecha'], y=df_metricas['gastos_operativos'], name='Gastos'),
        row=1, col=2
    )
    # Gráfico 3: Tasa de Conversión
    fig.add_trace(
        go.Scatter(x=df_metricas['fecha'], y=df_metricas['tasa_conversion'], name='Tasa de Conversión'),
        row=2, col=1
    )
    # Gráfico 4: Clientes Recurrentes
    fig.add_trace(
        go.Scatter(x=df_metricas['fecha'], y=df_metricas['clientes_recurrentes'], name='Clientes Recurrentes'),
        row=2, col=2
    )
    # Gráfico 5: Tiempo de Respuesta
    fig.add_trace(
        go.Scatter(x=df_metricas['fecha'], y=df_metricas['tiempo_respuesta'], name='Tiempo de Respuesta'),
        row=3, col=1
    )
    # Gráfico 6: Margen Operativo
    fig.add_trace(
        go.Scatter(x=df_metricas['fecha'], y=df_metricas['margen_operativo'], name='Margen Operativo'),
        row=3, col=2
    )
    fig.update_layout(
        height=1200,
        width=1200,
        title_text='Dashboard Operativo',
        showlegend=True
    )
    fig.write_html(output_html)
    print(f'Dashboard exportado a {output_html}') 