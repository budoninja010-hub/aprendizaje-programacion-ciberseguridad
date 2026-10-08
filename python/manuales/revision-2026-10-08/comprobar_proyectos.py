"""Comprueba resultados, efectos en archivos y ejemplos que solo definen funciones."""
import contextlib, io, json, os, tempfile, unittest
from pathlib import Path
B={b['id']:b['code'] for b in json.load(open('blocks3.json'))}
P=json.load(open('fragmentos_adicionales.json'))
def cargar(n):
 ns={'__name__':'__main__'}
 with contextlib.redirect_stdout(io.StringIO()):exec(B[n],ns)
 return ns
class Proyectos(unittest.TestCase):
 def test_saludos_iniciales(self):
  for a,z,expected in [(2022,2069,'¡Hola, mundo!'),(4925,4963,'Iniciando mi viaje en Python')]:
   code=''.join(p['text'] for p in P if a<=p['start']<z);out=io.StringIO()
   with contextlib.redirect_stdout(out):exec(code,{})
   self.assertEqual(out.getvalue().strip(),expected)
 def test_atributos_mutables(self):
  for a,z,shared in [(121617,121895,True),(122204,122398,False)]:
   ns={};code=''.join(p['text'] for p in P if a<=p['start']<z)
   with contextlib.redirect_stdout(io.StringIO()):exec(code,ns)
   fido=ns['Perro']();rex=ns['Perro']();fido.agregar_truco('sentarse')
   self.assertEqual('sentarse' in rex.trucos,shared)
 def test_censura(self):
  ns=cargar(103);self.assertEqual(ns['resultado'],'Este ******* es muy *******')
 def test_academico(self):
  ns=cargar(228);self.assertEqual(ns['estadisticas'],{'max':9.2,'min':6.5,'prom':7.8,'total_aprobados':3})
  self.assertEqual([x['nombre'] for x in ns['clasificacion']],['Ana','Luis','María','Carlos'])
 def test_generador(self):
  ns=cargar(211);self.assertEqual(list(ns['contar']()),[1,2,3])
 def test_args_kwargs(self):
  ns=cargar(213)
  with contextlib.redirect_stdout(io.StringIO()):self.assertEqual(ns['sumar'](1,2,3),6)
 def test_valor_predeterminado(self):
  ns=cargar(238);self.assertEqual(ns['agregar']('a'),['a']);self.assertEqual(ns['agregar']('b'),['b'])
 def test_asyncio_y_decorador(self):
  ns=cargar(243)
  with contextlib.redirect_stdout(io.StringIO()):ns['asyncio'].run(ns['tarea']())
  ns=cargar(245);out=io.StringIO()
  with contextlib.redirect_stdout(out):ns['proceso_lento']()
  self.assertIn('La función tardó',out.getvalue())
 def test_sha256(self):
  ns=cargar(248)
  with tempfile.TemporaryDirectory() as tmp:
   p=Path(tmp)/'dato';p.write_bytes(b'abc')
   self.assertEqual(ns['calcular_sha256'](p),'ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad')
 def test_persistencia_y_reporte(self):
  old=os.getcwd()
  with tempfile.TemporaryDirectory() as tmp:
   try:
    os.chdir(tmp);ns=cargar(247);ns['gestor'].agregar('Otra tarea')
    recargado=ns['GestorTareas']('mis_tareas.json');self.assertEqual(len(recargado.tareas),2)
    cargar(254);reporte=json.loads(Path('reporte_auditoria.json').read_text())
    self.assertEqual(len(reporte),2);self.assertTrue(all(a['tipo']=='Intento Fallido' for a in reporte))
   finally:os.chdir(old)
if __name__=='__main__':unittest.main(verbosity=2)
