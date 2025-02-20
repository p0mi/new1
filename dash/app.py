from dash import Dash, html, dash_table, dcc
import requests
import pandas as pd
import plotly.express as px

# Incorporate data
def get_nocodb_data():
    url = "http://localhost:8000/nocodb-data/"
    # headers = {
    #     "xc-token": "C3UrQ22BaOLseRT7wVTTqy3PQ4yg4JV-RLZxnX6T",  # Замените на ваш API-ключ
    # }

    # Получаем данные
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        # Предполагаем, что данные находятся в ключе 'list'
        records = data.get('records', [])
        print(records)
        return pd.DataFrame(records)
    else:
        print("Ошибка при получении данных:", response.status_code)
        return pd.DataFrame()
# Initialize the app
app = Dash(__name__)

# Получаем данные
df = get_nocodb_data()

# App layout
app.layout = html.Div([
    html.Div(children='My First App with Data'),
    dash_table.DataTable(
        data=df.to_dict('records'),
        columns=[{'name': i, 'id': i} for i in df.columns],
        page_size=10
    ),
    dcc.Graph(figure=px.histogram(df, x='Id', y='username', histfunc='avg'))
])

# Run the app
if __name__ == '__main__':
    app.run(debug=True)