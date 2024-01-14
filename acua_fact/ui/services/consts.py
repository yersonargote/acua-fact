HTML_TEMPLATE = """
<html>
  <head>
    <meta charset="utf-8">
    <title>{title}</title>
    <meta name="description" content="App para generar facturas de un acueducto local.">
  </head>

  <body>
    <h1>Acueducto</h1>

    <aside>
      <address id="from">
        Identificación: {persona_id}
        Nombre: {nombre}
        Dirección: {direccion}
        Telefono: {telefono}
        Estrato: {estrato}
      </address>

      <address id="to">
        Fecha de inicio: {fecha_inicio}
        Fecha de fin: {fecha_fin}
        Fecha limite de pago: {fecha_limite_pago}
      </address>
    </aside>

    <dl id="informations">
      <dt>Factura número: </dt>
      <dd>{factura_id}</dd>
    </dl>

    <table>
      <thead>
        <tr>
          <th>Concepto</th>
          <th>Valor</th>
        </tr>
      </thead>
      <tbody>
        {conceptos}
      </tbody>
    </table>

    <footer>
      <table id="total">
        <thead>
          <tr>
            <th>Total</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>{total}</td>
          </tr>
        </tbody>
      </table>
    </footer>
  </body>
</html>
"""


CSS_TEMPLATE = """
@font-face {
  font-family: Pacifico;
  src: url(acua_fact/assets/pacifico.ttf);
}
@font-face {
  font-family: Source Sans Pro;
  font-weight: 400;
  src: url(acua_fact/assets/sourcesanspro-regular.otf);
}
@font-face {
  font-family: Source Sans Pro;
  font-weight: 700;
  src: url(acua_fact/assets/sourcesanspro-bold.otf);
}

@page {
  font-family: Pacifico;
  margin: 3cm;
  @bottom-left {
    color: #1ee494;
    content: 'Slogan';
  }
  @bottom-right {
    color: #a9a;
    content: 'Contacto: +57 123 456 7890 | contacto@acueducto.com';
    font-size: 9pt;
  }
}

html {
  color: #14213d;
  font-family: Source Sans Pro;
  font-size: 11pt;
  line-height: 1.6;
}
body {
  margin: 0;
}

h1 {
  color: #1ee494;
  font-family: Pacifico;
  font-size: 40pt;
  margin: 0;
}

aside {
  display: flex;
  margin: 2em 0 4em;
}
aside address {
  font-style: normal;
  white-space: pre-line;
}
aside address#from {
  color: #a9a;
  flex: 1;
}
aside address#to {
  text-align: right;
}

dl {
  position: absolute;
  right: 0;
  text-align: right;
  top: 0;
}
dt, dd {
  display: inline;
  margin: 0;
}
dt {
  color: #a9a;
}
dt::before {
  content: '';
  display: block;
}
dt::after {
  content: ':';
}

table {
  border-collapse: collapse;
  width: 100%;
}
th {
  border-bottom: .2mm solid #a9a;
  color: #a9a;
  font-size: 10pt;
  font-weight: 400;
  padding-bottom: .25cm;
  text-transform: uppercase;
}
td {
  padding-top: 7mm;
}
td:last-of-type {
  color: #1ee494;
  font-weight: bold;
  text-align: right;
}
th, td {
  text-align: center;
}
th:first-of-type, td:first-of-type {
  text-align: left;
}
th:last-of-type, td:last-of-type {
  text-align: right;
}
footer {
  content: '';
  display: block;
  height: 6cm;
}
table#total {
  background: #f6f6f6;
  border-color: #f6f6f6;
  border-style: solid;
  border-width: 2cm 3cm;
  bottom: 0;
  font-size: 20pt;
  margin: 0 -3cm;
  position: absolute;
  width: 18cm;
}
"""
