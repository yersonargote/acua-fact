from weasyprint import CSS, HTML
from weasyprint.text.fonts import FontConfiguration

from acua_fact.ui.services.consts import CSS_TEMPLATE, HTML_TEMPLATE


def generar_pdf(
    title: str,
    persona_id: int,
    nombre: str,
    direccion: str,
    telefono: str,
    estrato: int,
    fecha_inicio: str,
    fecha_fin: str,
    fecha_limite_pago: str,
    factura_id: int,
    conceptos: list,
    total: float,
):
    html_conceptos = ""
    for concepto in conceptos:
        html_conceptos += f"""
        <tr>
          <td>{concepto.nombre}</td>
          <td>{concepto.valor}</td>
        </tr>
        """

    font_config = FontConfiguration()
    html = HTML(
        string=HTML_TEMPLATE.format(
            title=title,
            persona_id=persona_id,
            nombre=nombre,
            direccion=direccion,
            telefono=telefono,
            estrato=estrato,
            fecha_inicio=fecha_inicio,
            fecha_fin=fecha_fin,
            fecha_limite_pago=fecha_limite_pago,
            factura_id=factura_id,
            conceptos=html_conceptos,
            total=total,
        )
    )
    css = CSS(string=CSS_TEMPLATE, font_config=font_config)
    pdf_path = f"acua_fact/ui/assets/factura{factura_id}.pdf"
    html.write_pdf(
        pdf_path,
        stylesheets=[css],
        font_config=font_config,
    )
    return pdf_path
