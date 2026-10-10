// Imprime el HTML generado por generar_pdf.py como PDF A4 con número de página.
const { chromium } = require('playwright');

(async () => {
  const [entrada, salida] = process.argv.slice(2);
  const navegador = await chromium.launch();
  const pagina = await navegador.newPage();
  await pagina.goto('file://' + entrada, { waitUntil: 'load' });
  await pagina.pdf({
    path: salida,
    format: 'A4',
    margin: { top: '18mm', bottom: '18mm', left: '16mm', right: '16mm' },
    displayHeaderFooter: true,
    headerTemplate: '<span></span>',
    footerTemplate: '<div style="font-size:8px;width:100%;text-align:center;color:#666">' +
      'Manual Maestro de Linux y Shell Scripting · v3 · <span class="pageNumber"></span> / <span class="totalPages"></span></div>',
    outline: true,
  });
  await navegador.close();
})();
