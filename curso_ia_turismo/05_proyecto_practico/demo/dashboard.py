import pandas as pd
from src.visualization.dashboard import generar_dashboard

if __name__ == "__main__":
    df = pd.read_csv("data/metricas.csv")
    # Calcular métricas adicionales si no existen
    if 'tasa_conversion' not in df.columns:
        df['tasa_conversion'] = df['reservas_nuevas'] / (df['reservas_nuevas'] + df['reservas_canceladas'])
    if 'margen_operativo' not in df.columns:
        df['margen_operativo'] = (df['ingresos'] - df['gastos_operativos']) / df['ingresos']
    generar_dashboard(df, output_html="dashboard_operativo.html") 