import pandas as pd
import plotly.graph_objects as go
from openpyxl import Workbook
from openpyxl.drawing.image import Image

# Output files
output_file = '../../data/graph_data.xlsx'
output_image = '../../data/graph_data.html'

# Crear un DataFrame de ejemplo con latitud y longitud
data = {
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston'],
    'Lat': [40.7128, 34.0522, 41.8781, 29.7604],
    'Lon': [-74.0060, -118.2437, -87.6298, -95.3698]
}
df = pd.DataFrame(data)

# Crear el gráfico interactivo con plotly
fig = go.Figure()

# Añadir marcadores para cada ciudad
for i, row in df.iterrows():
    fig.add_trace(go.Scattergeo(
        lon = [row['Lon']],
        lat = [row['Lat']],
        text = row['City'],
        mode = 'markers',
        marker = dict(size = 10),
        name = row['City']
    ))

fig.update_layout(
    title = 'Ciudades en Estados Unidos',
    geo_scope='usa'
)

# Guardar el gráfico como HTML
fig.write_html(output_image)

# Crear un archivo Excel y añadir el mapa como una imagen
wb = Workbook()
ws = wb.active

img = Image(output_image)
ws.add_image(img, 'A1')

# Guardar el archivo Excel
wb.save(output_file)

print(f"Archivo {output_file} creado exitosamente.")
