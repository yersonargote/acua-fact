import gradio as gr

from acua_fact.ui.tabs.factura import factura_tab
from acua_fact.ui.tabs.persona import persona_tab


def build_ui_blocks() -> gr.Blocks:
    with gr.Blocks(title="ACUA Fact") as blocks:
        gr.Markdown("# ACUA Fact")
        factura_tab()
        persona_tab()

    return blocks
