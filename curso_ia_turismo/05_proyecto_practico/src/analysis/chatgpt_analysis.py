import pandas as pd
import numpy as np
from openai import OpenAI
import json
import os
from dotenv import load_dotenv
from typing import Dict, List, Any

class ChatGPTAnalyzer:
    def __init__(self):
        """Inicializa el analizador de ChatGPT."""
        load_dotenv()
        self.client = OpenAI()
        self.model = "gpt-4"
        self.temperature = 0.7

    def analyze_review(self, text: str) -> Dict[str, Any]:
        """
        Analiza una reseña individual.
        
        Args:
            text: Texto de la reseña
            
        Returns:
            Dict con el análisis
        """
        prompt = f"""Analiza la siguiente reseña de un servicio turístico y proporciona:
        1. Sentimiento general (positivo/neutral/negativo)
        2. Aspectos destacados
        3. Áreas de mejora
        4. Recomendaciones
        
        Reseña: {text}
        
        Responde en formato JSON."""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            temperature=self.temperature
        )

        return json.loads(response.choices[0].message.content)

    def analyze_category(self, reviews: List[str], category: str) -> Dict[str, Any]:
        """
        Analiza un conjunto de reseñas de una categoría.
        
        Args:
            reviews: Lista de reseñas
            category: Categoría a analizar
            
        Returns:
            Dict con el análisis de la categoría
        """
        prompt = f"""Analiza las siguientes reseñas de {category} y proporciona:
        1. Tendencias generales
        2. Fortalezas comunes
        3. Debilidades recurrentes
        4. Recomendaciones estratégicas
        
        Reseñas: {reviews}
        
        Responde en formato JSON."""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            temperature=self.temperature
        )

        return json.loads(response.choices[0].message.content)

    def generate_recommendations(self, df: pd.DataFrame) -> Dict[str, Any]:
        """
        Genera recomendaciones basadas en todas las reseñas.
        
        Args:
            df: DataFrame con las reseñas
            
        Returns:
            Dict con recomendaciones
        """
        prompt = f"""Basado en el siguiente conjunto de reseñas, proporciona:
        1. Resumen ejecutivo
        2. Principales hallazgos
        3. Recomendaciones estratégicas
        4. Plan de acción
        
        Datos: {df.to_dict('records')}
        
        Responde en formato JSON."""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            temperature=self.temperature
        )

        return json.loads(response.choices[0].message.content)

    def analyze_by_platform(self, df: pd.DataFrame) -> Dict[str, Any]:
        """
        Analiza reseñas por plataforma de origen.
        
        Args:
            df: DataFrame con las reseñas
            
        Returns:
            Dict con análisis por plataforma
        """
        platforms = df['origen'].unique()
        analysis = {}

        for platform in platforms:
            platform_reviews = df[df['origen'] == platform]['texto'].tolist()
            prompt = f"""Analiza las reseñas de {platform} y proporciona:
            1. Tendencias específicas de la plataforma
            2. Fortalezas y debilidades
            3. Recomendaciones específicas
            
            Reseñas: {platform_reviews}
            
            Responde en formato JSON."""

            response = self.client.chat.completions.create(
                model=self.model,
                messages=[{"role": "user", "content": prompt}],
                temperature=self.temperature
            )

            analysis[platform] = json.loads(response.choices[0].message.content)

        return analysis

    def analyze_by_language(self, df: pd.DataFrame) -> Dict[str, Any]:
        """
        Analiza reseñas por idioma.
        
        Args:
            df: DataFrame con las reseñas
            
        Returns:
            Dict con análisis por idioma
        """
        languages = df['idioma'].unique()
        analysis = {}

        for language in languages:
            language_reviews = df[df['idioma'] == language]['texto'].tolist()
            prompt = f"""Analiza las reseñas en {language} y proporciona:
            1. Tendencias específicas del idioma
            2. Fortalezas y debilidades
            3. Recomendaciones específicas
            
            Reseñas: {language_reviews}
            
            Responde en formato JSON."""

            response = self.client.chat.completions.create(
                model=self.model,
                messages=[{"role": "user", "content": prompt}],
                temperature=self.temperature
            )

            analysis[language] = json.loads(response.choices[0].message.content)

        return analysis

    def analyze_by_customer_type(self, df: pd.DataFrame) -> Dict[str, Any]:
        """
        Analiza reseñas por tipo de cliente.
        
        Args:
            df: DataFrame con las reseñas
            
        Returns:
            Dict con análisis por tipo de cliente
        """
        customer_types = df['tipo_cliente'].unique()
        analysis = {}

        for customer_type in customer_types:
            type_reviews = df[df['tipo_cliente'] == customer_type]['texto'].tolist()
            prompt = f"""Analiza las reseñas de clientes {customer_type} y proporciona:
            1. Tendencias específicas del tipo de cliente
            2. Fortalezas y debilidades
            3. Recomendaciones específicas
            
            Reseñas: {type_reviews}
            
            Responde en formato JSON."""

            response = self.client.chat.completions.create(
                model=self.model,
                messages=[{"role": "user", "content": prompt}],
                temperature=self.temperature
            )

            analysis[customer_type] = json.loads(response.choices[0].message.content)

        return analysis

if __name__ == "__main__":
    # Ejemplo de uso
    analyzer = ChatGPTAnalyzer()
    
    # Cargar datos
    df = pd.read_csv('../../demo/data/reseñas.csv')
    
    # Realizar análisis
    analysis = {
        'general': analyzer.generate_recommendations(df),
        'by_platform': analyzer.analyze_by_platform(df),
        'by_language': analyzer.analyze_by_language(df),
        'by_customer_type': analyzer.analyze_by_customer_type(df)
    }
    
    # Guardar resultados
    with open('../../demo/results/chatgpt_analysis.json', 'w', encoding='utf-8') as f:
        json.dump(analysis, f, indent=2, ensure_ascii=False) 