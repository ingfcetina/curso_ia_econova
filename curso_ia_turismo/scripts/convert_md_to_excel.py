import os
import re
import pandas as pd
from bs4 import BeautifulSoup
import markdown
from pathlib import Path

def extract_tables_from_markdown(md_content):
    """Extrae las tablas del contenido markdown y las convierte en DataFrames."""
    # Convertir markdown a HTML
    html = markdown.markdown(md_content, extensions=['tables'])
    soup = BeautifulSoup(html, 'html.parser')
    
    # Encontrar todas las tablas
    tables = soup.find_all('table')
    dataframes = []
    
    for table in tables:
        # Extraer encabezados
        headers = []
        for th in table.find_all('th'):
            headers.append(th.get_text().strip())
        
        # Extraer filas
        rows = []
        for tr in table.find_all('tr')[1:]:  # Saltar la fila de encabezados
            row = []
            for td in tr.find_all('td'):
                row.append(td.get_text().strip())
            if row:  # Solo añadir filas no vacías
                rows.append(row)
        
        # Crear DataFrame
        if headers and rows:
            df = pd.DataFrame(rows, columns=headers)
            dataframes.append(df)
    
    return dataframes

def process_markdown_file(file_path):
    """Procesa un archivo markdown y extrae su estructura."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extraer el título del archivo
    title_match = re.search(r'^# (.+?)$', content, re.MULTILINE)
    title = title_match.group(1) if title_match else Path(file_path).stem
    
    # Extraer nombres de secciones
    sections = re.findall(r'^## (.+?)$', content, re.MULTILINE)
    
    # Extraer nombres de subsecciones (hojas)
    subsections = re.findall(r'^### (.+?)$', content, re.MULTILINE)
    
    # Extraer tablas
    tables = extract_tables_from_markdown(content)
    
    return {
        'title': title,
        'sections': sections,
        'subsections': subsections,
        'tables': tables
    }

def create_excel_from_markdowns(directory_path, output_file):
    """Crea un archivo Excel con la estructura de todos los archivos markdown."""
    # Crear un Excel writer
    with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
        # Recorrer todos los archivos markdown
        for root, dirs, files in os.walk(directory_path):
            for file in files:
                if file.endswith('.md'):
                    file_path = os.path.join(root, file)
                    print(f"Procesando: {file_path}")
                    
                    # Procesar el archivo markdown
                    result = process_markdown_file(file_path)
                    
                    # Crear una hoja de resumen
                    summary_data = {
                        'Sección': ['Título', 'Secciones Principales', 'Subsecciones (Hojas)'],
                        'Contenido': [
                            result['title'],
                            '\n'.join(result['sections']),
                            '\n'.join(result['subsections'])
                        ]
                    }
                    summary_df = pd.DataFrame(summary_data)
                    summary_df.to_excel(writer, sheet_name=f"{result['title'][:30]}", index=False)
                    
                    # Crear hojas para cada tabla
                    for i, df in enumerate(result['tables']):
                        sheet_name = f"{result['subsections'][i][:30]}" if i < len(result['subsections']) else f"Tabla_{i+1}"
                        df.to_excel(writer, sheet_name=sheet_name, index=False)

def main():
    # Definir rutas
    base_dir = Path(__file__).parent.parent
    plantillas_dir = base_dir / '03_plantillas'
    output_file = base_dir / 'plantillas_estructura.xlsx'
    
    # Crear el Excel
    create_excel_from_markdowns(plantillas_dir, output_file)
    print(f"\nArchivo Excel creado exitosamente: {output_file}")

if __name__ == "__main__":
    main() 