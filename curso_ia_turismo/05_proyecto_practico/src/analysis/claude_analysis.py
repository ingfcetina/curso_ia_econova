import pandas as pd
import json
import os
from dotenv import load_dotenv
from typing import Dict, Any
import anthropic

class ClaudeAnalyzer:
    def __init__(self):
        load_dotenv()
        self.client = anthropic.Anthropic()
        self.model = "claude-3-opus-20240229"
        self.temperature = 0.7

    def analyze_segment(self, segmento: str, datos: dict) -> Dict[str, Any]:
        prompt = f"""Analiza las siguientes tendencias del segmento {segmento} y proporciona:
        1. Resumen de la situación actual
        2. Oportunidades identificadas
        3. Amenazas potenciales
        4. Recomendaciones estratégicas
        
        Datos: {json.dumps(datos, indent=2)}
        
        Responde en formato JSON."""
        response = self.client.messages.create(
            model=self.model,
            max_tokens=1000,
            temperature=self.temperature,
            messages=[{"role": "user", "content": prompt}]
        )
        return json.loads(response.content[0].text)

    def analyze_competencia(self, datos: dict) -> Dict[str, Any]:
        prompt = f"""Analiza la siguiente información competitiva y proporciona:
        1. Análisis de la posición competitiva
        2. Ventajas competitivas
        3. Áreas de mejora
        4. Estrategias recomendadas
        
        Datos: {json.dumps(datos, indent=2)}
        
        Responde en formato JSON."""
        response = self.client.messages.create(
            model=self.model,
            max_tokens=1000,
            temperature=self.temperature,
            messages=[{"role": "user", "content": prompt}]
        )
        return json.loads(response.content[0].text)

    def generate_estrategias(self, datos_completos: dict) -> Dict[str, Any]:
        prompt = f"""Basado en toda la información disponible, genera:
        1. Estrategia general
        2. Objetivos específicos por segmento
        3. Plan de implementación
        4. KPIs de seguimiento
        
        Datos: {json.dumps(datos_completos, indent=2)}
        
        Responde en formato JSON."""
        response = self.client.messages.create(
            model=self.model,
            max_tokens=1000,
            temperature=self.temperature,
            messages=[{"role": "user", "content": prompt}]
        )
        return json.loads(response.content[0].text)

if __name__ == "__main__":
    # Ejemplo de uso
    with open('../../demo/data/tendencias.json', 'r', encoding='utf-8') as f:
        tendencias = json.load(f)
    analyzer = ClaudeAnalyzer()
    resultados = {}
    for segmento, datos in tendencias['tendencias_mercado']['segmentos'].items():
        resultados[segmento] = analyzer.analyze_segment(segmento, datos)
    resultados['competencia'] = analyzer.analyze_competencia(tendencias['tendencias_mercado']['competencia'])
    resultados['estrategias'] = analyzer.generate_estrategias(tendencias['tendencias_mercado'])
    with open('../../demo/results/claude_analysis.json', 'w', encoding='utf-8') as f:
        json.dump(resultados, f, indent=2, ensure_ascii=False) 