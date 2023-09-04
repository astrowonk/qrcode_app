from dash import Dash, html, dcc, callback, Output, Input, State
import dash_bootstrap_components as dbc
import segno

from pathlib import Path

parent_dir = Path().absolute().stem

app = Dash(__name__,
           url_base_pathname=f"/dash/{parent_dir}/",
           external_stylesheets=[dbc.themes.YETI],
           title="QR Code Generator",
           meta_tags=[
               {
                   "name": "viewport",
                   "content": "width=device-width, initial-scale=1"
               },
           ])
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
    html.Div(id='my-output', style={
        'text-align': 'center',
        'margin': 'auto'
    })
])


@callback(
    Output('my-output', 'children'),
    State('content', 'value'),
    State('img-type', 'value'),
    State('scale', 'value'),
    Input('go', 'n_clicks'),
)
def update_code(content, img_type, scale, _):
    if not content:
        return ''

    _qrcode = segno.make(content, micro=False)
    if img_type == "svg":
        _img = _qrcode.svg_data_uri(scale=scale)
    else:
        _img = _qrcode.png_data_uri(scale=scale)

    return [
        html.Img(
            id='output-image',
            src=_img,
            width=400,
            style={
                'margin': 'auto',
                'display': 'block'
            },
        ),
        html.A(download=f'qrcode.{img_type}',
               href=_img,
               role='button',
               children=f"Download {img_type.upper()}",
               className="btn btn-primary",
               style={
                   'text-align': 'center',
                   'margin': 'auto'
               })
    ]


server = app.server

if __name__ == '__main__':
    app.run(debug=True)
