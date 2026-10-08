"""Comprobación reproducible de ejemplos extraídos; no instala paquetes ni usa la red."""
import json, subprocess, sys, tempfile
from pathlib import Path
blocks={b['id']:b for b in json.load(open('blocks3.json'))}
inputs={7:'25\n25\n',8:'Ana\n2000\n',10:'Ana\n2000\n1.75\n',11:'50\n',19:'Admin\n',20:'100\n',25:'si\n',26:'21\n',28:'secreta123\n',29:'8\n',63:'10\n',78:'8\n2\n4\n',100:'si\n',105:'Ana García\n',106:'reconocer\n',107:'Python es útil\np\n',119:'Ana\n',125:'Matrix\n',127:'2\n1\nAna\n123\n2\n3\n',131:'25\n',132:'2\n',133:'2\n',136:'error\n25\n',139:'2.5\n',140:'1\n',141:'8\n2\n',142:'?\n/\n8\n0\n+\nx\n+\n2\n3\nsalir\n',167:'4\n'}
nonpython=set(range(151,163))|{168,241}
expected_errors={11:'TypeError',30:'SyntaxError',50:'IndexError',188:'TypeError'}
deps={39:[38],40:[38],42:[41],87:[86],171:[170],173:[172],180:[179],182:[179,180],199:[198],207:[206],208:[206]}
extra={2:'valor = 42\n',222:'resultado = None\n'}
reports=[]
for n,b in blocks.items():
 if n in nonpython:
  reports.append({'id':n,'status':'terminal_o_esquema_no_ejecutado'});continue
 if n==64:
  reports.append({'id':n,'status':'bucle_infinito_intencional_revisado_sin_ejecutar'});continue
 code=extra.get(n,'')+''.join(blocks[k]['code']+'\n' for k in deps.get(n,[]))+b['code']
 with tempfile.TemporaryDirectory(prefix='manual-python-') as tmp:
  p=Path(tmp)
  for name,txt in {'datos.txt':'primera\nsegunda\n','nombres.txt':'Ana\nLuis\n','peliculas.txt':'Matrix\n','operaciones.py':blocks[148]['code']+'\n'+blocks[165]['code'],'textos.py':blocks[166]['code'],'saludos.py':'def saludo_formal(nombre):\n    return f"Estimado/a {nombre}, reciba un cordial saludo."\n'}.items():(p/name).write_text(txt,encoding='utf-8')
  (p/'ejemplo.py').write_text(code,encoding='utf-8')
  try:
   r=subprocess.run([sys.executable,str(p/'ejemplo.py')],cwd=p,input=inputs.get(n,''),text=True,capture_output=True,timeout=4)
   expected=expected_errors.get(n)
   ok=(expected in r.stderr if expected else r.returncode==0)
   reports.append({'id':n,'status':'error_didactico_confirmado' if ok and expected else 'ejecutado' if ok else 'revisar','stdout':r.stdout,'stderr':r.stderr})
  except subprocess.TimeoutExpired:reports.append({'id':n,'status':'timeout'})
Path('resultados-ejemplos.json').write_text(json.dumps({'python':sys.version,'resultados':reports},ensure_ascii=False,indent=2),encoding='utf-8')
from collections import Counter
print(Counter(r['status'] for r in reports))
for r in reports:
 if r['status'] in {'revisar','timeout'}:print(r)
