import gradio as gr

from acua_fact.server.app import app as fastapi_app
from acua_fact.ui.ui import build_ui_blocks

ui = build_ui_blocks()
ui.queue()
app = gr.mount_gradio_app(app=fastapi_app, blocks=ui.queue(), path="/")
