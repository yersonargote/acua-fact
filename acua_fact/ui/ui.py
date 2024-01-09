import gradio as gr

from acua_fact.ui.tabs.persona import persona_tab

# TODO: Implementar función de limpiar campos.


def build_ui_blocks() -> gr.Blocks:
    with gr.Blocks(title="ACUA Fact") as blocks:
        gr.Markdown("# ACUA Fact")
        persona_tab()

    return blocks
