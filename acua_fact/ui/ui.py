import gradio as gr

from acua_fact.ui.tabs.factura import factura_tab
from acua_fact.ui.tabs.pago import pago_tab
from acua_fact.ui.tabs.persona import persona_tab

css = """
.label {
    font-size: 0.1rem !important;
    font-weight: bold;
}
"""


def build_ui_blocks() -> gr.Blocks:
    with gr.Blocks(title="ACUA Fact", css=css) as blocks:
        gr.Markdown("# ACUA Fact")
        factura_tab()
        pago_tab()
        persona_tab()

    return blocks
