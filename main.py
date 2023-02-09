import dash
import dash_html_components as html
import dash_core_components as dcc
import pandas as pd
from dash.dependencies import Input, Output

app = dash.Dash()

df = pd.DataFrame({
    'col1': [1, 2, 3, 4],
    'col2': ['A', 'B', 'C', 'D'],
    'col3': [10, 20, 30, 40]
})

app.layout = html.Div([
    html.H1('Dashboard'),
    html.Div([
        html.P('입력해주세요'),
        dcc.Input(id='input-text', type='text', value='')
    ]),
    html.Br(),
    html.Div([
        html.P('결과 테이블'),
        html.Table(id='output-table')
    ])
])

@app.callback(
    Output(component_id='output-table', component_property='children'),
    [Input(component_id='input-text', component_property='value')]
)
def update_table(input_text):
    print(f"df: {df}")
    print(f"input:text: {input_text}")
    filtered_df = df[df['col2'] == input_text]
    if len(filtered_df) == 0:
        return html.P('데이터가 없습니다. 데이터를 확인해주세요')
    print(f"filtered_df: {filtered_df}")
    table_rows = []
    for i in range(len(filtered_df)):
        row = []
        for col in filtered_df.columns:
            row.append(html.Td(filtered_df.iloc[i][col]))
        table_rows.append(html.Tr(row))
    return [html.Tr([html.Th(col) for col in filtered_df.columns])] + table_rows

if __name__ == '__main__':
    app.run_server(debug=True)
