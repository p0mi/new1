# Import packages
from dash import Dash, html, dash_table
import pandas as pd

# Incorporate data
def user_list(request):
    table_id = 'ms0ix9oy5vzfw4n'  # ID вашей таблицы
    try:
        records = get_users(table_id)
        print(records)
    except Exception as e:
        records = []
        print(e)
    
    context = {'records': records}
    return render(request, 'app/user_list.html', context)

# Initialize the app
app = Dash()

# App layout
app.layout = [
    html.Div(children='My First App with Data'),
    dash_table.DataTable(data=df.to_dict('records'), page_size=10)
]

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
