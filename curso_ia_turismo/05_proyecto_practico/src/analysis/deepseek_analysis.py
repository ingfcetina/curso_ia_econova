import pandas as pd
import json
import os
from dotenv import load_dotenv
from typing import Dict, Any
import deepseek

class DeepSeekAnalyzer:
    def __init__(self):
        load_dotenv()
        self.client = deepseek.Client()
        self.model = "deepseek-chat"
        self.temperature = 0.7

    def analyze_kpis(self, df: pd.DataFrame) -> Dict[str, Any]:
        prompt = f"""Analiza las siguientes métricas operativas y proporciona:
        1. KPIs principales y su evolución
        2. Correlaciones significativas
        3. Alertas y anomalías
        4. Recomendaciones de optimización
        
        Datos: {df.to_dict('records')}
        
        Responde en formato JSON."""
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            temperature=self.temperature
        )
        return json.loads(response.choices[0].message.content)

    def generate_recommendations(self, df: pd.DataFrame) -> Dict[str, Any]:
        prompt = f"""Basado en el análisis de las métricas operativas, proporciona:
        1. Resumen ejecutivo
        2. Áreas de mejora identificadas
        3. Recomendaciones específicas
        4. Plan de acción
        
        Datos: {df.to_dict('records')}
        
        Responde en formato JSON."""
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            temperature=self.temperature
        )
        return json.loads(response.choices[0].message.content)

if __name__ == "__main__":
    df = pd.read_csv('../../demo/data/metricas.csv')
    analyzer = DeepSeekAnalyzer()
    resultados = {
        'kpis': analyzer.analyze_kpis(df),
        'recomendaciones': analyzer.generate_recommendations(df)
    }
    with open('../../demo/results/deepseek_analysis.json', 'w', encoding='utf-8') as f:
        json.dump(resultados, f, indent=2, ensure_ascii=False) 