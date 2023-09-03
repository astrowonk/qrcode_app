from dash import Dash, html, dcc, callback, Output, Input, State
import dash_bootstrap_components as dbc
import segno

app = Dash(__name__, external_stylesheets=[dbc.themes.YETI])

app.layout = html.Div([
    html.H1(children='QR Code App', style={'textAlign': 'center'}),
    dbc.InputGroup([
        dbc.InputGroupText("Image Type and Scale"),
        dbc.Input(id='scale', name="Scale", type='number', value=10),
        dbc.Select(id='img-type',
                   options=['svg', 'png'],
                   name="Image Type",
                   persistence=True,
                   persistence_type='local',
                   value='svg'),
    ],
                   style={
                       "width": "60%",
                       'margin': 'auto'
                   }),
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
    html.Div(
        html.Img(
            id='output-image',
            width=600,
            style={
                'margin': 'auto',
                'display': 'block'
            },
        ), )
])


@callback(
    Output('output-image', 'src'),
    State('content', 'value'),
    State('img-type', 'value'),
    State('scale', 'value'),
    Input('go', 'n_clicks'),
)
def update_code(content, img_type, scale, _):
    if not content:
        return ''

    _qrcode = segno.make(content, micro=False)
    print(type(scale))
    if img_type == "svg":
        return _qrcode.svg_data_uri(scale=scale)
    return _qrcode.png_data_uri(scale=scale)


if __name__ == '__main__':
    app.run(debug=True)