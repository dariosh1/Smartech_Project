from dash import Dash,dcc,Output,Input
import dash_bootstrap_components as dbc
import dash_html_components as html

app = Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP])


my_text = html.H1('hi bitch',style={'color':'silver'})
my_input = dbc.Input(placeholder='type me bitch',style={'color':'red'})

@app.callback(Output(my_text,component_property='children'),
              Input(my_input,component_property='value'))
def update_text(inp_text):
    return inp_text

app.layout = dbc.Container(
        [   
            dbc.Row([my_text,my_input],class_name='text-center')
        ]
    )

if __name__ == "__main__":
    app.run_server(port='8000')