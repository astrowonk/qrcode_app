from shiny import App, render, ui, reactive
import segno

app_ui = ui.page_bootstrap(
    ui.h2("Shiny QR Code Generator"),
    ui.layout_sidebar(
        ui.panel_sidebar(
            ui.input_text(id="text", label="Content"),
            ui.input_select(id='img_kind',
                            choices=['png', 'svg'],
                            selected='svg',
                            multiple=False,
                            label='Image Type'),
            ui.input_action_button(id="go", label="Generate!"),
        ), ui.panel_main(ui.output_ui("qrcode"), )))


def server(input, output, session):

    @output
    @render.ui
    def qrcode():
        input.go()
        with reactive.isolate():

            if not input.text():
                return ui.tags.p("Enter Content to generate QR Code.")
            _qrcode = segno.make(input.text(), micro=False)

            if input.img_kind() == 'svg':
                thesrc = _qrcode.svg_data_uri(scale=10)
            else:
                thesrc = _qrcode.png_data_uri(scale=15)
            return ui.tags.img({'src': thesrc, 'width': "600px"})


app = App(app_ui, server)
