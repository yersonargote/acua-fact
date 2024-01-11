import gradio as gr


def concepto_tab() -> gr.Blocks:
    with gr.Tab("Gestión Conceptos"):
        gr.Markdown(value="## Buscar Concepto", show_label=False)
