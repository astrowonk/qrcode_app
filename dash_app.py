from dash import Dash, html, dcc, callback, Output, Input, State
import dash_bootstrap_components as dbc
import segno

app = Dash(__name__, external_stylesheets=[dbc.themes.YETI])

app.layout = html.Div([
    html.H1(children='QR Code App', style={'textAlign': 'center'}),
    dbc.InputGroup([
        dbc.Input(
            id='content',
            value='',
            debounce=True,
            placeholder="Enter text for QR Code",
        ),
        dbc.Button(id='go', children="Make QR Code!"),
    ],
                   style={
                       "width": "60%",
                       "margin": "auto"
                   }),
    html.Div(html.Img(id='output-image', width=600))
])


@callback(
    Output('output-image', 'src'),
    State('content', 'value'),
    Input('go', 'n_clicks'),
)
def update_code(content, _):
    if not content:
        return ''

    _qrcode = segno.make(content, micro=False)

    return _qrcode.svg_data_uri()


if __name__ == '__main__':
    app.run(debug=True)