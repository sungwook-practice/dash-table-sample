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
        html.P('Input Text'),
        dcc.Input(id='input-text', type='text', value='')
    ]),
    html.Br(),
    html.Div([
        html.P('Table'),
        html.Div(id='output-table')
    ])
])

@app.callback(
    Output(component_id='output-table', component_property='children'),
    [Input(component_id='input-text', component_property='value')]
)
def update_table(input_text):
    filtered_df = df[df['col2'] == input_text]
    return html.Table(
        [html.Tr([html.Th(col) for col in filtered_df.columns])] +
        [html.Tr([
            html.Td(filtered_df.iloc[i][col]) for col in filtered_df.columns
        ]) for i in range(len(filtered_df))]
    )

if __name__ == '__main__':
    app.run_server(debug=True)
